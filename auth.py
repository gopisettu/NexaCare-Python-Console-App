from getpass import getpass


users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },

    "doctor": {
        "password": "doctor123",
        "role": "doctor"
    },

    "patient": {
        "password": "patient123",
        "role": "patient"
    }
}


def login():

    print("\n========================================")
    print("              LOGIN")
    print("========================================")

    username = input("Username : ")
    password = getpass("Password : ")

    if username not in users:
        print("Username not found.")
        return None, None

    if users[username]["password"] != password:
        print("Invalid password.")
        return None, None

    role = users[username]["role"]

    print("\nLogin successful!")
    print("Welcome,", username)

    return username, role