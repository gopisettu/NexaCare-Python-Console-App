import pytest

from utils.appointment_iterator import AppointmentIterator


def test_appointment_iterator(appointment):

    iterator = AppointmentIterator(
        [appointment]
    )

    result = next(iterator)

    assert result == appointment

    with pytest.raises(StopIteration):
        next(iterator)