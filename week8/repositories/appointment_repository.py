from abc import ABC, abstractmethod #abstract classes that other classes must follow

#you can only create a class that follows this one instead of making one directily
class AppointmentRepository(ABC):
    """Contract for storing and finding appointments.
    Only the methods the current use cases need."""

    #every repository should be able to save an appointment
    @abstractmethod
    def add(self, appointment) -> None:
        pass #placeholder

    #this is to prevent double bookings
    @abstractmethod
    def exists_for(self, practitioner, time: str, day: str) -> bool:
        """Will be true if the practitioner already has a scheduled."""
        pass

    #return the list of patients
    @abstractmethod
    def list_for_patient(self, patient) -> list:
        pass
