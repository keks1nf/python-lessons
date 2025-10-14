import json
import os
import time

'''
Функція	Дія
json.dump(obj, file)	записує Python-об’єкт у JSON-файл
json.load(file)	читає JSON-файл і повертає Python-об’єкт
json.dumps(obj)	перетворює Python-об’єкт у JSON-рядок
json.loads(str)	перетворює JSON-рядок у Python-об’єкт

Основні режими роботи з файлами
Режим	Повна назва	Що робить
'r'	read	🔹 Відкриває файл для читання. Файл має вже існувати.
'w'	write	🔹 Відкриває файл для запису. Якщо файл існує — усе в ньому стирається! Якщо не існує — створюється новий файл.
'a'	append	🔹 Відкриває файл для додавання (новий текст додається в кінець, нічого не стирається).
'x'	exclusive creation	🔹 Створює новий файл, якщо такого ще немає. Якщо файл існує — буде помилка.


'''

def main_menu() -> None:
    print('Програма для управління задачами. Дані зберігаються у файлі data.json')
    print('Команди:')
    print("add              Додати завдання")
    print("rm <id>          Видалити завдання")
    print("complete <id>    Позначити виконаним")
    print("revert <id>      Відмінити виконання")
    print("edit <id>        Редагувати завдання")
    print("ls               Показати всі завдання")
    print("filter <category>Показати завдання певної категорії")
    print("help             Показати це меню")



def write_file(tasks: list) -> None:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def read_file() -> list:
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []


def show_tasks(tasks: list | None = None) -> None:
    if tasks is None:
        tasks = read_file()

    print(f"\n{'ID':<12}{'Завдання':<30}{'Категорія':<15}{'Статус'}")
    print("-" * 70)

    if tasks:
        for task in tasks:
            print(f"{task['id']:<12}{task['text']:<30}{task.get('category', '-'):<15}{task['status']}")
    else:
        print('Завдань немає. Використовуйте "add", щоб додати нове.')


def add_task() -> None:
    tasks = read_file()

    text = input('Введіть завдання: ')
    category = input('Введіть категорію (робота, навчання, дім, особисте...): ').strip().lower()

    task = {
        'text': text,
        'id': str(int(time.time())),
        'status': 'Нова',
        'category': category if category else 'загальна',
    }

    tasks.append(task)
    write_file(tasks)
    print(f"Завдання створено (ID: {task['id']})")


def rm_task(id: str):
    tasks = read_file()
    new_task_list = [t for t in tasks if t['id'] != id]

    if len(new_task_list) != len(tasks):
        write_file(new_task_list)
        print(f"Завдання ID {id} видалено.")
    else:
        print(f"Завдання з ID {id} не знайдено.")


def get_task_by_id(id: str):
    tasks = read_file()
    return next((t for t in tasks if t['id'] == id), None)


def update_task(task_to_update: dict[str, str]) -> None:
    tasks = read_file()
    updated = [task_to_update if t['id'] == task_to_update['id'] else t for t in tasks]
    write_file(updated)


def update_task_status(id: str, status: str) -> None:
    task = get_task_by_id(id)
    if task:
        task['status'] = status
        update_task(task)
        print(f"Завдання ID {id} → статус '{status}'")
    else:
        print(f"Завдання ID {id} не знайдено.")


def edit_task(id: str):
    task = get_task_by_id(id)
    if not task:
        print(f"Завдання ID {id} не знайдено.")
        return

    text = input(f" Новий текст (поточний: {task['text']}): ") or task['text']
    category = input(f"Нова категорія (поточна: {task.get('category', '-')}) : ") or task.get('category', 'загальна')

    task['text'] = text
    task['category'] = category
    update_task(task)

    print(f"Завдання ID {id} оновлено.")


def filter_by_category(category: str):
    tasks = read_file()
    filtered = [t for t in tasks if t.get('category', '').lower() == category.lower()]

    if filtered:
        print(f"\nЗавдання у категорії '{category}':")
        show_tasks(filtered)
    else:
        print(f"Немає завдань у категорії '{category}'.")


def main():
    main_menu()
    while True:
        parts = input('\nКоманда: ').split(' ', 1)
        command, *args = parts

        if command == 'ls':
            show_tasks()
        elif command == 'add':
            add_task()
        elif command == 'rm':
            rm_task(args[0] if args else '')
        elif command == 'complete':
            update_task_status(args[0], 'Виконана')
        elif command == 'revert':
            update_task_status(args[0], 'Нова')
        elif command == 'edit':
            edit_task(args[0])
        elif command == 'filter':
            if args:
                filter_by_category(args[0])
            else:
                print("Вкажіть категорію після команди: filter <category>")
        elif command == 'help':
            main_menu()
        else:
            print("Невідома команда. Введіть 'help'.")


if __name__ == '__main__':
    main()
