# # phonebook_dict = {
# #   'Alice': '703-493-1834',
# #   'Bob': '857-384-1234',
# #   'Elizabeth': '484-584-2923'
# # }

# # ## Print Elizabeth's phone number.
# # phonebook_dict["Elizabeth"]

# # ## Add an entry to the dictionary: Kareem's number is 938-489-1234
# # phonebook_dict["Kareem"] = "968-345-2345"

# # ## Delete Alice's phone entry

# # del phonebook_dict["Alice"]

# # ## Change Bob's phone number to '968-345-2345'.

# # phonebook_dict["Bob"] = "968-345-2345"

# # ## Print all the phone entries (try to find a solution using a loop)
# # for number in phonebook_dict:
# #     print(number,phonebook_dict[number])
# # ##
# # ##

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
#     { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
#   ]
# }

# # ## Write a python expression that gets the email address of Ramit.

# # print(ramit["email"])

# # # ## Write a python expression that gets the first of Ramit's interests.

# print(ramit["interests"][0])

# # # ## Write a python expression that gets the email address of Jasmine.

# print(ramit["friends"][0]["email"])

# # ## Write a python expression that gets the second of Jan's two interests.

# # print(ramit["friends"][1]["interests"][1])

# # Letter Histogram

# text = input("Please enter a word: ")

# histogram = {}

# for c in text:
#     if c not in histogram:
#         histogram[c] = 1
#     else:
#         histogram[c] = histogram[c] + 1

# for key, value in histogram.items():
#     print("'%s': %d" % (key, value))

# ####

# user_sentence = input("Please enter a sentence: ").split()
# sent_dict = {}

# for index in user_sentence:
#     if index not in sent_dict:
#         sent_dict[index] = 0
#     sent_dict[index] += 1
#     print(sent_dict)

todo = input(""""
Press 1 to add task
Press 2 to delete task
Press 3 to view all tasks
Press q to quit
Enter an option:  
""").lower()

if todo == 1:
  add_task_input()
elif todo == 2:
  delete_task()
elif todo == 3:
  view_task()
elif todo == "q":
  quit()
else:
  print("Enter a valid option")

## add task

def add_task_input():
  print("Add Task")
  priorities = ["low", "medium", "high"]
  title = input("Enter A task: ")
  priorities_input = {f'Enter a priority for {priorities}.'}
  while priorities_input not in priorities and priorities_input != "m":
    priorities_input = input("You haven't enter a valid property")
    if priorities_input == "m":
      display_menu()
      return
    add_task_input(title_input, priorities_input)
      



