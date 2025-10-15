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
    id = str(int(time.time()))
    title = input("Введіть назву: ")
    text = input("Введіть текст: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "id": id,
        "title": title,
        "text": text,
        "date": date,
        "status": "created"
    }

    entries.append(entry)
    write_file(entries)
    print("додано")

def show_entries() -> None:
    entries = read_file()

    if not entries:
        print("У щоденнику немає записів.")
        return

    entries.sort(key=lambda x: x.get("date", ""), reverse=True)

    for i, entry in enumerate(entries, start=1):
        print(f"\n--- Запис {i} ---")
        print(f"id: {entry.get('id', entry.get('id', 'Невідомо'))}")
        print(f"Назва: {entry.get('title', 'Без назви')}")
        print(f"Дата: {entry.get('date', 'Невідомо')} ({entry.get('status', 'невідомо')})")
        print(f"Текст: {entry.get('text', '')}")



def get_entry_by_id(id: str):
    entries = read_file()
    return next((e for e in entries if e.get('id') == id), None)


def update_entry(entry_to_update: dict[str, str]) -> None:
    entries = read_file()
    updated = [entry_to_update if e['id'] == entry_to_update['id'] else e for e in entries]
    write_file(updated)


def update_entry_status(id: str, status: str) -> None:
    entry = get_entry_by_id(id)
    if entry:
        entry['status'] = status
        update_entry(entry)
        print(f"id {id} → статус '{status}'")
    else:
        print(f"id {id} не знайдено.")


def edit_entry():
    id = input("Введіть id запису: ")

    entry = get_entry_by_id(id)
    if not entry:
        print(f"id {id} не знайдено.")
        return

    text = input(f"Новий текст (поточний: {entry['text']}): ") or entry['text']

    entry['text'] = text
    entry['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry['status'] = "modified"

    update_entry(entry)
    print(f"id {id} оновлено.")


def delete_entry() -> None:
    id = input("Введіть id для видалення: ").strip()

    entries = read_file()

    if not entries:
        print("Щоденник порожній.")
        return


    new_entries = [e for e in entries if e.get('id') != id]

    if len(new_entries) != len(entries):
        write_file(new_entries)
        print(f"Запис id {id} видалено.")
    else:
        print(f"Запис з id {id} не знайдено.")


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
