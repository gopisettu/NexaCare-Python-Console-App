class AppointmentIterator:

    def __init__(self, appointments):

        self.appointments = appointments
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= len(self.appointments):

            raise StopIteration

        appointment = self.appointments[self.index]

        self.index += 1

        return appointment