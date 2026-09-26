from database.db import get_connection
import re
from exceptions.exception import DoctorNotFoundException

def get_all_doctors(sort_by="name"):
    """Return all doctors sorted by the selected field."""

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                doctor_id,
                name,
                specialization
            FROM doctors
        """

        cursor.execute(query)

        doctors = cursor.fetchall()

        # Lambda + sorted
        if sort_by == "specialization":
            doctors = sorted(
                doctors,
                key=lambda doctor: doctor["specialization"]
            )
        else:
            doctors = sorted(
                doctors,
                key=lambda doctor: doctor["name"]
            )

        return doctors

    except Exception as error:

        print("Failed to fetch doctors:", error)

        return []

    finally:

        cursor.close()
        connection.close()
def search_doctor_by_specialization(specialization):

    if not re.fullmatch(
        r"[A-Za-z ]+",
        specialization
    ):
        raise ValueError(
            "Specialization must contain only letters."
        )

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                doctor_id,
                name,
                specialization
            FROM doctors
            WHERE specialization LIKE %s
        """

        values = (f"%{specialization}%",)

        cursor.execute(query, values)

        doctors = cursor.fetchall()

        if not doctors:
            raise DoctorNotFoundError(
                "No doctor found for this specialization."
            )

        # filter() + lambda
        doctors = list(
            filter(
                lambda doctor:
                    specialization.lower()
                    in doctor["specialization"].lower(),
                doctors
            )
        )

        return doctors

    except DoctorNotFoundError:
        raise

    except Exception as error:

        print("Failed to search doctors:", error)

        return []

    finally:

        cursor.close()
        connection.close()
def book_appointment(
    user_id,
    doctor_id,
    appointment_date,
    reason
):
    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Find patient ID using logged-in user ID
        query = """
            SELECT patient_id
            FROM patients
            WHERE user_id = %s
        """

        cursor.execute(query, (user_id,))

        patient = cursor.fetchone()

        if patient is None:
            print("Patient profile not found.")
            return False

        patient_id = patient[0]

        # Check whether doctor exists
        query = """
            SELECT doctor_id
            FROM doctors
            WHERE doctor_id = %s
        """

        cursor.execute(query, (doctor_id,))

        doctor = cursor.fetchone()

        if doctor is None:
            print("Doctor not found.")
            return False

        # Insert appointment
        query = """
            INSERT INTO appointments
            (
                patient_id,
                doctor_id,
                appointment_date,
                reason,
                status
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            patient_id,
            doctor_id,
            appointment_date,
            reason,
            "BOOKED"
        )

        cursor.execute(query, values)

        connection.commit()

        return True

    except Exception as error:

        connection.rollback()

        print("Failed to book appointment:", error)

        return False

    finally:

        cursor.close()
        connection.close()
def view_my_appointments(user_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                a.appointment_id,
                a.appointment_date,
                a.reason,
                a.status,
                a.medicine,
                a.dosage,
                a.doctor_notes
            FROM appointments a
            JOIN patients p
                ON a.patient_id = p.patient_id
            WHERE p.user_id = %s
        """

        values = (user_id,)

        cursor.execute(query, values)

        my_appointments = cursor.fetchall()

        for appointment in my_appointments:

            print("\n-----------------------------")
            print("Appointment ID:", appointment["appointment_id"])
            print("Date:", appointment["appointment_date"])
            print("Reason:", appointment["reason"])
            print("Status:", appointment["status"])
            print("Medicine:", appointment["medicine"])
            print("Dosage:", appointment["dosage"])
            print("Doctor Notes:", appointment["doctor_notes"])

    except Exception as error:
        print("Failed to fetch appointments:", error)

    finally:
        cursor.close()
        connection.close()