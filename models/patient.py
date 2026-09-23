from models.user import User


class Patient(User):

    def __init__(
        self,
        user_id,
        username,
        password,
        name,
        age,
        phone,
        role="Patient"
    ):
        super().__init__(
            user_id,
            username,
            password,
            role
        )

        self.name = name
        self.age = age
        self.phone = phone

    def display_info(self):
        return (
            f"Patient ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Phone: {self.phone}"
        )