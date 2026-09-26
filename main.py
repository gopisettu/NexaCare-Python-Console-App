from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from services.auth_service import register_user ,login_user
from menus.admin_menu import admin_menu
from menus.patient_menu import patient_menu
from menus.doctor_menu import doctor_menu


def register():

    print("\n========================================")
    print("              REGISTRATION")
    print("========================================")

    print("1. Register as Patient")
    print("2. Register as Doctor")
    print("3. Back")

    choice = input("Enter the Choice: ")

    if choice == "3":
        return

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if choice == "1":

        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        phone = input("Enter Phone: ")

        user_id = register_user(
            username,
            password,
            "PATIENT",
            name,
            age,
            phone
        )

        if user_id:
            print("Patient Registered Successfully!")
            print("User ID:", user_id)

    elif choice == "2":

        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")

        user_id = register_user(
            username,
            password,
            "DOCTOR",
            name,
            specialization=specialization
        )

        if user_id:
            print("Doctor Registered Successfully!")
            print("User ID:", user_id)

    else:
        print("Invalid Choice.")

def login():
    print("\n Login")
    username=input("Enter username : ")
    password=input("Enter password : ")
    user=login_user(username,password)
    
    if user is None:
        print("Invalid username or password ")
    print("\nLogin Successfull")
    print("Welcome ,",user["username"])
    print("Role ,",user["role"])
    
    if user["role"]=="ADMIN":
        admin_menu()
    elif user["role"]=="PATIENT":
        patient_menu()
    elif user["role"]=="DOCTOR":
        doctor_menu()
    else:
        print("Invalid user role.")

def main():

    while True:

        print("\n========================================")
        print("           NEXACARE MINI")
        print("      Hospital Management System")
        print("========================================")

        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            print("\nLogin Selected")
            login()

        elif choice == "2":
            print("\nRegister Selected")
            register()

        elif choice == "3":
            print("\nThank you for using NexaCare")
            break

        else:
            print("Invalid Choice, try again.")


if __name__ == "__main__":
    main()
