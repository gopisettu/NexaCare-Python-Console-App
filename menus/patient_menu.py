def patient_menu():

    while True:

        print("\n========================================")
        print("             PATIENT MENU")
        print("========================================")

        print("1. View All Doctors")
        print("2. Search Doctor by Specialization")
        print("3. Book Appointment")
        print("4. View My Appointments")
        print("5. View My Prescriptions")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nView All Doctors selected.")

        elif choice == "2":
            print("\nSearch Doctor selected.")

        elif choice == "3":
            print("\nBook Appointment selected.")

        elif choice == "4":
            print("\nView My Appointments selected.")

        elif choice == "5":
            print("\nView My Prescriptions selected.")

        elif choice == "6":
            print("\nPatient logged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")