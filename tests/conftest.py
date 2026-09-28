import pytest

from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment


@pytest.fixture
def doctor():
    return Doctor(
        1,
        "doctor",
        "doctor@123",
        "Dr. Kumar",
        "Cardiology"
    )


@pytest.fixture
def patient():
    return Patient(
        1,
        "patient",
        "patient@123",
        "Gopi",
        25,
        "9876543210"
    )


@pytest.fixture
def appointment(patient, doctor):
    return Appointment(
        1,
        patient,
        doctor,
        "2026-09-28",
        "Chest pain",
        "BOOKED"
    )