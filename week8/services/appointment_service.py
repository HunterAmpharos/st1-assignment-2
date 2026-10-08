from domain.appointment import Appointment
from repositories.appointment_repository import AppointmentRepository


class AppointmentService:
    """Coordinates the booking and cancelling workflows.
    Business rules about an appointment itself stay in the Appointment class."""

    def __init__(self, repository: AppointmentRepository) -> None:
        self._repository = repository

    def book_appointment(self, patient, practitioner, time: str, day: str) -> Appointment:
        #1. check if the appointment has already been booked
        #only service can see all appointments so one appointment can't know about the others
        if self._repository.exists_for(practitioner, time, day):
            raise ValueError("Practitioner already has an appointment at this time")
        #2. if there is not a duplicate then create the appointment.
        #appointment class already does its own validation. line 14
        appointment = Appointment(patient, practitioner, time, day)
        #3. save through the repository
        self._repository.add(appointment)
        #return that appointment that was booked
        return appointment

    #cancel appointment
    def cancel_appointment(self, appointment: Appointment) -> None:
        appointment.cancel()  # the status rule lives in the domain

    #see a list of all patient previous appointments
    def get_patient_history(self, patient) -> list:
        return self._repository.list_for_patient(patient)