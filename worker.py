import json
import os

DATA_FILE = "files\\data.json"


def add_worker(name: str, age: int, job: str, skills: list[str]):

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []


    worker = {
        "name": name,
        "age": age,
        "job": job,
        "skills": skills
    }


    data.append(worker)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Працівника '{name}' додано у файл.")



def print_workers():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            workers = json.load(f)

        if not workers:
            print("Gоки немає працівників.")
            return

        print("\nДосьє працівників:\n")
        for w in workers:
            print(f"{w.get('name', 'Невідомо')}, {w.get('age', 'Невідомо')} років")
            print(f"  Місце роботи та адреса: {w.get('job', 'Невідомо')}")
            print("  Навички:")
            for s in w.get("skills", []):
                print(f"     {s}")
            print()


def main():
    while True:
        print("1 — Додати працівника")
        print("2 — Показати працівників")
        print("3 — Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            name = input("Ім'я: ")
            age = int(input("Вік: "))
            job = input("Місце роботи та адреса: ")
            skills = input("Навички (кома): ").split(",")
            skills = [s.strip() for s in skills]
            add_worker(name, age, job, skills)

        elif choice == "2":
            print_workers()

        elif choice == "3":
            print("Вихід")
            break
        else:
            print("Невірний вибір")


if __name__ == '__main__':
    main()

