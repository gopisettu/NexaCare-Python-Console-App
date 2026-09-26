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