import json
import os
from datetime import datetime
import  time

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
    ID = str(int(time.time()))
    title = input("Введіть назву: ")
    text = input("Введіть текст: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "ID": ID,
        "title": title,
        "text": text,
        "date": date,
        "status": "created"
    }

    entries.append(entry)
    write_file(entries)
    print("додано")

def show_entries(entries: list | None = None) -> None:
    if entries is None:
        entries = read_file()

    if not entries:
        print("У щоденнику немає записів.")
        return

    entries.sort(key=lambda x: x.get("date", ""), reverse=True)

    for i, entry in enumerate(entries, start=1):
        print(f"\n--- Запис {i} ---")
        print(f"ID: {entry.get('ID', entry.get('id', 'Невідомо'))}")
        print(f"Назва: {entry.get('title', 'Без назви')}")
        print(f"Дата: {entry.get('date', 'Невідомо')} ({entry.get('status', 'невідомо')})")
        print(f"Текст: {entry.get('text', '')}")



def get_entry_by_id(ID: str):
    entries = read_file()
    return next((e for e in entries if e.get('ID') == ID), None)


def update_entry(entry_to_update: dict[str, str]) -> None:
    entries = read_file()
    updated = [entry_to_update if e['ID'] == entry_to_update['ID'] else e for e in entries]
    write_file(updated)


def update_entry_status(ID: str, status: str) -> None:
    entry = get_entry_by_id(ID)
    if entry:
        entry['status'] = status
        update_entry(entry)
        print(f"ID {ID} → статус '{status}'")
    else:
        print(f"ID {ID} не знайдено.")


def edit_entry(ID: str | None = None):
    if ID is None:
        ID = input("Введіть ID запису: ")

    entry = get_entry_by_id(ID)
    if not entry:
        print(f"ID {ID} не знайдено.")
        return

    text = input(f"Новий текст (поточний: {entry['text']}): ") or entry['text']

    entry['text'] = text
    entry['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry['status'] = "modified"

    update_entry(entry)
    print(f"ID {ID} оновлено.")


def delete_entry(ID: str | None = None) -> None:

    if not ID:
        ID = input("Введіть ID для видалення: ").strip()

    entries = read_file()


    if not entries:
        print("Щоденник порожній.")
        return


    new_entries = [e for e in entries if e.get('ID') != ID]

    if len(new_entries) != len(entries):
        write_file(new_entries)
        print(f"Запис ID {ID} видалено.")
    else:
        print(f"Запис з ID {ID} не знайдено.")


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
