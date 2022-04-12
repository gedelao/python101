list = {}
task = []

while True:
    option = input("""
 Press 1 to add task 
 Press 2 to delete task 
 Press 3 to view all tasks 
 Press q to quit
 Enter an option: """
     )
    if option == "1":
        task = input("Add task")
        priority = input("Your priority: Easy, Medium or Hard ")
        list[task] = priority
        print(list)
        verification = input("Final decision ")
        if verification == "No" or "no":
            del list[task]
            print(list)
        if verification == "Yes" or "yes":
            print(list)
    elif task == "2":
        print(list)
        task_del = input("Which task do you wish to delete? ")
        del list[task_del]
    elif task == "3":
        print(list)
    elif task == 'q':
        break

# add = int(input("Press 1 to add task: "))
# delete = int(input("Press 2 to delete task: "))
# view_tasks = int(input("Press 3 to view all tasks: "))
# quit_program = input("Press q to quit: ")

# delete task
  # use if statement to print code
  # use the indexing to allow them to select the code they want to delete
  # delete the selected code
  # print the new list of items with the deleted one gone

  # print items
  # print the list of current tasks
  # print them by index
  # loop the user input function

# q for quit function