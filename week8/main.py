#this is my demo for the appointment booking system
#gotta import all the other "Things" from the booking system
from domain.patient import Patient
from domain.practitioner import Practitioner
from domain.appointment import AppointmentCancelledError
from persistence.in_memory_repository import InMemoryAppointmentRepository
from services.appointment_service import AppointmentService

#main - when the program runs
def main() -> None:
    service = AppointmentService(InMemoryAppointmentRepository()) #set service as AppointmentService

    patient = Patient("PT022", "John Patient", "2000-01-01", "0400000000") #test patient data
    doctor = Practitioner("P009", "Dr Potato Tomato", "GP", {"Monday": ("09:00", "17:00")}) #test doctor data

    #1st test - a normal booking
    appt = service.book_appointment(patient, doctor, "10:00", "2026-10-12") #test appointment
    print("Booked an appointment for:", appt.patient.name, "with", appt.practitioner.name,
          "-", appt.status.value)

    #2nd test - booking for the same practitioner
    try:
        service.book_appointment(patient, doctor, "10:00", "2026-10-12") #test if its already been booked
    except ValueError as e:
        print("Double booking not permitted:", e)

    #3rd test - cancelling an appointment should work
    service.cancel_appointment(appt) #cancel
    print("Cancel result:", appt.status.value)

    #4th test - should not be cancelled a second time
    try:
        service.cancel_appointment(appt)
    except AppointmentCancelledError as e:
        print("Second cancel result:", e) #can't cancel twice

    #5th test - now the cancelled slot is free again, booking the appointment should work
    service.book_appointment(patient, doctor, "10:00", "2026-10-12")
    print("Slot has now been rebooked. Patient history count:",
          len(service.get_patient_history(patient)))


if __name__ == "__main__":
    main()