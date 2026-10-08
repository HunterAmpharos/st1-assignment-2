from enum import Enum

class Practitioner:
    def __init__ (self, practitionerID :str, name: str, specialty: str, hours: dict):
        if not practitionerID or not practitionerID.strip():
            raise ValueError("Practitioner needs an ID")
        if not name or not name.strip():
            raise ValueError("Name field cannot be empty") #needs to have a name
        if not specialty:
            raise ValueError("Practitioner must have a specialty")
        self._practitionerID = practitionerID
        self._name = name
        self._specialty = specialty
        self._hours = dict(hours) #using a dictonary because hours is a complicated variable   

    @property
    def practitionerID(self) -> str:
        return self._practitionerID

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> int:
        return self._specialty

    @property
    def specialty(self) -> int:
        return (dict(self._hours)) #we need a specific format for hours