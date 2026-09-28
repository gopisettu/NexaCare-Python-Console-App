from database.db import get_connection
from exceptions.exception import UsernameNotFoundError
def register_user(
    username,
    password,
    role,
    name,
    age=None,
    phone=None,
    specialization=None
):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Insert into users table
        query = """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s)
        """

        values = (username, password, role)

        cursor.execute(query, values)

        user_id = cursor.lastrowid

        # Insert patient profile
        if role == "PATIENT":

            query = """
                INSERT INTO patients
                (user_id, name, age, phone)
                VALUES (%s, %s, %s, %s)
            """

            values = (user_id, name, age, phone)

            cursor.execute(query, values)

        # Insert doctor profile
        elif role == "DOCTOR":

            query = """
                INSERT INTO doctors
                (user_id, name, specialization)
                VALUES (%s, %s, %s)
            """

            values = (user_id, name, specialization)

            cursor.execute(query, values)

        connection.commit()

        return user_id

    except Exception as error:
        connection.rollback()
        print("Registration failed:", error)
        return None

    finally:
        cursor.close()
        connection.close()
  


def login_user(username, password):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT user_id, username, password, role
            FROM users
            WHERE username = %s
        """

        cursor.execute(query, (username,))

        user = cursor.fetchone()

        if user is None:
            raise UsernameNotFoundError(
                "Username not found."
            )

        if user["password"] != password:
            return None

        return user

    except UsernameNotFoundError:
        raise

    except Exception as err:
        print("Login Failed:", err)
        return None

    finally:
        cursor.close()
        connection.close()