def doctor_menu():

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
            print("\nView Upcoming Appointments selected.")

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