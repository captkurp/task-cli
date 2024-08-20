import json
import time
from pathlib import Path
import sys

# define filepath
dirname = Path(__file__)
filename = Path(dirname.parent, 'task_list.json')

def main():
    #read in input, pass arguements to methods
    if len(sys.argv) < 2:
        print('Usage: task-cli <command> or use task-cli help')
        sys.exit(1)
    
    command = sys.argv[1]

    if command == 'add':
        try:
            task_desc = sys.argv[2]
            add(task_desc)
        except NameError:
            print('Please enter a description inside quotes')

    elif command == 'delete':
        task_desc = sys.argv[2]
        delete(task_num)

    elif command == 'update':
        task_num = sys.argv[2]
        new_desc = sys.argv[3]
        update(task_num, new_desc)
    
    elif command == 'help':
        print('Available commands: "add (description)" "delete (task number)" "update (task number) (new description)" "list (todo, in-progress, done)"')

    elif command == 'list':
        try:
            task_status = sys.argv[2]
            list(task_status)
        except IndexError:
            print('Please choose "all", "todo", "in-progress", or "done"')

    elif command == 'mark_in_progress':
        task_num = sys.argv[2]
        mark_in_progress(task_num)

    elif command == 'mark_done':
        task_num = sys.argv[2]
        mark_done(task_num)

def add(task_desc):
    #add task, the dict id number is generated based on next available number by incrementing in the while loop
    add_time = time.strftime('%m/%d/%Y, %H:%M:%S')
    id_num = 1
    #check if json file already exists, find next available id number and add
    if filename.exists():
        try:
            with open(filename, 'r') as file:
                json_file = json.load(file)
                id_num = 1
                while id_num == json_file.get(f"task{id_num}", {}).get('id'):
                    id_num += 1
                add_dict = {
                    f"task{str(id_num)}": {
                        "id": id_num,
                        "description": task_desc,
                        "time created": add_time,
                        "status": 'todo'
                    }
                }
                json_file.update(add_dict)
            with open(filename, 'w') as file:
                json.dump(json_file, file, indent=4)
        except KeyError:
            print('value error')
    #if json file does not exist, this creates a new file and adds a dict
    else:
        add_dict_new = {
            "task1": {
                "id": 1,
                "description": task_desc,
                "time created": add_time,
                "status": 'todo'
            }
        }
        with open(filename, 'w') as file:
            json.dump(add_dict_new, file, indent=4)

def delete(task_num):
    #delete tasks based on task number
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            del json_file[f'task{task_num}']
        with open(filename, 'w') as file:
            json.dump(json_file, file, indent=4)
    except:
        print('Task not located')

def update(task_num, new_desc):
    #update description of task with a new description, uses dict.update() method
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            json_file[f'task{task_num}'].update({'description': new_desc})
        with open(filename, 'w') as file:
            json.dump(json_file, file, indent=4)
    except:
        print('update error')

def mark_done(task_num):
    #update status of task with a "done" status, uses dict.update() method
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            json_file[f'task{task_num}'].update({'status': 'done'})
        with open(filename, 'w') as file:
            json.dump(json_file, file, indent=4)
    except NameError:
        print('mark done error')

def mark_in_progress(task_num):
    #update status of task with a "in-progress" status, uses dict.update() method
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            json_file[f'task{task_num}'].update({'status': 'in-progress'})
        with open(filename, 'w') as file:
            json.dump(json_file, file, indent=4)
    except NameError:
        print('mark_in_progress error')

def list(task_status):
    #product list of tasks based on task status
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            #prints all tasks, uses while loop and increments id_num to run through every available number, assumes they're consecutive
        if task_status == 'all':
            id_num = 1
            while id_num == json_file.get(f"task{id_num}", {}).get('id'):
                #data is defined based on incrementing id_num variable, relevant dict info is produced using this
                id = json_file.get(f"task{id_num}", {}).get('id')
                description = json_file.get(f"task{id_num}", {}).get('description')
                time_created = json_file.get(f"task{id_num}", {}).get('time created')
                status = json_file.get(f"task{id_num}", {}).get('status')
                print(f'\nTask ID: {id}')
                print(f'Description: {description}')
                print(f'Time created: {time_created}')
                print(f'Status: {status}')
                print('-------------')
                id_num += 1

        elif task_status == 'todo':
            #same incrementing while loop, prints the tasks based on their status being "todo"
            id_num = 1
            while id_num == json_file.get(f"task{id_num}", {}).get('id'):
                id = json_file.get(f"task{id_num}", {}).get('id')
                description = json_file.get(f"task{id_num}", {}).get('description')
                time_created = json_file.get(f"task{id_num}", {}).get('time created')
                status = json_file.get(f"task{id_num}", {}).get('status')
                if json_file.get(f"task{id_num}", {}).get('status') == task_status:
                    print(f'\nTask ID: {id}')
                    print(f'Description: {description}')
                    print(f'Time created: {time_created}')
                    print('-------------')
                    id_num +=1
                else:
                    id_num += 1
                    print(f'No task to do')

        elif task_status == 'in-progress':
            #same incrementing while loop, prints the tasks based on their status being "in-progress"
            id_num = 1
            while id_num == json_file.get(f"task{id_num}", {}).get('id'):
                id = json_file.get(f"task{id_num}", {}).get('id')
                description = json_file.get(f"task{id_num}", {}).get('description')
                time_created = json_file.get(f"task{id_num}", {}).get('time created')
                status = json_file.get(f"task{id_num}", {}).get('status')
                if json_file.get(f"task{id_num}", {}).get('status') == task_status:
                    print(f'\nTask ID: {id}')
                    print(f'Description: {description}')
                    print(f'Time created: {time_created}')
                    print('-------------')
                    id_num +=1
                else:
                    id_num += 1
                    print(f'No pending in-progress tasks')

        elif task_status == 'done':
            #same incrementing while loop, prints the tasks based on their status being "done"
            id_num = 1
            while id_num == json_file.get(f"task{id_num}", {}).get('id'):
                id = json_file.get(f"task{id_num}", {}).get('id')
                description = json_file.get(f"task{id_num}", {}).get('description')
                time_created = json_file.get(f"task{id_num}", {}).get('time created')
                status = json_file.get(f"task{id_num}", {}).get('status')
                if json_file.get(f"task{id_num}", {}).get('status') == task_status:
                    print(f'\nTask ID: {id}')
                    print(f'Description: {description}')
                    print(f'Time created: {time_created}')
                    print('-------------')
                    id_num += 1
                else:
                    id_num += 1
                    print(f'No tasks done')
                    
        else:
            print('No tasks added')     
    except NameError:
        print('error')

if __name__ == "__main__":
    main()