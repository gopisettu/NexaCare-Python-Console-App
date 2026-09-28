from datetime import datetime
from collections import Counter, defaultdict


from database.db import get_connection
from exceptions.exception import AppointmentAlreadyCompletedError,AppointmentNotFoundError
from utils.decorators import log_activity


@log_activity
def get_all_upcoming_appointments(user_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                ap.appointment_id,
                ap.appointment_date,
                pa.name AS patient_name,
                pa.age,
                pa.phone,
                ap.reason,
                ap.status
            FROM appointments AS ap
            JOIN doctors AS d
                ON ap.doctor_id = d.doctor_id
            JOIN patients AS pa
                ON ap.patient_id = pa.patient_id
            WHERE d.user_id = %s
              AND ap.status = 'BOOKED'
            ORDER BY ap.appointment_date
        """

        values = (user_id,)

        cursor.execute(query, values)

        appointments = cursor.fetchall()

        return appointments

    except Exception as error:

        print(
            "Failed to fetch upcoming appointments:",
            error
        )

        return []

    else:

        print("Upcoming appointments fetched successfully.")

    finally:

        cursor.close()
        connection.close()


@log_activity
def get_all_completed_appointments(user_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                ap.appointment_id,
                ap.appointment_date,
                pa.name AS patient_name,
                pa.age,
                ap.reason,
                ap.status,
                ap.diagnosis,
                ap.medicine,
                ap.dosage,
                ap.duration,
                ap.doctor_notes
            FROM appointments AS ap
            JOIN doctors AS d
                ON ap.doctor_id = d.doctor_id
            JOIN patients AS pa
                ON ap.patient_id = pa.patient_id
            WHERE d.user_id = %s
              AND ap.status = 'COMPLETED'
            ORDER BY ap.appointment_date DESC
        """

        values = (user_id,)

        cursor.execute(query, values)

        appointments = cursor.fetchall()

        return appointments

    except Exception as error:

        print(
            "Failed to fetch completed appointments:",
            error
        )

        return []

    finally:

        cursor.close()
        connection.close()


@log_activity
def complete_appointment(
    appointment_id,
    user_id,
    diagnosis,
    medicine,
    dosage,
    duration,
    doctor_notes
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            SELECT
                ap.appointment_id,
                ap.status
            FROM appointments AS ap
            JOIN doctors AS d
                ON ap.doctor_id = d.doctor_id
            WHERE ap.appointment_id = %s
              AND d.user_id = %s
        """

        values = (
            appointment_id,
            user_id
        )

        cursor.execute(query, values)

        appointment = cursor.fetchone()

        if appointment is None:

            raise AppointmentNotFoundError(
                "Appointment not found or "
                "appointment does not belong to this doctor."
            )

        if appointment[1] == "COMPLETED":

            raise AppointmentAlreadyCompletedError(
                "This appointment is already completed."
            )

        query = """
            UPDATE appointments
            SET
                status = 'COMPLETED',
                diagnosis = %s,
                medicine = %s,
                dosage = %s,
                duration = %s,
                doctor_notes = %s
            WHERE appointment_id = %s
        """

        values = (
            diagnosis,
            medicine,
            dosage,
            duration,
            doctor_notes,
            appointment_id
        )

        cursor.execute(query, values)

        connection.commit()

        return True

    except (
        AppointmentNotFoundError,
        AppointmentAlreadyCompletedError
    ) as error:

        connection.rollback()

        print(error)

        return False

    except Exception as error:

        connection.rollback()

        print(
            "Failed to complete appointment:",
            error
        )

        return False

    finally:

        cursor.close()
        connection.close()


@log_activity
def provide_prescription(
    appointment_id,
    user_id,
    **prescription_details
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            SELECT
                ap.appointment_id
            FROM appointments AS ap
            JOIN doctors AS d
                ON ap.doctor_id = d.doctor_id
            WHERE ap.appointment_id = %s
              AND d.user_id = %s
        """

        values = (
            appointment_id,
            user_id
        )

        cursor.execute(query, values)

        appointment = cursor.fetchone()

        if appointment is None:

            raise AppointmentNotFoundError(
                "Appointment not found or "
                "appointment does not belong to this doctor."
            )

        diagnosis = prescription_details.get(
            "diagnosis"
        )

        medicine = prescription_details.get(
            "medicine"
        )

        dosage = prescription_details.get(
            "dosage"
        )

        duration = prescription_details.get(
            "duration"
        )

        doctor_notes = prescription_details.get(
            "doctor_notes"
        )

        query = """
            UPDATE appointments
            SET
                diagnosis = %s,
                medicine = %s,
                dosage = %s,
                duration = %s,
                doctor_notes = %s
            WHERE appointment_id = %s
        """

        values = (
            diagnosis,
            medicine,
            dosage,
            duration,
            doctor_notes,
            appointment_id
        )

        cursor.execute(query, values)

        connection.commit()

        return True

    except AppointmentNotFoundError as error:

        connection.rollback()

        print(error)

        return False

    except Exception as error:

        connection.rollback()

        print(
            "Failed to provide prescription:",
            error
        )

        return False

    finally:

        cursor.close()
        connection.close()
        
def get_appointment_statistics(*statuses):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                a.status,
                d.name AS doctor_name
            FROM appointments AS a
            JOIN doctors AS d
                ON a.doctor_id = d.doctor_id
        """

        cursor.execute(query)

        appointments = cursor.fetchall()

        if statuses:
            appointments = list(
                filter(
                    lambda appointment:
                    appointment["status"] in statuses,
                    appointments
                )
            )

        status_count = Counter(
            appointment["status"]
            for appointment in appointments
        )

        doctor_count = Counter(
            appointment["doctor_name"]
            for appointment in appointments
        )

        return {
            "total": len(appointments),
            "status_count": status_count,
            "doctor_count": doctor_count
        }

    except Exception as error:
        print("Failed to generate statistics:", error)
        return None

    finally:
        cursor.close()
        connection.close()
        
def get_doctor_wise_appointments():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                a.appointment_id,
                d.name AS doctor_name,
                d.specialization,
                p.name AS patient_name,
                a.appointment_date,
                a.reason,
                a.status
            FROM appointments AS a
            JOIN doctors AS d
                ON a.doctor_id = d.doctor_id
            JOIN patients AS p
                ON a.patient_id = p.patient_id
            ORDER BY d.name, a.appointment_date
        """

        cursor.execute(query)

        appointments = cursor.fetchall()

        doctor_appointments = defaultdict(list)

        for appointment in appointments:

            doctor_appointments[
                appointment["doctor_name"]
            ].append(appointment)

        return doctor_appointments

    except Exception as error:
        print(
            "Failed to fetch doctor-wise appointments:",
            error
        )
        return {}

    finally:
        cursor.close()
        connection.close()
        