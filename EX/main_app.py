from datetime import datetime

from db_setup import setup_database

from EX import crud_operations as crud


# --- Утиліти вводу ---
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Будь ласка, введіть ціле число.")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("❌ Будь ласка, введіть число (використовуйте крапку або кому).")


def get_date_input(prompt):
    while True:
        date_str = input(prompt + " (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("❌ Невірний формат дати. Використовуйте YYYY-MM-DD.")


# --- Функції Меню ---

def menu_clients():
    print("\n--- МЕНЮ КЛІЄНТІВ ---")
    print("1. Додати клієнта")
    print("2. Редагувати клієнта")
    print("3. Видалити клієнта")
    print("4. Переглянути всіх клієнтів")
    print("0. Назад")
    choice = input("Виберіть дію: ")

    if choice == '1':
        customer_id = input("ID клієнта: ")
        check_in = input("Телефон: ")
        check_out = input("Email: ")
        nights = input("Країна: ")
        total_price = input('Сума: ')
        crud.add_client(customer_id, check_in, check_out, nights, total_price)
        print("✅ Клієнта додано.")

    elif choice == '2':
        cid = get_int_input("ID клієнта для редагування: ")
        client = crud.get_client(cid)
        if client:
            print(f"Редагування клієнта: {client}")
            name = input(f"Нове Ім'я ({client[1]}): ") or client[1]
            phone = input(f"Новий номер телефону ({client[2]}): ") or client[2]
            email = input(f"Новий Email ({client[3]}): ") or client[3]
            country = input(f"Нова Країна ({client[4]}): ") or client[4]
            crud.update_client(cid, name, phone, email, country)
            print(f"✅ Клієнта ID:{cid} оновлено.")
        else:
            print("❌ Клієнта з таким ID не знайдено.")

    elif choice == '3':
        cid = get_int_input("ID клієнта для видалення: ")
        if crud.get_client(cid):
            crud.delete_client(cid)
            print(f"✅ Клієнта ID:{cid} видалено.")
        else:
            print("❌ Клієнта з таким ID не знайдено.")

    elif choice == '4':
        print("\n--- СПИСОК КЛІЄНТІВ ---")
        clients = crud.get_all_records('clients')
        for c in clients:
            print(f"ID: {c[0]} | {c[1]} {c[2]} | {c[3]} ({c[4]})")
        print("-----------------------")

    elif choice == '0':
        return
    else:
        print("Невірний вибір.")


# --- Функції для OPEX, BOOKINGS, CAPEX

def menu_bookings():
    # ... (Реалізація функцій add_booking, update_booking, delete_booking, get_all_records('bookings'))
    print("\n--- МЕНЮ БРОНЮВАНЬ (реалізувати CRUD) ---")
    print("1. Додати бронювання")
    print("2. Редагувати бронювання")
    print("3. Видалити бронювання")
    print("4. Переглянути всі бронювання")
    print("0. Назад")
    choice = input("Виберіть дію: ")


def menu_opex():
    # ... (Реалізація функцій add_opex, update_opex, delete_opex, get_all_records('opex'))
    print("\n--- МЕНЮ OPEX (реалізувати CRUD) ---")
    pass


def menu_capex():
    # ... (Реалізація функцій add_capex, update_capex, delete_capex, get_all_records('capex'))
    print("\n--- МЕНЮ CAPEX (реалізувати CRUD) ---")
    pass


# --- Головна Функція ---

def main_menu():
    """Відображає головне меню програми."""
    while True:
        print("\n===============================")
        print("🏠 СИСТЕМА УПРАВЛІННЯ ОРЕНДОЮ")
        print("===============================")
        print("1. Клієнти (CRUD)")
        print("2. Бронювання (CRUD)")
        print("3. Операційні Витрати (OPEX CRUD)")
        print("4. Капітальні Інвестиції (CAPEX CRUD)")
        print("0. Вихід")

        main_choice = input("Оберіть розділ: ")

        if main_choice == '1':
            menu_clients()
        elif main_choice == '2':
            menu_bookings()
        elif main_choice == '3':
            menu_opex()
        elif main_choice == '4':
            menu_capex()
        elif main_choice == '0':
            print("Дякую за використання програми! До побачення.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == '__main__':
    # Перевіряємо та створюємо БД перед запуском
    setup_database()
    main_menu()
