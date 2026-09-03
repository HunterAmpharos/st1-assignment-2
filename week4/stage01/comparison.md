# Easy to Understand?
Human Version:
This version has two cleary outlined functions that are easy to understand. They have variable names that clearly identify what that variable is storing, such as "patient" and "time". The logic is very simple an easy to understand just by looking at it without comments.
AI Version:
This version has way too many functions for the task it needs to complete. It is not as easy to understand as the human made version. It uses "self." to save variables to the object itself instead of saving it to a dictonary. Using names like a1 and a2 are very unclear and don't make any sense without context.
# Runs Successfully?
Human Version:
Runs great and functions as it should.
AI Version:
Also runs great and does not throw any errors.
# Uses Only Required Features?
Human Version:
This version includes a list, dictonary and simple functions. (what was needed)
AI Version:
This version uses classes and a manager object for a task that was honestly pretty simple.
# Adds Assumptions?
Human Version:
It assumes that the patient name should not be an empty variable. However it does not check for anything else. Something like an impossible time or even bookings be duplicated would just work and cause issues.
AI Version:
The AI version assumes that the appointments should be stored as objects instead of in a dictonary. It also ended up assuming that a manager is needed to book records in the system.
# Handles Errors?
Human Version:
It only handles the one error mentioned earlier. A patient name should not be an empty variable. It does not do anything else to handle errors however.
AI Version:
Does NO error handling!
# Could I Explain It?
Human Version:
I understand that when the function is run to create a booking, it looks for 3 variables. Once it has recieved these 3 variables it creates a list and adds it to the dictonary. Once this dictonary is called back on, it displays! (or it will throw an error because patient name is empty)
AI Version:
I am gonna be honest, I am way more confused here. I think what happens is it also gets 3 variables from the user for the appointment function (__init__). It has some other functions and then it adds these objects to a list. (very confusing to be honest)