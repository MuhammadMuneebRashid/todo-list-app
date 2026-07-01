# Create an empty list to store the tasks
tasks=[] 
# Keep the program running until the user exists
while True:
  # Display the menu
    print("=== To Do List ===")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Exit")
  # Take input from the user    
    choice=int(input("Enter the choice :"))
  # Add a new task    
    if(choice==1):
        task=input("Enter the task :")
        tasks.append(task)
        print("task added successfully")
   # Veiwing the tasks    
    elif(choice==2):
        if(len(tasks))==0:
            print("no tasks available") 
        else:
            print("\n Your tasks")    
            for task in tasks:
                print("-",task)       
   # Removing the task             
    elif(choice==3):
        task=input("Enter the task to remove:")
        if task in tasks:
            tasks.remove(task)
            print("task is removed successfully")
   # Exit the program         
    elif(choice==4):
        print("Good Bye!")
        break
   # Handle invalid input 
    else:
        print("Invalid Choice")                      