import json
import os
import time


def show_help() -> None:
    print('Програма для управління задачами. Принцип роботи - задачі зберігаються в файл data.json що створюється поряд з цим файлом')
    print('Для роботи можна використовувати команди:')
    print("add           Додати завдання")
    print("rm <id>       Видалити завдання")
    print("complete <id> Позначити виконаним")
    print("revert <id>   Відмінити виконання")
    print("edit <id>     Редагувати завдання")
    print("ls            Показати всі завдання")
    print("ctrl+c Вийти")

def write_file(tasks: list) -> None:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def read_file() -> list:
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def show_tasks() -> None:
    tasks = read_file()
    print(f"Ідентифікатор\tЗавдання\tСтатус")

    if (tasks and len(tasks)):
        for task in tasks:
            print(f"{task['id']}\t{task['text']}\t{task['status']}")
    else:
        print('Задач немає. Використовуйте "add" щоб додати нову задачу')

def add_task() -> None :
    tasks = read_file();

    text = input('Що потрібно зробити?')
    task = {
        'text': text,
        'id': str(int(time.time())),
        'status': 'Нова',
    }
    
    tasks.append(task)
    write_file(tasks);

    print(f"Задача створена, ID: {task['id']}")

def rm_task(id: str):
    tasks = read_file()
    
    new_task_list = [];
    for task in tasks:
        if task['id'] == id:
            continue
        
        new_task_list.append(task)
    
    write_file(new_task_list)
    print(f"Задача створена, ID: {task['id']}")

def get_task_by_id(id: str):
    tasks = read_file()
    
    for task in tasks:
        if (task['id'] == id):
            return task

    return None

def update_task(task_to_update: dict[str, str]) -> None:
    tasks = read_file()

    to_update = []
    
    for task in tasks:
        if (task['id'] == task_to_update['id']):
            to_update.append(task_to_update)
        else:
            to_update.append(task)

    write_file(to_update)

def update_task_status(id: str, status: str) -> None:
    task = get_task_by_id(id)

    if task:
        task['status'] = status

        update_task(task)
    else:
        print(f'Задача не знайдена по ID: {id}')

def set_complete_task_status(id: str) -> None: 
    update_task_status(id, 'Виконана')
    print(f'Задача ID: {id} виконана!')

def set_new_task_status(id: str) -> None: 
    update_task_status(id, 'Нова')
    print(f'Задача ID: {id} має статус Нова!')

def edit_task(id: str): 
    task = get_task_by_id(id)
    
    if task:
        text = input('Що потрібно зробити? ')
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
