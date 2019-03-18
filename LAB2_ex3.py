from sys import argv

#Assigning to first the first parameter from command line
script, filename = argv

#Printing the parameter
#print("The parameter is:", filename)

#Opening file
txt=open(filename, 'r')

#Checking file content
#print(txt.read())

#Create an empty task list
Task_List = []
Toremove_List = []

choice=0

#Copyng each line of file into the List without newline character, with method .strip()
for task in txt:
    Task_List.append(task.strip())

txt.close()

print("Printing the list: ")
print(Task_List)
print("\n")

beginning = """Insert the number corresponding to the action you want to perform:
    1. insert a new task from file "task_list.txt";
    2. remove a task containing a specified substring;
    3. show all the tasks;
    4. close the program.
    Your choice: """

#Select an option
while choice != 4:
    print(beginning)
    choice=int(input())
    if choice == 1:
        print("Insert a new task: ")
        new_task = input()
        Task_List.append(new_task)
    elif choice == 2:
        print("Insert a a string to be checked as a substring of a task to remove: ")
        substring = input()
        for task in Task_List:
            if substring in task:
                Task_List.remove(task)

    elif choice == 3:
        print("Printing the whole list in alphabetic order: ")
        sorted(Task_List)
        print(Task_List)
    else:
        print("Program ending, file being updated to the the list content...")
        txt=open(filename, 'w')
        #Writing each string of the list into the file
        txt.writelines(["%s\n" % task  for task in Task_List])
        txt.close()
        txt=open(filename, 'r')
        print(txt.read())
        txt.close()
