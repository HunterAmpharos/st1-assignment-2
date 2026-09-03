If I could improve one thing, I think I'd first start by making sure we are checking that there are no double bookings.
for appt in appointments:
    if appt["practitioner"] == practitioner_name and appt["time"] == appointment_time:
        raise ValueError("There is already a booking that exists with the practitioner and time")
Something similar to that I am sure would work.

I am really unsure what I was meant to do here? I mean it says to write our own code and then in the lab student handout it gives us the code? So I had no idea if I was meant to be writing something. So I am sorry if I got this wrong.

Before I used the AI I compiled some code that was meant to be the booking systemf or a smartcare system. This system let you add bookings to a dictonary. I think the AI probably helped me to understand the difference between lists and dictonaries. The AI did make a lot of assumptions, it assumed things even when not prompted to add certain features, such as using classes in its design. Well to test it I just added another appointment to the list. Really not sure if that was how I was meant to test it. 