from exceptions.exception import DoctorNotFoundException
from services.patient_service import (
    get_all_doctors,
    search_doctor_by_specialization,
    book_appointment,
    view_my_appointments
)


def patient_menu(user):

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

            print("\n========== ALL DOCTORS ==========")

            doctors = get_all_doctors()

            if not doctors:

                print("No doctors found.")

            else:

                for doctor in doctors:

                    print("\n------------------------------")

                    print(
                        "Doctor ID:",
                        doctor["doctor_id"]
                    )

                    print(
                        "Name:",
                        doctor["name"]
                    )

                    print(
                        "Specialization:",
                        doctor["specialization"]
                    )

        elif choice == "2":

            print("\n========== SEARCH DOCTOR ==========")

            specialization = input(
                "Enter specialization: "
            ).strip()

            try:

                doctors = search_doctor_by_specialization(
                    specialization=specialization
                )

                for doctor in doctors:

                    print("\n------------------------------")

                    print(
                        "Doctor ID:",
                        doctor["doctor_id"])

                    print(
                        "Name:",
                        doctor["name"]
                    )

                    print(
                        "Specialization:",
                        doctor["specialization"]
                    )

            except DoctorNotFoundError as error:

                print(error)

            except ValueError as error:

                print("Invalid input:", error)

        elif choice == "3":

            print("\n========== BOOK APPOINTMENT ==========")

            doctor_id = int(
        input("Enter doctor ID: ")
    )

            appointment_date = input(
        "Enter appointment date (YYYY-MM-DD): "
    )

            reason = input(
        "Enter reason for appointment: "
    )

            success = book_appointment(
        user_id=user["user_id"],
        doctor_id=doctor_id,
        appointment_date=appointment_date,
        reason=reason
    )

            if success:

               print("\nAppointment booked successfully.")

        elif choice == "4":

              print("\nView My Appointments selected.")
              view_my_appointments(user["user_id"])
              

        elif choice == "5":

            print("\nView My Prescriptions selected.")

        elif choice == "6":

            print("\nPatient logged out successfully.")

            break

        else:

            print("\nInvalid choice. Please try again.")
