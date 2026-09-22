from auth import login
from admin import admin_menu
from doctor import doctor_menu
from patient import patient_menu


def main():

    while True:

        username, role = login()

        if username is None:
            continue

        if role == "admin":
            admin_menu(username)

        elif role == "doctor":
            doctor_menu(username)

        elif role == "patient":
            patient_menu(username)

        print("\n1. Login Again")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "2":
            print("Thank you for using NexaCare.")
            break


if __name__ == "__main__":
    main()