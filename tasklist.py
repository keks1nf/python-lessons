from datetime import datetime

from unicodedata import category


def add_task(tasks):
   new_task = input('Введіть нове завдання: ')
   category = input("Введіть категорію (робота, навчання, дім, особисте...): ").strip().lower()
   tasks.append({"task": new_task, "execution": False, 'category': category})
   print(tasks)
def remove_task(tasks):
    show_all_tasks(tasks)
    tasks_num = int(input('Введіть номер завдання для видалення: '))
    if 1 <= tasks_num <= len(tasks):
        removed_task = tasks.pop(tasks_num - 1)
        print(f'Видалено завдання: {removed_task["task"]}')
    else:
        print('Невірний номер завдання!')
def mark_done(tasks):
    show_all_tasks(tasks)
    num_done = int(input('Введіть номер виконаного завдання: '))
    if 1 <= num_done <= len(tasks):
        tasks[num_done-1]["execution"] = True
        print(tasks)
def show_all_tasks(tasks):
    if not  tasks:
        print('Список порожній')
        return
    for i, task in enumerate(tasks, start=1):
        status = 'True' if task["execution"] else 'False'
        print(f"{i}. [{task['category']}] {task['task']}")
def show_pending_tasks(tasks):
     pending = [t for t in tasks if not t['execution']]
     if not pending:
         print('Виконано')
     else:
        for i, t in enumerate(pending, start=1 ):
            print(f"{i}. [{t['category']}] {t['task']}")

def filter_by_category(tasks):
    category = input("Введіть категорію для фільтрації: ").strip().lower()
    filtered = [t for t in tasks if t["category"] == category]

    if not filtered:
        print(f"Немає завдань у категорії '{category}'.")
    else:
        print(f"\n--- Завдання у категорії '{category}' ---")
        for i, t in enumerate(filtered, start=1):
            status = "True" if t["execution"] else "False"
            print(f"{i}. {t['task']} {status}")

def main_menu():
    tasks = []
    while True:
        current_date = datetime.now().date()
        print(current_date)
        print('\n Меню')
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Позначити виконаним")
        print("4. Показати всі завдання")
        print("5. Показати невиконані завдання")
        print("6. Фільтр по категоріям")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            show_all_tasks(tasks)
        elif choice == "5":
            show_pending_tasks(tasks)
        elif choice == "6":
            filter_by_category(tasks)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірна команда, спробуйте ще раз.")

if __name__ == '__main__':
    main_menu()
