tasks = [] # create an array 

def addTask(): # define the addTask function. This will let the user add a task
    task = input("Please enter a task: ") # asks the user for their task
    tasks.append(task) # this will add the task to the list 
    print(f"Task '{task}' was added to the list!") # notify the user of task being added

def listTasks(): # define the listTasks function. This will list the tasks to the user
    if not tasks: # IF statement based on if the list is empty or not
        print("The task list is currently empty.") # this will display if the list is empty
    else: # ELSE statment, this will show if the list has items in it 
        print("Current Tasks:") # this will display alongside the tasks, makes it look btetter for the user
        for index, task in enumerate(tasks, start=1):  # Start index at 1
            print(f"Task #{index}. {task}") # print the tasks by using their indexes

def deleteTask(): # define the deleteTask function. This will allow users to delete items from their task list
    listTasks() # calls the listTracks function because we meed the information from i
    try:
        taskToDelete = int(input("Please enter the number of the task you wish to delete: ")) # get's the users input
        taskIndex = taskToDelete - 1  # This will take one away from the list, aka, deleting one item

        if 0 <= taskIndex < len(tasks):
            removed_task = tasks.pop(taskIndex)
            print(f"Task '{removed_task}' (#{taskToDelete}) was deleted successfully!") # shows the user that the iten has been deleted
        else: 
            print(f"Task #{taskToDelete} was not found, please try again.") # this will show if the users task couldn't be found. in this case, the number is either too big or too small

    except ValueError:
        print("What you have entered is invalid, please try again.") # similar to the last comment. another error message.

while True: # this will always start in the program because it is running while True
    print("\nWelcome to my simple to-do-list app!")  # Menu system
    print("Here are your options:")
    print("-------------------------")
    print("1: Add an item to your list")
    print("2: Delete an item from your list")
    print("3: View your list of tasks")
    print("4: Quit the application")
    
    choice = input("What will your choice be?:   ") # get's the users menu choice with If statements

    if choice == "1": 
        addTask() # for each of these, we will make a call to the function that aligns wuth the menu choice
    elif choice == "2":
        deleteTask()
    elif choice == "3":
        listTasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("ERROR, this isn't a valid option. Please pick 1, 2, 3, or 4.") # error for if the number isn't 1,2,3 or 4
