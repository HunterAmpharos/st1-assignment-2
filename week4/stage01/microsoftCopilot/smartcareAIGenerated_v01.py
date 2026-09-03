#THIS CODE IS GENERATED WITH MICROSOFT COPILOT AND IS *NOT* HUMAN WRITTEN
# Simple appointment system using classes

class Appointment:
    def __init__(self, patient, practitioner, time):
        self.patient = patient
        self.practitioner = practitioner
        self.time = time

    def details(self):
        return f"{self.patient} with {self.practitioner} at {self.time}"


class AppointmentBook:
    def __init__(self):
        self.records = []

    def add(self, appointment):
        self.records.append(appointment)
        print("Appointment stored.")

    def show_all(self):
        if len(self.records) == 0:
            print("No appointments available.")
            return

        print("Appointments:")
        for entry in self.records:
            print("-", entry.details())


# Example usage
book = AppointmentBook()

a1 = Appointment("Liam Brown", "Dr. Carter", "2026-09-10 9:00 AM")
a2 = Appointment("Maya Green", "Dr. Wilson", "2026-09-10 10:15 AM")
a3 = Appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')

book.add(a1)
book.add(a2)
book.add(a3)

book.show_all()