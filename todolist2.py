import time

task_list = []

def show_help() -> None:
    print('\nКоманди')
    print("add Додати завдання")
    print("rm <id> Видалити завдання")
    print("complete <id> Позначити виконаним")
    print("revert <id> Відмінити виконання")
    print("edit <id> Редагувати завдання")
    print("ls Показати всі завдання")
    print("ctrl+c Вийти")

def write_task_list(tasks: list) -> None:
    global task_list

    task_list = tasks

def read_task_list() -> list:
    return task_list

def show_tasks() -> None:
    tasks = read_task_list()
    print(f"ID\tDescription\tStatus")

    if (tasks and len(tasks)):
        for task in tasks:
            print(f"{task['id']}\t{task['text']}\t{task['status']}")
    else:
        print('Використовуйте "add" щоб додати нову задачу')

def add_task() -> None :
    tasks = read_task_list();

    text = input('Опис таски: ')
    task = {
        'text': text,
        'id': str(int(time.time())),
        'status': 'Нова',
    }
    
    tasks.append(task)
    write_task_list(tasks);

    print(f"Таска створена, ID: {task['id']}")

def rm_task(id: str):
    tasks = read_task_list()
    
    new_task_list = [];
    for task in tasks:
        if task['id'] == id:
            continue
        
        new_task_list.append(task)
    
    write_task_list(new_task_list)

def get_task_by_id(id: str):
    tasks = read_task_list()
    
    for task in tasks:
        if (task['id'] == id):
            return task

    return None

def update_task(task_to_update: dict[str, str]) -> None:
    tasks = read_task_list()

    to_update = []
    
    for task in tasks:
        if (task['id'] == task_to_update['id']):
            to_update.append(task_to_update)
        else:
            to_update.append(task)

    write_task_list(to_update)

def update_task_status(id: str, status: str) -> None:
    task = get_task_by_id(id)

    if task:
        task['status'] = status

        update_task(task)
    else:
        print(f'Задача не знайдена по ID: {id}')

def set_complete_task_status(id: str) -> None: 
    update_task_status(id, 'Виконана')

def set_new_task_status(id: str) -> None: 
    update_task_status(id, 'Нова')

def edit_task(id: str): 
    task = get_task_by_id(id)
    
    if task:
        text = input('Новий опис: ')
        task['text'] = text

        update_task(task)
    else:
        print(f'Задача не знайдена по ID: {id}')

show_help()

while True:
    parts = input('Команда: ').split(' ', 1)

    command, *args = parts

    if command == 'ls':
        show_tasks()
    elif command == 'add':
        add_task()
    elif command == 'rm':
        rm_task(args[0])
    elif command == 'complete':
        set_complete_task_status(args[0])
    elif command == 'revert':
        set_new_task_status(args[0])
    elif command == 'edit':
        edit_task(args[0])
    elif command == 'help':
        show_help()
