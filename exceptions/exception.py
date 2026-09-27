class DoctorNotFoundError(Exception):
    """Raised when a doctor cannot be found."""


class AppointmentNotFoundError(Exception):
    """Raised when an appointment cannot be found."""


class AppointmentAlreadyCompletedError(Exception):
    """Raised when a completed appointment is modified incorrectly."""