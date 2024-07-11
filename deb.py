tasks = []
def addTask():
    task = input("Please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list")
def deleteTask():
    task = input("Enter a task to delete:")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted from the list")
    else:
        print(f"Task '{task}' not found in the list")
def listTask():
    if not tasks:
        print("There are no task currently")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index}. {task}")
if __name__ == "__main__":
    print("Welcome to the to do list app:")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input")
    print("Goodbye")