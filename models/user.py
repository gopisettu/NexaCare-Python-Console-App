from abc import ABC, abstractmethod
from datetime import datetime


class User(ABC):

    def __init__(
        self,
        user_id,
        username,
        password,
        role="User"
    ):
        self.user_id = user_id
        self.username = username
        self._password = password
        self.role = role
        self.created_at = datetime.now()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):

        if len(password) < 4:
            raise ValueError(
                "Password must contain at least 4 characters."
            )

        self._password = password

    @abstractmethod
    def display_info(self):
        pass