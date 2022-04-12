## Coin flip 

# Write a function that will "flip a coin" and print 
# the result. There should be a 50/50 chance of getting
#  heads or tails.

import random

token = input("Flip a coin: ")
coins = 0

while coins < 1:
    toss = random.randrange(2)
    if token == "yes":
        coins +=1
        print("You flipped Heads")
    elif token == "no":
        print("You flipped Tails")
        coins +=1

# # Even Odd
# # Write a function that when given a number as an input will return true 
# # if the number is odd and false if the number is even. Write a script that 
# # asks the user for a number. Pass the number to the function and then print
# #  a message to the console that informs the user if the number was even or
# #  odd
# import random
# num = int(input("Enter a number: "))

# chance = num % 2
# if chance > 0:
#     print("It's Odd!")
# else:
#     print("It's Even!")


# Dice Roller 
# Write a function that takes two numbers as arguments, then returns a 
# random whole number between those two numbers.
#Write a script that tells the user that we are going to roll the dice but
#  we need to know how many sides they have. Ask them for a 
# number between 2 and 20. Pass the number 1 and the number 
# from the user to the function, then print a message that shows the result

# import random 
# repeat = True 
# while repeat: 
#     Die = str(random.randint(1,6)) 
#     print("Your roll was a " + Die) 
#     if Die == "1" or Die == "3" or Die == "5": 
#         print("You rolled an odd number") 
#     elif Die == "2" or Die == "4" or Die == "6": 
#             print("You rolled an even number") 
#             print("Roll again?") 
#             repeat = "Yes" in input()