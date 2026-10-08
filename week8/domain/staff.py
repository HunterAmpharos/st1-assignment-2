class Staff: # i haven't really done much with this lol
    def __init__ (self, staffID, name):
        if not staffID or not staffID.strip():
            raise ValueError("Staff needs an ID")
        if not name:
            raise ValueError("Name field cannot be empty") #needs to have a name
        self._staffID = staffID
        self._name = name

    @property
    def name(self) -> str:
        return self._name