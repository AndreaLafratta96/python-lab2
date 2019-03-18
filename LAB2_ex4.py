#Tasks
task1 = {'todo': 'call John for AmI project organization', 'urgent': True}
task2 = {'todo': 'buy a new mouse', 'urgent': True}
task3 = {'todo': 'find a present for Angelina’s birthday', 'urgent': False}
task4 = {'todo': 'organize mega party (last week of April)', 'urgent': False}
task5 = {'todo': 'book summer holidays', 'urgent': False}
task6 = {'todo': 'whatsapp Mary for a coffee', 'urgent': False}

#Final list of dictionaries containing all the urgent tasks
final_task_List = []

#List of all tasks: i'm including all the task into a list to interate on each of them
Task_List = []
Task_List.append(task1)
Task_List.append(task2)
Task_List.append(task3)
Task_List.append(task4)
Task_List.append(task5)
Task_List.append(task6)

for task in Task_List:
    if task.get("urgent", True):
        final_task_List.append(task)

print(final_task_List)


