from database.db import get_connection


def add_doctor(username, password, name, specialization):
    """Add a doctor user and doctor profile."""

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s)
        """

        values = (username, password, "DOCTOR")

        cursor.execute(query, values)

        user_id = cursor.lastrowid

        query = """
            INSERT INTO doctors
            (user_id, name, specialization)
            VALUES (%s, %s, %s)
        """

        values = (user_id, name, specialization)

        cursor.execute(query, values)

    except Exception as error:
        connection.rollback()
        print("Failed to add doctor:", error)
        return None

    else:
        connection.commit()
        return user_id

    finally:
        cursor.close()
        connection.close()


def add_patient(username, password, name, age, phone):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query = """
        insert into users(username,password,role)
        values(%s,%s,%s)
        """
        values = (username, password, "PATIENT")
        cursor.execute(query, values)
        user_id = cursor.lastrowid
        patient_info = """
         insert into patients(user_id,name,age,phone)
         values(%s,%s,%s,%s)
         """
        values_info = (user_id, name, age, phone)
        cursor.execute(patient_info, values_info)

    except Exception as err:
        connection.rollback()
        print("Failed to add Patient Details",err)
        return None
    else:
        connection.commit()
        return user_id
    finally:
        cursor.close()
        connection.close()


def get_all_appointments(page=1, page_size=2):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        offset = (page - 1) * page_size

        query = """
            SELECT
                a.appointment_id,
                p.name AS patient_name,
                d.name AS doctor_name,
                d.specialization,
                a.appointment_date,
                a.reason,
                a.status,
                a.diagnosis,
                a.medicine,
                a.dosage,
                a.duration,
                a.doctor_notes
            FROM appointments a
            JOIN patients p
                ON a.patient_id = p.patient_id
            JOIN doctors d
                ON a.doctor_id = d.doctor_id
            ORDER BY a.appointment_date
            LIMIT %s OFFSET %s
        """

        values = (page_size, offset)

        cursor.execute(query, values)

        return cursor.fetchall()

    except Exception as error:

        print("Failed to fetch appointments:", error)

        return []

    finally:

        cursor.close()
        connection.close()
def delete_patient(patient_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            SELECT user_id
            FROM patients
            WHERE patient_id = %s
        """

        cursor.execute(query, (patient_id,))

        patient = cursor.fetchone()

        if patient is None:
            print("Patient not found.")
            return False

        user_id = patient[0]

        # Delete appointments
        query = """
            DELETE FROM appointments
            WHERE patient_id = %s
        """

        cursor.execute(query, (patient_id,))

        # Delete patient record
        query = """
            DELETE FROM patients
            WHERE patient_id = %s
        """

        cursor.execute(query, (patient_id,))

        # Delete user account
        query = """
            DELETE FROM users
            WHERE user_id = %s
        """

        cursor.execute(query, (user_id,))

        connection.commit()

        return True

    except Exception as err:

        connection.rollback()

        print("Failed to delete patient:", err)

        return False

    finally:

        cursor.close()
        connection.close()

def export_patient_details():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    file_name = "patient_report.txt"

    try:
        query = """
            SELECT
                patient_id,
                name,
                age,
                phone
            FROM patients
            ORDER BY patient_id
        """

        cursor.execute(query)

        patients = cursor.fetchall()

        with open(file_name, "w", encoding="utf-8") as file:

            file.write("NEXACARE MINI - PATIENT REPORT\n")
            file.write("================================\n\n")

            for patient in patients:

                file.write(
                    f"Patient ID: {patient['patient_id']}\n"
                )

                file.write(
                    f"Name: {patient['name']}\n"
                )

                file.write(
                    f"Age: {patient['age']}\n"
                )

                file.write(
                    f"Phone: {patient['phone']}\n"
                )

                file.write("\n")

        return file_name

    except Exception as error:

        print("Failed to export patient details:", error)

        return None

    finally:

        cursor.close()
        connection.close()
