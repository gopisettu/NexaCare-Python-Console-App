def test_appointment_creation(appointment):

    assert appointment.appointment_id == 1
    assert appointment.status == "BOOKED"
    assert appointment.reason == "Chest pain"