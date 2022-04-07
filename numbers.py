#Write functions that accept two parameters, a and b, that print the result for each to the console

#add - print the result of a + b
#a = 5
#b = 5
#print(a + b)
#subtract - print the result of a - b
#a = 3
#b = 2
#print(a - b)
#multiply - print the result of a * b
#a = 7
#b = 2
#print(a * b)
#divide - print the result of a / b
#a = 10
#b = 2
#print(a / b)

#Call each one of your functions to make sure they work correctly.


#You need to calculate how many pancakes to make for a large conference breakfast. 
# Write a function that accepts two parameters: number of guests, number of pancakes per guest. 
# The calculation for the total number of pancakes should be 12% higher 
# than the number of guests multiplied by the number of pancakes per guest, 
# rounded up to the nearest whole number. Print the result to the console.
#Call your function to make sure it is working correctly. For example, 10 guests with 3 pancakes each = 34 pancakes total

#number_of_pancakes = round(1.12 * 10 * 3)

#print(number_of_pancakes)

number_of_guests =int(input("How many guests will be attending?"))
number_of_pancakes = int(input("How man pancakes per guest"))
return math.ceil(space_divider + (12 * number_of_guests * number_of_pancakes))
    import math
def calculator(guests, pancakes):
        total =calculator(number_of_guests, number_of_pancakes)



#Write a function called fahrenheitToCelsius that accepts a parameter for the temperature. 
#Convert the temperature from celsius to fahrenheit and print the result. 
# Do the opposite conversion in a function called celsiusToFahrenheit.

#def celsius
#fahrenheit_to_celsius = temperature