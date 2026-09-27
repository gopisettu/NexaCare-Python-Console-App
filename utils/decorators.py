from functools import wraps
from datetime import datetime


def log_activity(function):
    """
    Logs when a service function starts and finishes.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(
            f"\n[LOG] {function.__name__} started "
            f"at {datetime.now()}"
        )

        result = function(*args, **kwargs)

        print(
            f"[LOG] {function.__name__} completed"
        )

        return result

    return wrapper


def require_role(required_role):
    """
    Decorator with an argument used to validate a user's role.
    """

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            user = kwargs.get("user")

            if user is None and args:
                for argument in args:
                    if isinstance(argument, dict):
                        user = argument
                        break

            if user is None:
                print("User information is required.")
                return None

            if user.get("role") != required_role:
                print(
                    f"Access denied. "
                    f"{required_role} role required."
                )
                return None

            return function(*args, **kwargs)

        return wrapper

    return decorator