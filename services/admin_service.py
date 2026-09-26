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
        print("Failed to add Patient Details")
        return None
    else:
        connection.commit()
        return user_id
    finally:
        cursor.close()
        connection.close()


def get_all_appointments():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
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
        """
        appointments=cursor.execute(query)
        return cursor.fetchall()
        
    except Exception as error:
        print("Failed to fetch appointments:", error)
        return []
    else:
        return appointments
    finally:
        cursor.close()
        connection.close()

        