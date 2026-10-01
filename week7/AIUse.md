I asked AI (Copilot) to generate me its idea of an appointment class. This is what i was given.
I decided to take the appointmentstatus class as well as the appointmentcancellederror and I incorporated those into my classes for the complete system.

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

APPROVED UML
Appointment
- patient: Patient
- practitioner: Practitioner
- time / day: (your attributes)
- status: AppointmentStatus
+ cancel()

AppointmentStatus (enum): SCHEDULED, CANCELLED

Relationships:
- Patient 1 to 0..* Appointment
- Practitioner 1 to 0..* Appointment

BUSINESS RULES
- A new appointment starts as SCHEDULED.
- Only a SCHEDULED appointment can be cancelled.
- Cancelling twice must raise a clear custom exception.
- Cancelled appointments remain as objects (history is kept).
- Status must not be changeable from outside the class.

EXISTING CLASSES
class Patient:
    def __init__ (self, patientID, name, DOB, phoneNumber):
        if not name:
            raise ValueError("Name field cannot be empty") #needs to have a name
        if not DOB:
            raise ValueError("Date of birth required") #needs to have a date of birth
        if not phoneNumber:
            raise ValueError("Contact details are required") #needs to have contact details
        self._patientID = patientID
        self._name = name.strip() #removes unneccessary characters and spaces
        self._DOB = DOB
        self._phoneNumber = phoneNumber

class Practitioner:
    def __init__ (self, practitionerID, name, specialty, hours):
        if not name:
            raise ValueError("Name field cannot be empty") #needs to have a name
        if not specialty:
            raise ValueError("Practitioner must have a specialty")
        self._practitionerID = practitionerID
        self._name = name
        self._specialty = specialty
        self._hours = dict(hours) #using a dictonary because hours is a complicated variable

------------------------------------------------------------------------------------------------------------------

from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Optional


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class AppointmentCancelledError(Exception):
    """Raised when attempting to cancel an already cancelled appointment."""
    pass


class Appointment:
    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        time: datetime,
    ) -> None:
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient instance")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner instance")
        if not isinstance(time, datetime):
            raise TypeError("time must be a datetime object")

        self._patient: Patient = patient
        self._practitioner: Practitioner = practitioner
        self._time: datetime = time
        self._status: AppointmentStatus = AppointmentStatus.SCHEDULED

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def time(self) -> datetime:
        return self._time

    @property
    def status(self) -> AppointmentStatus:
        """Read-only access to status; cannot be modified externally."""
        return self._status

    def cancel(self) -> None:
        """Cancels the appointment if it is currently scheduled."""
        if self._status == AppointmentStatus.CANCELLED:
            raise AppointmentCancelledError("Appointment has already been cancelled.")
        self._status = AppointmentStatus.CANCELLED

    def __repr__(self) -> str:
        return (
            f"Appointment(patient={self._patient._name}, "
            f"practitioner={self._practitioner._name}, "
            f"time={self._time}, status={self._status.value})"
        )
