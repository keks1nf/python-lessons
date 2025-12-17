from rental_house.analysis import *
from rental_house.operations import *

DATABASE_NAME = 'rental_db.sqlite'


# --- МЕНЮ ---
def menu_analytics():
    """Меню для аналітики та звітів."""
    while True:
        print("\n--- МЕНЮ АНАЛІТИКИ ТА ЗВІТІВ ---")
        print("1. Фінансовий Звіт (Revenue, OPEX, TAXES, Net Profit)")
        print("2. Звіт OPEX за категоріями")
        print("3. Розрахунок заповнюваності (Occupancy Rate) (TBD)")
        print("4. Завантаженість по місяцях")
        print("5. Сезонний звіт (Дохід/Витрати/Завантаження)")
        print("0. Назад")
        choice = input("Виберіть дію: ")

        if choice == '1':
            start_date, end_date = get_period_dates()
            if start_date:
                calculate_financial_summary_full(start_date, end_date)
        elif choice == '2':
            start_date, end_date = get_period_dates()
            if start_date:
                report_opex_by_category(start_date, end_date)
        elif choice == '3':
            start_date, end_date = get_period_dates()
            if start_date:
                calculate_occupancy_rate_single_unit(start_date, end_date)
        elif choice == '4':
            display_monthly_occupancy()
        elif choice == '5':
            display_full_seasonality_report()
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def menu_clients():
    """Меню для керування клієнтами."""
    while True:
        print("\n--- МЕНЮ КЛІЄНТІВ (CRUD) ---")
        print("1. Додати клієнта")
        print("2. Редагувати клієнта")
        print("3. Видалити клієнта")
        print("4. Переглянути всіх клієнтів")
        print("0. Назад")
        choice = input("Виберіть дію: ")

        if choice == '1':
            add_client()
        elif choice == '2':
            update_client()
        elif choice == '3':
            delete_client()
        elif choice == '4':
            get_all_records('clients')
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def menu_bookings():
    """Меню для керування бронюваннями."""
    while True:
        print("\n--- МЕНЮ БРОНЮВАНЬ (CRUD) ---")
        print("1. Додати бронювання")
        print("2. Редагувати бронювання")
        print("3. Видалити бронювання")
        print("4. Переглянути всі бронювання")
        print("0. Назад")
        choice = input("Виберіть дію: ")

        if choice == '1':
            add_booking()
        elif choice == '2':
            update_booking()
        elif choice == '3':
            delete_booking()
        elif choice == '4':
            get_all_records('bookings')
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def menu_opex():
    """Меню для керування операційними витратами (OPEX)."""
    while True:
        print("\n--- МЕНЮ OPEX (CRUD) ---")
        print("1. Додати витрату")
        print("2. Редагувати витрату")
        print("3. Видалити витрату")
        print("4. Переглянути всі OPEX")
        print("0. Назад")
        choice = input("Виберіть дію: ")

        if choice == '1':
            add_opex()
        elif choice == '2':
            update_opex()
        elif choice == '3':
            delete_opex()
        elif choice == '4':
            get_all_records('opex')
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def menu_capex():
    """Меню для керування капітальними інвестиціями (CAPEX)."""
    while True:
        print("\n--- МЕНЮ CAPEX (CRUD) ---")
        print("1. Додати інвестицію")
        print("2. Редагувати інвестицію")
        print("3. Видалити інвестицію")
        print("4. Переглянути всі CAPEX")
        print("0. Назад")
        choice = input("Виберіть дію: ")

        if choice == '1':
            add_capex()
        elif choice == '2':
            update_capex()
        elif choice == '3':
            delete_capex()
        elif choice == '4':
            get_all_records('capex')
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def main():
    """Головна функція програми для навігації."""
    while True:
        print("\n===============================")
        print("  🏠 УПРАВЛІННЯ ОРЕНДОЮ НЕРУХОМОСТІ")
        print("===============================")
        print("1. Клієнти")
        print("2. Бронювання (Revenue)")
        print("3. Операційні витрати (OPEX)")
        print("4. Капітальні інвестиції (CAPEX)")
        print("5. Аналітика та Звіти")
        print("0. Вихід")

        main_choice = input("Виберіть розділ: ")

        if main_choice == '1':
            menu_clients()
        elif main_choice == '2':
            menu_bookings()
        elif main_choice == '3':
            menu_opex()
        elif main_choice == '4':
            menu_capex()
        elif main_choice == '5':
            menu_analytics()
        elif main_choice == '0':
            print("Дякуємо за використання! Програма завершує роботу.")
            break
        else:
            print("Невірний вибір. Будь ласка, введіть число від 0 до 4.")


if __name__ == '__main__':
    main()
