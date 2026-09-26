import mysql.connector


def get_connection():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gopi@123",
            database="python_health_care"
        )

        print("Successfully Connected Database")
        return db

    except mysql.connector.Error as error:
        print("Error in MySQL connection:", error)
        return None


if __name__ == "__main__":
    connection = get_connection()

    if connection:
        connection.close()