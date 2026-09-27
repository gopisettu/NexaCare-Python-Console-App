from database.db import get_connection


def get_all_upcoming_appointments(user_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                ap.appointment_id,
                ap.appointment_date,
                pa.name AS patient_name,
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
              AND ap.status = 'BOOKED'
            ORDER BY ap.appointment_date
        """

        values = (user_id,)

        cursor.execute(query, values)

        appointments = cursor.fetchall()

        return appointments

    except Exception as error:

        print(
            "Failed to fetch appointment details:",
            error
        )

        return []

    finally:

        cursor.close()
        connection.close()