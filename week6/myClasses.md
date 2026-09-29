These can have many attributes so they are classes.
Appointment
Practitoner
Patient

WHAT ARE THE OTHERS NOT CLASSES?
Name - This is a piece of data
Status - This is a value assigned to appointment
Cancellation - This feels like it'd be more of a function
Database - not even close to being a class
Clinic - Does not serve a unique function for this purpose

CRC Cards
| Class | Resposibilities | Collaborators |
| Appointment | Know its patient, practitioner as well as time and status | Patient |
| - | Can be cancelled | Practitioner |
| - | Does not allow invalid data | - |
| Practitioner | Know its ID, name and specialty | Appointment |
| - | Has appointments and knows when they are | - |
| - | - | - |
| Patient | Know its ID and name | Appointment |
| - | Has knowledge of its appointment history | - |
