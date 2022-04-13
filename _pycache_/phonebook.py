# # If they choose to look up an entry, you will ask them 
# # for the person's name, and then look up the person's phone number 
# # by the given name and print it to the screen.
# # If they choose to set an entry, you will prompt 
# # them for the person's name and the person's phone number,
# # If they choose to delete an entry, you will prompt them
# #  for the person's name and delete the given person's entry.
# # If they choose to list all entries, you will go 
# # through all entries in the dictionary and print 
# # each out to the terminal.
# # If they choose to quit, end the program.

# phonebookApp: It's where we will start 


# Examples

# $ python3 phonebook.py

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# What do you want to do (1-5)? 2

# Name: Melissa
# Phone Number: 584-394-5857
# Entry stored for Melissa.

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 2

# Name: Igor
# Phone Number: 857-485-2935
# Entry stored for Igor.

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 2

# Name: Jazz
# Phone Number: 334-584-2345
# Entry stored for Jazz.

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# What do you want to do (1-5)? 1

# Name: Melissa
# Found entry for Melissa: 584-394-5857

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 3

# Name: Melissa
# Deleted entry for Melissa

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 4

# Found entry for Igor: 857-485-2935
# Found entry for Jazz: 334-584-2345

# Electronic Phone Book =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
#  What do you want to do (1-5)? 5

# Bye.


def print_menu():
    print('''
    Electronic Phone Book 
    =====================
    1. List all entry
    2. Set an entry
    3. Delete an entry
    4. List up an entry
    5. Quit
    ''')

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("What do you want to do (1-5)?: ")) #### Menu
    if menu_choice == 1: ### list all entry
        print("Phone Numbers:")
        for i in numbers.keys():
            print("Name: ", i, "\t Number: ", numbers[i])
        print()
    elif menu_choice == 2:   ### set an entry
        print("Add Name and Number ")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:         ##### Removes entries
        print("Remove Name and Number ")
        name = input("Delete entry for: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found ")
    elif menu_choice == 4: #### look up numbers
        print("Lookup number by name ")
        name = input("Name: ")
        if name in numbers:
            print("Found entry for", name + ":" + " "+ numbers[name], )
        else:
            print(name, "was not found")
    elif menu_choice == 5: ### exit
        print_menu()



