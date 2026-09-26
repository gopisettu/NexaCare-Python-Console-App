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
            print("\nAdd Doctor selected.")

        elif choice == "2":
            print("\nAdd Patient selected.")

        elif choice == "3":
            print("\nView All Appointments selected.")

        elif choice == "4":
            print("\nDelete Patient selected.")

        elif choice == "5":
            print("\nAdmin logged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")