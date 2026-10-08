from domain.appointment import appointmentStatus
from repositories.appointment_repository import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
    #meaning it will disapear when the program stops.

    #this runs as soon as the repository is created.
    #there will be an empty list at the start but it will fill up as more appointments are added
    def __init__(self) -> None:
        self._appointments = [] #private

    #adds the appointment to the end of the list.
    def add(self, appointment) -> None:
        self._appointments.append(appointment)

    #has this appointment already been added to the list?
    #will check every appointment already stored in the list
    def exists_for(self, practitioner, time: str, day: str) -> bool:
        for a in self._appointments: #a is appointment
            if (a.practitioner.practitionerID == practitioner.practitionerID #if they are the same
                    and a.time == time and a.day == day
                    and a.status == appointmentStatus.SCHEDULED):
                return True #yes this is a duplicate, stop looking
        return False #no, no duplicate

    def list_for_patient(self, patient) -> list:
        return [a for a in self._appointments
                if a.patient.patientID == patient.patientID]