# Function to display tasks from a specific list (pending or completed)
def display_tasks(task_list, title):
    if len(task_list) == 0:
        print(f'There are no {title.lower()}.')
    else:
        print(f'\n{title:-^30}')
        for i, task in enumerate(task_list, start=1):
            print(f'{i}. {task}')


# Function for validating numeric input
def validate_numeric_input(message, limit):
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) <= limit:
            return int(choice)
        else:
            print("Invalid input. Please try again.")


# Function to pause the program
def pause():
    input('Press Enter to continue...')


# Task lists
pending_tasks = ['Fight', 'Go to the gym']
completed_tasks = ['College assignment', 'Make coffee']

while True:
    print(f'\n{" MENU ":-^30}')
    print('''1. Add task
2. Remove task
3. List tasks
4. Mark task as completed
5. Display completed tasks
6. Exit''')

    user_choice = validate_numeric_input('Choose an option: ', 6)

    if user_choice == 1:
        new_task = input('\nEnter new task: ')
        pending_tasks.append(new_task)
        print('Task added successfully!')
        pause()

    elif user_choice == 2:
        if pending_tasks:
            display_tasks(pending_tasks, ' Your tasks ')
            task_to_remove = validate_numeric_input('Enter the number of the task to remove: ', len(pending_tasks))
            removed_task = pending_tasks.pop(task_to_remove - 1)
            print(f'Task "{removed_task}" removed successfully!')
        else:
            print('You have no pending tasks.')
        pause()

    elif user_choice == 3:
        display_tasks(pending_tasks, ' Your tasks ')
        pause()

    elif user_choice == 4:
        if pending_tasks:
            display_tasks(pending_tasks, ' Your tasks ')
            task_to_complete = validate_numeric_input('Enter the number of the task to mark as completed: ',
                                                      len(pending_tasks))
            completed_task = pending_tasks.pop(task_to_complete - 1)
            completed_tasks.append(completed_task)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('You have no pending tasks.')
        pause()

    elif user_choice == 5:
        display_tasks(completed_tasks, ' Completed tasks ')
        pause()

    elif user_choice == 6:
        print('Exiting the program...')
        break
