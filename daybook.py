import json
import os
from datetime import datetime

DATA_FILE = "diary.json"

def write_file(entries: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=4)


def read_file() -> list:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []


def add_entry():
    entries = read_file()
    title = input("Введіть назву: ")
    text = input("Введіть текст: ")
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    entry = {
        "title": title,
        "text": text,
        "date": date,
        "status": "created"
    }

    entries.append(entry)
    write_file(entries)
    print("додано")

def show_entries():
    entries = read_file()

    if not entries:
        print("У щоденнику немає записів.")
        return


    entries.sort(key=lambda x: x["date"], reverse=True)

    for i, entry in enumerate(entries, start=1):
        print(f"\n--- Запис {i} ---")
        print(f"Назва: {entry['title']}")
        print(f"Дата: {entry['date']} ({entry['status']})")
        print(f"Текст: {entry['text']}")


def edit_entry():
    entries = read_file()
    show_entries()

    if not entries:
        return

    num = int(input("\nВведіть номер запису для редагування: ")) - 1

    if 0 <= num < len(entries):
pass

def delete_entry():
    pass

def main_menu():
    while True:
        print("\n=== ЩОДЕННИК ===")
        print("1. Додати запис")
        print("2. Переглянути записи")
        print("3. Редагувати запис")
        print("4. Видалити запис")
        print("5. Вийти")

        choice = input("Виберіть дію: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            show_entries()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("До побачення!")
            exit()
        else:
            print("Невідома команда.")



if __name__ == "__main__":
        main_menu()
