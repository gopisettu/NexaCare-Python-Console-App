from services.admin_service import (
    add_doctor,
    add_patient,
    get_all_appointments,
    delete_patient
    # get_appointment_statistics,
    # get_doctor_appointments,
    # export_patient_details
)
def admin_menu():

    while True:

        print("\n========================================")
        print("              ADMIN MENU")
        print("========================================")

        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. View All Appointments")
        print("4. Delete Patient")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n========== ADD DOCTOR ==========")

            username = input("Enter username: ")
            password = input("Enter password: ")
            name = input("Enter doctor name: ")
            specialization = input(
                "Enter specialization: "
            )

            user_id = add_doctor(
                username=username,
                password=password,
                name=name,
                specialization=specialization
            )

            if user_id:
                print("\nDoctor added successfully.")
                print("User ID:", user_id)

        elif choice == "2":

            print("\n========== ADD PATIENT ==========")

            username = input("Enter username: ")
            password = input("Enter password: ")
            name = input("Enter patient name: ")

            age = int(
                input("Enter age: ")
            )

            phone = input("Enter phone number: ")

            user_id = add_patient(
                username=username,
                password=password,
                name=name,
                age=age,
                phone=phone
            )

            if user_id:
                print("\nPatient added successfully.")
                print("User ID:", user_id)

        elif choice == "3":

            print("\n========== ALL APPOINTMENTS ==========")

            appointments = get_all_appointments()

            if not appointments:
                print("No appointments found.")

            else:
                for appointment in appointments:

                    print("\n------------------------------")

                    print(
                        "Appointment ID:",
                        appointment["appointment_id"]
                    )

                    print(
                        "Patient:",
                        appointment["patient_name"]
                    )

                    print(
                        "Doctor:",
                        appointment["doctor_name"]
                    )

                    print(
                        "Specialization:",
                        appointment["specialization"]
                    )

                    print(
                        "Date:",
                        appointment["appointment_date"]
                    )

                    print(
                        "Reason:",
                        appointment["reason"]
                    )

                    print(
                        "Status:",
                        appointment["status"]
                    )

                    if appointment["diagnosis"]:
                        print(
                            "Diagnosis:",
                            appointment["diagnosis"]
                        )

                    if appointment["medicine"]:
                        print(
                            "Medicine:",
                            appointment["medicine"]
                        )

        elif choice == "4":

            print("\n========== DELETE PATIENT ==========")

            patient_id = int(
                input("Enter patient ID: ")
            )

            deleted = delete_patient(patient_id)

            if deleted:
                print(
                    "\nPatient deleted successfully."
                )

        elif choice == "5":

            print("\nAdmin logged out successfully.")
            break

        else:

            print("\nInvalid choice. Please try again.")