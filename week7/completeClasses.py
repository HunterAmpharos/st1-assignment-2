from enum import Enum

class Patient:
    def __init__ (self, patientID: int, name: str, DOB: str, phoneNumber: int):
        if not name or not name.strip():
            raise ValueError("Name field cannot be empty") #needs to have a name
        if not DOB:
            raise ValueError("Date of birth required") #needs to have a date of birth
        if not phoneNumber:
            raise ValueError("Contact details are required") #needs to have contact details
        self._patientID = patientID
        self._name = name.strip() #removes unneccessary characters and spaces
        self._DOB = DOB
        self._phoneNumber = phoneNumber

@property #these property tags allow the variables to be read. the requirments state that these need to be read
#FOR SOME REASON IT WON'T WORK THOUGH
def name(self) -> str:
    return self._name

@property
def DOB(self) -> str:
    return self._DOB

@property
def phoneNumber(self) -> int:
    return self._phoneNumber

class Practitioner:
    def __init__ (self, practitionerID, name, specialty, hours):
        if not name or not name.strip():
            raise ValueError("Name field cannot be empty") #needs to have a name
        if not specialty:
            raise ValueError("Practitioner must have a specialty")
        self._practitionerID = practitionerID
        self._name = name
        self._specialty = specialty
        self._hours = dict(hours) #using a dictonary because hours is a complicated variable   

@property
def name(self) -> str:
    return self._name

@property
def specialty(self) -> int:
    return self._specialty

@property
def specialty(self) -> int:
    return (dict(self._hours)) #we need a specific format for hours

class appointmentStatus(Enum):
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

class Staff:
    def __init__ (self, staffID, name):
        if not name:
                    raise ValueError("Name field cannot be empty") #needs to have a name
        self._staffID = staffID
        self._name = name

@property
def name(self) -> str:
    return self._name


#my test objects
patient = Patient(1001, "  John Wabungus ", "01-12-1998", "0434 200 400")
doctor = Practitioner(2001, "Dr Happy Birthday", "GP", {"Tuesday": ("09:00", "17:00")})
appt = Appointment(patient, doctor, "10:00", "25-05-2004")
print("Created:", patient._name, "/", doctor._name, "/", appt._status.value)
 