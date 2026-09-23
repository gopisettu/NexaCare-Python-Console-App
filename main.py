from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment


doctor = Doctor(
    1,
    "ravi",
    "1234",
    "Ravi",
    "Cardiology"
)

patient = Patient(
    2,
    "arun",
    "1234",
    "Arun",
    25,
    "9876543210"
)

appointment = Appointment(
    1,
    patient,
    doctor,
    "25-09-2026",
    "Fever"
)


print("===== DOCTOR =====")
print(doctor.display_info())

print("\n===== PATIENT =====")
print(patient.display_info())

print("\n===== APPOINTMENT =====")
print(appointment.display_info())