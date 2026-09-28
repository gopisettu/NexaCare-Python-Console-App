import pytest

from services.patient_service import (
    search_doctor_by_specialization
)

from exceptions.exception import DoctorNotFoundError


class TestDoctorSearch:

    @pytest.mark.parametrize(
        "specialization",
        ["123", "@Cardiology", "Cardiology123"]
    )
    def test_invalid_specialization(
        self,
        specialization
    ):

        with pytest.raises(ValueError):
            search_doctor_by_specialization(
                specialization
            )

    def test_doctor_not_found(self):

        with pytest.raises(DoctorNotFoundError):
            search_doctor_by_specialization(
                "UnknownSpecialization"
            )