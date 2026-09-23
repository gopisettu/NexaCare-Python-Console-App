from datetime import datetime


class Appointment:

    def __init__(
        self,
        appointment_id,
        patient,
        doctor,
        appointment_date,
        reason,
        status="SCHEDULED"
    ):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.reason = reason
        self.status = status
        self.created_at = datetime.now()

    def display_info(self):
        return (
            f"Appointment ID: {self.appointment_id}\n"
            f"Patient: {self.patient.name}\n"
            f"Doctor: {self.doctor.name}\n"
            f"Date: {self.appointment_date}\n"
            f"Reason: {self.reason}\n"
            f"Status: {self.status}"
        )