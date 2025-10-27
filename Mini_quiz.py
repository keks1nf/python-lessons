import json
import os
import random
from datetime import datetime

def get_question_file_path():
    return os.path.join("files", "questions.json")

def get_result_file_path():
    return os.path.join("files", "results.json")

def load_json(filename: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(filename: str, data: list) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_question():
    print("\n--- Додавання нового питання ---")
    question_text = input("Введіть питання: ").strip()

    options = []
    num_options = int(input("Скільки варіантів відповіді? "))

    for i in range(num_options):
        option = input(f"Варіант {i + 1}: ").strip()
        options.append(option)

    correct = int(input("Номер правильної відповіді: "))

    new_question = {
        "question": question_text,
        "options": options,
        "answer": correct
    }


    questions = load_json(get_question_file_path())
    questions.append(new_question)
    save_json(get_question_file_path(), questions)

    print("Питання успішно додано!\n")



def run_quiz():
    questions = load_json(get_question_file_path())

    if not questions:
        print("Немає питань для вікторини.")
        return

    random.shuffle(questions)
    print("Вітаємо у міні-вікторині!")

    username = input("Введіть своє ім'я: ")
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nПитання {i}: {q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")

        try:
            answer = int(input("Ваша відповідь (номер): "))
            if answer == q["answer"]:
                print("Правильно!")
                score += 1
            else:
                print(f"Неправильно! Правильна відповідь: {q['options'][q['answer'] - 1]}")
        except ValueError:
            print("Введіть число!")

    print(f"\n{username}, ваш результат: {score} із {len(questions)}")
    save_result(username, score, len(questions))
    print("Результати збережено у 'results.json'.")



def save_result(username: str, score: int, total: int):
    results = load_json(get_result_file_path())
    results.append({
        "user": username,
        "score": score,
        "total": total,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_json(get_result_file_path(), results)



def show_results():
    results = load_json(get_result_file_path())

    if not results:
        print("Ще ніхто не проходив вікторину.")
        return

    print("\nРезультати вікторини:")
    for res in results:
        print(f"{res['user']} — {res['score']}/{res['total']} ({res['date']})")



def main():
    while True:
        print("\n=== МЕНЮ ВІКТОРИНИ ===")
        print("1. Пройти вікторину")
        print("2. Додати нове питання")
        print("3. Переглянути результати")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            show_results()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
