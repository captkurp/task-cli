
master_list = []

menu = '''
    1. Add a Task
    2. View Tasks
    3. Update Tasks
      '''
    
def input_validation(user_input):
    if user_input == '1' or user_input == '2' or user_input == '3' or user_input == '4':
        input_decision_tree(user_input)
    else:
        print('Please select a valid option')
        user_new_input = menu_prompt()
        return input_validation(user_new_input)

def menu_prompt():
    n = 0
    while n == 0:
        print('\n    Please select an option from the menu')
        print(menu)
        user_input = input('>')
        input_validation(user_input)

def input_decision_tree(user_input):
    if user_input == '1':
        print('Please enter a name for the task')
        task_name = input('>')
        print('Please enter a due date for the task')
        task_date = input('>')
        task_creation(task_name, task_date)
        return
    elif user_input == '2':
        print(master_list)
        return
    elif user_input == '3':
        print('to do')
        return
    elif user_input == '4':
        print('close')
    else:
        print('Input not understood, please try again')
        menu_prompt()

def task_creation(task_name, task_date):
    for index in master_list:
        master_list[index] = [task_name, task_date]

print('''
    Welcome to the Python to-do list, please enter the number next to a command a command:
      ''')
menu_prompt()
