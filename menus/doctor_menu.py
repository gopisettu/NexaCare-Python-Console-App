from services.doctor_service import get_all_upcommingAppointments


def doctor_menu(user):

    while True:

        print("\n========================================")
        print("              DOCTOR MENU")
        print("========================================")

        print("1. View Upcoming Appointments")
        print("2. View Completed Appointments")
        print("3. Complete Appointment")
        print("4. Provide Prescription")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n========== UPCOMING APPOINTMENTS ==========")

            appointments = get_all_upcommingAppointments(
                user["user_id"]
            )

            if not appointments:

                print("No upcoming appointments.")

            else:

                for appointment in appointments:

                    print("\n-----------------------------")

                    print(
                        "Appointment ID:",
                        appointment["appointment_id"]
                    )

                    print(
                        "Patient:",
                        appointment["patient_name"]
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

        elif choice == "2":

            print("\nView Completed Appointments selected.")

        elif choice == "3":

            print("\nComplete Appointment selected.")

        elif choice == "4":

            print("\nProvide Prescription selected.")

        elif choice == "5":

            print("\nDoctor logged out successfully.")
            break

        else:

            print("\nInvalid choice. Please try again.")