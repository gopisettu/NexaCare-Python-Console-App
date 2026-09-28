from services.doctor_service import (
    get_all_upcoming_appointments,
    get_all_completed_appointments,
    complete_appointment,
    provide_prescription,
    get_appointment_statistics,
    get_doctor_wise_appointments
)

from utils.decorators import require_role


@require_role("DOCTOR")
def doctor_menu(user):

    while True:

        print("\n========================================")
        print("              DOCTOR MENU")
        print("========================================")

        print("1. View Upcoming Appointments")
        print("2. View Completed Appointments")
        print("3. Complete Appointment")
        print("4. Provide Prescription")
        print("5. Appointment Statistics")
        print("6. Get doctor vise Appointment")
        print("7. Logout")

        choice = input("Enter your choice: ")

        # ---------------------------------
        # 1. Upcoming Appointments
        # ---------------------------------

        if choice == "1":

            print(
                "\n========== UPCOMING APPOINTMENTS =========="
            )

            appointments = get_all_upcoming_appointments(
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
                        "Age:",
                        appointment["age"]
                    )

                    print(
                        "Phone:",
                        appointment["phone"]
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

        # ---------------------------------
        # 2. Completed Appointments
        # ---------------------------------

        elif choice == "2":

            print(
                "\n========== COMPLETED APPOINTMENTS =========="
            )

            appointments = get_all_completed_appointments(
                user["user_id"]
            )

            if not appointments:

                print("No completed appointments.")

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

                    print(
                        "Diagnosis:",
                        appointment["diagnosis"]
                    )

                    print(
                        "Medicine:",
                        appointment["medicine"]
                    )

                    print(
                        "Dosage:",
                        appointment["dosage"]
                    )

                    print(
                        "Duration:",
                        appointment["duration"]
                    )

                    print(
                        "Doctor Notes:",
                        appointment["doctor_notes"]
                    )

        # ---------------------------------
        # 3. Complete Appointment
        # ---------------------------------

        elif choice == "3":

            print(
                "\n========== COMPLETE APPOINTMENT =========="
            )

            try:

                appointment_id = int(
                    input("Enter Appointment ID: ")
                )

                diagnosis = input(
                    "Enter Diagnosis: "
                )

                medicine = input(
                    "Enter Medicine: "
                )

                dosage = input(
                    "Enter Dosage: "
                )

                duration = input(
                    "Enter Duration: "
                )

                doctor_notes = input(
                    "Enter Doctor Notes: "
                )

                success = complete_appointment(
                    appointment_id=appointment_id,
                    user_id=user["user_id"],
                    diagnosis=diagnosis,
                    medicine=medicine,
                    dosage=dosage,
                    duration=duration,
                    doctor_notes=doctor_notes
                )

                if success:

                    print(
                        "\nAppointment completed "
                        "successfully."
                    )

            except ValueError:

                print(
                    "\nAppointment ID must be a number."
                )

        # ---------------------------------
        # 4. Provide Prescription
        # ---------------------------------

        elif choice == "4":

            print(
                "\n========== PROVIDE PRESCRIPTION =========="
            )

            try:

                appointment_id = int(
                    input("Enter Appointment ID: ")
                )

                diagnosis = input(
                    "Enter Diagnosis: "
                )

                medicine = input(
                    "Enter Medicine: "
                )

                dosage = input(
                    "Enter Dosage: "
                )

                duration = input(
                    "Enter Duration: "
                )

                doctor_notes = input(
                    "Enter Doctor Notes: "
                )

                success = provide_prescription(
                    appointment_id=appointment_id,
                    user_id=user["user_id"],
                    diagnosis=diagnosis,
                    medicine=medicine,
                    dosage=dosage,
                    duration=duration,
                    doctor_notes=doctor_notes
                )

                if success:

                    print(
                        "\nPrescription provided "
                        "successfully."
                    )

            except ValueError:

                print(
                    "\nAppointment ID must be a number."
                )

        
        elif choice == "5":

            print("\n========== APPOINTMENT STATISTICS ==========")

            statistics =get_appointment_statistics("BOOKED")

            if statistics is None:
                print("Unable to generate statistics.")

            else:
                print(
                    "Total Appointments:",
                    statistics["total"]
                )

                print("\nAppointments by Status:")

                for status, count in statistics["status_count"].items():
                    print(f"{status}: {count}")

                print("\nAppointments by Doctor:")

                for doctor, count in statistics["doctor_count"].items():
                    print(f"{doctor}: {count}")
        elif choice == "6":

            print(
                "\n========== DOCTOR-WISE APPOINTMENTS =========="
            )

            doctor_data = get_doctor_wise_appointments()

            if not doctor_data:
                print("No appointments found.")

            else:

                for doctor_name, appointments in doctor_data.items():

                    print(f"\nDoctor: {doctor_name}")
                    print("--------------------------------")

                    for appointment in appointments:

                        print(
                            "Appointment ID:",
                            appointment["appointment_id"]
                        )

                        print(
                            "Patient:",
                            appointment["patient_name"]
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

                        print()
                    
        elif choice == "7":

            print(
                "\nDoctor logged out successfully."
            )

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )