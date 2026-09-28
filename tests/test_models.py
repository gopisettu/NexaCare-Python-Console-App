import pytest

from models.user import User


class TestUser:

    def test_password_getter(self, doctor):
        assert doctor.password == "doctor@123"

    def test_password_setter(self, doctor):
        doctor.password = "newpassword"

        assert doctor.password == "newpassword"

    @pytest.mark.parametrize(
        "password",
        ["", "123", "abc"]
    )
    def test_invalid_password(self, doctor, password):

        with pytest.raises(ValueError):
            doctor.password = password


class TestPolymorphism:

    def test_polymorphism(self, doctor, patient):

        users = [doctor, patient]

        results = [
            user.display_info()
            for user in users
        ]

        assert "Dr. Kumar" in results[0]
        assert "Gopi" in results[1]