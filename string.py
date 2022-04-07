# assignment operator =
# dog = "nelson" #assigning "nelson" to the variables `dog`
# introduction = 'nelson's is nelson' # doesn't work because the string uses single quotes
# # string containing singe quotes needs double quotes
# introduction
# introduction = """nelson's name is "nelson"! """
#characters can be "escaped" using backlash
# introduction - "my dog's name is \"nelson" 
# characters can be "escaped" using backlash

# multi-line-strings
# use triple quotes to use newlines
# long_introduction = """hello

# my dog's name is "nelson\""""

# use escaped newline
# long_introduction = "hellow\n\my dog's name is \"




# new_introduction = "my dog's name is " + dog + " he is awesome!"
# print(new_introduction)
# dog = "toby"
# new_introduction = "my dog's name is " + dog + " he is awesome!"
# print(new_introduction)


# user_details = 'password: helloworld!123'
# print(user_details[4])

#Define two variables: firstname and lastname. 
first_name = "Gerardo"
last_name = "Delao"

#Assign some string values to the variables. 


#You can use your own name or someone else's. 
# Use those two variables to print a greeting that uses the firstname and lastname variables in the output.
print("How's it going " + first_name + " " + last_name)



# Using the two variables you set earlier, generate a company email address that follows the pattern: 
# "first initial, period, last name @ company domain". Assign the result to a new variable called email 
#and print the email to the console.

email = first_name[0] + "." + last_name + "@gmail.com"
print("Email: " + email)

#Username Generator
username = first_name[0:3] + "_" + last_name[0:5]
print("Username: " + username)

#New User Contact Information

contact_card = ("How's it going " + first_name + " " + last_name 
+ "Email: " + email + "Username: " + username)

print(contact_card)