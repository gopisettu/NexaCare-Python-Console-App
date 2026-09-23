from models.user import User


class Doctor(User):

    def __init__(
        self,
        user_id,
        username,
        password,
        name,
        specialization,
        role="Doctor"
    ):
        super().__init__(
            user_id,
            username,
            password,
            role
        )

        self.name = name
        self.specialization = specialization

    def display_info(self):
        return (
            f"Doctor ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Specialization: {self.specialization}"
        )