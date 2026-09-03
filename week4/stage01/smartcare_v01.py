# print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# # First Appointment
# patient1_name = 'Alice Smith'
# practitioner1_name = 'Dr. John Doe'
# appointment1_time = '2024-07-20 10:00 AM'
# print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# # Second Appointment
# patient2_name = 'Bob Johnson'
# practitioner2_name = 'Dr. Jane Roe'
# appointment2_time = '2024-07-20 11:30 AM'
# print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# Use lists, dictionaries and functions to enhance the Python file
appointments = []
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

#Limitations
#There is currently no way to add an appointment to the system while it is running.
#You cannot modify appointments that have already been created.
#The system does not check if a time is valid.
#There is no command to check appointments after seeing them initially.
#The variable names for each appointment are not great when there are a lot of appointments in the system.
