from enum import Enum

class Patient:
    def __init__ (self, patientID: str, name: str, DOB: str, phoneNumber: int):
        if not patientID or not patientID.strip(): #removes unneccessary characters and spaces
            raise ValueError("Each patient needs an ID")
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

    @property
    def patientID(self) -> str:
        return self._patientID

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