from enum import Enum

from domain.patient import Patient
from domain.practitioner import Practitioner


class appointmentStatus(Enum): #status for appointments
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"

class AppointmentCancelledError(Exception):
    pass #this is called when an appointment has already been cancelled.

class Appointment:
    def __init__ (self, patient, practitioner, time, day,):
        if not isinstance(patient, Patient): #this is so it accepts the object type rather than just a random string
            raise ValueError("An appointment requires a patient") #this seems kind of obvious
        if not isinstance(practitioner, Practitioner):
            raise ValueError("An appointment requires a practitioner to be there") #this too
        if not time:
            raise ValueError("Time is required for an appointment") #date and time are needed
        if not day:
            raise ValueError("Date is required for an appointment")
        self._patient = patient
        self._practitioner = practitioner
        self._time = time
        self._day = day
        self._status = appointmentStatus.SCHEDULED

    def cancel(self): #this function cancels the appointment only if it exists or hasn't been cancelled already
        if self._status != appointmentStatus.SCHEDULED: #check to see if appointment has been sceduled
            raise AppointmentCancelledError("no appointment so no cancellation")
        self._status = appointmentStatus.CANCELLED

    @property
    def patient(self) -> str:
        return self._patient

    @property
    def practitioner(self) -> str:
        return self._practitioner

    @property
    def time(self) -> str:
        return self._time

    @property
    def day(self) -> str:
        return self._day

    @property
    def status(self) -> appointmentStatus:
        return self._status