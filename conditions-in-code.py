day = input("What day of the week is it?: ")

#day_lower = day.lower()

#if day_lower == "monday" or "tuesday" or "wednesday" or "thursday" or "friday":
    #print("Go to work!")
#elif day_lower == "saturday" or "sunday":
    #print("It's a lazy day")
#else:
#   print("It's a lazy day")

   
#Secret Password

#password = input("password required: ")
#backup = True

#if password == "#" and backup:
   #print("Welcome!")

#else:
    #print("Try Again!")

#Write a script that asks the user for a password. If the user enters 
# the correct word (pick one yourself) then print 'Welcome!', otherwise print 'Try Again!'
 
# Day of week

day_of_week = int(input("Pick a number between 1-7"))
if (
    day_of_week == 1 or "sunday"
    or day_of_week == 2 or "monday"
    or day_of_week == 3  or "tuesday"
    or day_of_week == 4  or "wednesday"
    or day_of_week == 5   or "thursday"
    or day_of_week == 6  or "friday"
    or day_of_week == 7  or "saturday"
):
    print("Good Job")

elif day_of_week > 7:
    print("Error") 
    


