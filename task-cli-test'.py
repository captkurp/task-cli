import json
import time
from pathlib import Path

## NOTE -- TEXT IS NOT ENCODING TO JSON CORRECTLY

dirname = Path(__file__)
filename = Path(dirname.parent, 'task_list.json')

def main():
    '''
    if len(sys.argv) < 2:
        print('Usage: task-cli <command> or use task-cli help')
        sys.exit(1)
    
    command = sys.argv[1]
    remove when finished '''

    command = 'add'
    ##command2 = 2
    ##command3 = 'updated task'

    if command == 'add':
        try:
            task_desc = command2
            ##task_desc = sys.argv[2]
            add(task_desc)
        except NameError:
            print('Please enter a description')

    elif command == 'delete':
        task_num = command2
        ##task_desc = sys.argv[2]
        delete(task_num)

    elif command == 'update':
        task_num = command2
        new_desc = command3
        ##task_num = sys.argv[2]
        ##new_desc = sys.argv[3]
        update(task_num, new_desc)
    
    elif command == 'help':
        print('Available commands: "add (description)" "delete (task number)" "update (task number) (new description)')
        print('')

    elif command == 'list':
        print('to do - list done todo in-progress')
        task_status = command2
        list(task_status)

    elif command == 'mark_in-progress':
        print('to do')

    elif command == 'mark_done':
        print('to do')

def add(task_desc):
    add_time = time.strftime('%m/%d/%Y, %H:%M:%S')
    id_num = 1
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
            pass
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
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            del json_file[f'task{task_num}']
        with open(filename, 'w') as file:
            json.dump(json_file, file, indent=4)
    except:
        print('Task not located')

def update(task_num, new_desc):
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            json_file[f'task{task_num}'].update({'description': new_desc})
        with open(filename, 'w') as file:
            json.dump(json_file, file, indent=4)
    except:
        print('update error')


def help():
    print('to do')

def mark_done(task_num):
    print('to do')

def mark_in_progress(task_num):
    print('to do')

def list(task_status):
    print('to do')
    
if __name__ == "__main__":
    main()