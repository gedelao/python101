#MadLib 

madlib1 = input("a noun: ")
madlib2 = input("a present-tense verb: ")
madlib3 = input("a name: ")

def madlib():
    print(f"There once was a {madlib1} that suddenly came to life, called themselves {madlib2} and starting {madlib3} around the town. {name} decided that {verb} was unacceptable and decided to move to the countryside an live a life of solitude.")

madlib()

# Tip Calculator

bill = input("What is the total bill? ")
percent = input("What percentage would you like to tip? ")
total = (float(bill) * (1 + float(percent) / 100))

def percentage_plus(bill, percent):
    return total

def tip_calculator(): 
    print(f"Total bill is ${total:0.2f}.")

tip_calculator()

# Group Tip Calculator

bill = input("What is the total bill? ")
percent = input("What percentage would you like to tip? ")
people = input("How many people are in the group? ")
total = (float(bill) * (1 + float(percent) / 100))
final = total / float(people)

def percentage_plus(bill, percent):
    return total

def group_tip_calculator(): 
    print(f"Total bill is ${total:0.2f}.")
    print(f"Each person should pay ${final:0.2f}.")

group_tip_calculator()
