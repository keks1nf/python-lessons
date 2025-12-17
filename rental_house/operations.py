import sqlite3
from datetime import datetime

DATABASE_NAME = 'rental_db.sqlite'


# --- З'ЄДНАННЯ З БД ---
def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)


# # --- Утиліти вводу ---
# def get_int_input(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Введіть ціле число.")
#
#
# def get_float_input(prompt):
#     while True:
#         try:
#             return float(input(prompt).replace(',', '.'))
#         except ValueError:
#             print("Введіть число (використовуйте крапку або кому).")
#
#
# def get_date_input(prompt):
#     while True:
#         date_str = input(prompt + " (YYYY-MM-DD): ")
#         try:
#             datetime.strptime(date_str, '%Y-%m-%d')
#             return date_str
#         except ValueError:
#             print("Невірний формат дати. Використовуйте YYYY-MM-DD.")


# --- CLIENTS ---

def add_client():
    """Додає нового клієнта"""
    print("\n--- ДОДАТИ НОВОГО КЛІЄНТА ---")
    name = input("Введіть повне ім'я клієнта (name): ")
    phone = input("Введіть телефон клієнта (phone): ")
    email = input("Введіть email клієнта (email): ")
    country = input("Введіть країну клієнта (country): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clients (name, phone, email, country)
            VALUES (?, ?, ?, ?)
        """, (name, phone, email, country))

        conn.commit()
        print(f"✅ Клієнт '{name}' успішно доданий. ID: {cursor.lastrowid}")
    except sqlite3.IntegrityError:
        print("❌ Помилка: Клієнт з таким email вже існує (email має бути унікальним).")
    except sqlite3.Error as e:
        print(f"❌ Помилка додавання клієнта: {e}")
    finally:
        conn.close()


def update_client():
    """Оновлює за customer_id."""
    print("\n--- РЕДАГУВАТИ КЛІЄНТА ---")
    customer_id = input("Введіть ID клієнта, якого потрібно оновити (customer_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # перевірка наявності запису
        cursor.execute("SELECT * FROM clients WHERE customer_id=?", (customer_id,))
        if not cursor.fetchone():
            print(f"❌ Клієнт з ID {customer_id} не знайдений.")
            return

        print("Введіть нові дані (залиште порожнім, щоб не змінювати):")

        #  нові дані
        new_name = input(
            f"Нове ім'я (поточне: {get_current_value(conn, 'clients', 'name', customer_id, 'customer_id')}): ")
        new_phone = input(
            f"Новий телефон (поточний: {get_current_value(conn, 'clients', 'phone', customer_id, 'customer_id')}): ")
        new_email = input(
            f"Новий email (поточний: {get_current_value(conn, 'clients', 'email', customer_id, 'customer_id')}): ")
        new_country = input(
            f"Нова країна (поточна: {get_current_value(conn, 'clients', 'country', customer_id, 'customer_id')}): ")

        updates = []
        params = []

        if new_name:
            updates.append("name=?")
            params.append(new_name)
        if new_phone:
            updates.append("phone=?")
            params.append(new_phone)
        if new_email:
            updates.append("email=?")
            params.append(new_email)
        if new_country:
            updates.append("country=?")
            params.append(new_country)

        if not updates:
            print("Немає даних для оновлення.")
            return

        sql = f"UPDATE clients SET {', '.join(updates)} WHERE customer_id=?"
        params.append(customer_id)

        cursor.execute(sql, tuple(params))
        conn.commit()
        print(f"✅ Клієнт ID {customer_id} успішно оновлений.")

    except sqlite3.IntegrityError:
        print("❌ Помилка: Клієнт з таким email вже існує.")
    except sqlite3.Error as e:
        print(f"❌ Помилка оновлення клієнта: {e}")
    finally:
        conn.close()


def delete_client():
    """Видаляє за customer_id."""
    print("\n--- ВИДАЛИТИ КЛІЄНТА ---")
    customer_id = input("Введіть ID клієнта, якого потрібно видалити (customer_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clients WHERE customer_id=?", (customer_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Клієнт ID {customer_id} успішно видалений.")
        else:
            print(f"❌ Клієнт з ID {customer_id} не знайдений.")

    except sqlite3.IntegrityError:
        # спрацює, якщо клієнт має активні бронювання
        print("❌ Помилка: Неможливо видалити клієнта, оскільки він має існуючі бронювання.")
    except sqlite3.Error as e:
        print(f"❌ Помилка видалення клієнта: {e}")
    finally:
        conn.close()


# ---  ДОПОМІЖНІ ФУНКЦІЇ ---

def get_current_value(conn, table, column, pk_value, pk_column):
    """отримує поточне значення стовпця для відображення в меню оновлення."""
    cursor = conn.cursor()
    # Захист від SQL Injection
    cursor.execute(f"SELECT {column} FROM {table} WHERE {pk_column}=?", (pk_value,))
    result = cursor.fetchone()
    return result[0] if result else 'N/A'


def check_customer_exists(customer_id):
    """ перевіряє чи існує клієнт з даним ID (bookings)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM clients WHERE customer_id=?", (customer_id,))
        return cursor.fetchone() is not None
    finally:
        conn.close()


def get_all_records(table_name):
    """виводить всі записи таблиці"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")

        # заголовки
        column_names = [description[0] for description in cursor.description]
        print(f"\n--- ВСІ ЗАПИСИ З ТАБЛИЦІ '{table_name}' ---")
        print(" | ".join(column_names))
        print("-" * (sum(len(name) for name in column_names) + 3 * len(column_names)))

        # записи
        records = cursor.fetchall()
        for record in records:
            #  можливе виведення None
            print(" | ".join(map(lambda x: str(x) if x is not None else 'NULL', record)))

    except sqlite3.OperationalError as e:
        print(
            f"❌ Помилка: Не вдалося виконати запит до таблиці {table_name}. Можливо, таблиця порожня або не існує. {e}")
    finally:
        conn.close()


# ---  BOOKINGS  ---

def calculate_nights(check_in_str, check_out_str):
    """кількість ночей між датами"""
    try:
        check_in = datetime.strptime(check_in_str, '%Y-%m-%d')
        check_out = datetime.strptime(check_out_str, '%Y-%m-%d')
        nights = (check_out - check_in).days
        return nights if nights > 0 else 0
    except ValueError:
        return 0


def add_booking():
    """ нове бронювання bookings"""
    print("\n--- ДОДАТИ НОВЕ БРОНЮВАННЯ ---")
    customer_id = input("Введіть ID клієнта (customer_id): ")
    try:
        if not check_customer_exists(customer_id):
            print(f"❌ Клієнт з ID {customer_id} не знайдений. Будь ласка, спочатку додайте клієнта.")
            return
    except ValueError:
        print("Некоректний ID клієнта.")
        return

    check_in = input("Введіть дату заїзду (YYYY-MM-DD): ")
    check_out = input("Введіть дату виїзду (YYYY-MM-DD): ")

    nights = calculate_nights(check_in, check_out)
    if nights <= 0:
        print("❌ Некоректні дати. Дата виїзду має бути пізніше дати заїзду.")
        return

    print(f"Розрахована кількість ночей: {nights}")
    total_price = input("Введіть загальну вартість бронювання (total_price): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO bookings (customer_id, check_in, check_out, nights, total_price)
            VALUES (?, ?, ?, ?, ?)
        """, (customer_id, check_in, check_out, nights, total_price))

        conn.commit()
        print(f"✅ Бронювання для клієнта ID {customer_id} успішно додано. ID: {cursor.lastrowid}")
    except sqlite3.Error as e:
        print(f"❌ Помилка додавання бронювання: {e}")
    finally:
        conn.close()


def update_booking():
    """oновлює існуюче бронювання за booking_id."""
    print("\n--- РЕДАГУВАТИ БРОНЮВАННЯ ---")
    booking_id = input("Введіть ID бронювання, яке потрібно оновити (booking_id): ")

    conn = get_db_connection()

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings WHERE booking_id=?", (booking_id,))
        if not cursor.fetchone():
            print(f"❌ Бронювання з ID {booking_id} не знайдено.")
            return

        print("Введіть нові дані (залиште порожнім, щоб не змінювати):")

        # Отримання нових даних
        new_customer_id = input(
            f"Новий ID клієнта (поточний: {get_current_value(conn, 'bookings', 'customer_id', booking_id, 'booking_id')}): ")
        new_check_in = input(
            f"Нова дата заїзду (поточна: {get_current_value(conn, 'bookings', 'check_in', booking_id, 'booking_id')}): ")
        new_check_out = input(
            f"Нова дата виїзду (поточна: {get_current_value(conn, 'bookings', 'check_out', booking_id, 'booking_id')}): ")
        new_total_price = input(
            f"Нова загальна вартість (поточна: {get_current_value(conn, 'bookings', 'total_price', booking_id, 'booking_id')}): ")

        updates = []
        params = []

        if new_customer_id:
            if not check_customer_exists(new_customer_id):
                print(f"❌ Клієнт з ID {new_customer_id} не знайдений. Оновлення скасовано.")
                return
            updates.append("customer_id=?")
            params.append(new_customer_id)

        if new_check_in or new_check_out:
            current_check_in = new_check_in or get_current_value(conn, 'bookings', 'check_in', booking_id, 'booking_id')
            current_check_out = new_check_out or get_current_value(conn, 'bookings', 'check_out', booking_id,
                                                                   'booking_id')

            new_nights = calculate_nights(current_check_in, current_check_out)

            if new_nights <= 0 and (new_check_in or new_check_out):
                print("❌ Некоректні дати. Дата виїзду має бути пізніше дати заїзду. Оновлення скасовано.")
                return

            if new_check_in:
                updates.append("check_in=?")
                params.append(new_check_in)

            if new_check_out:
                updates.append("check_out=?")
                params.append(new_check_out)

            updates.append("nights=?")
            params.append(new_nights)
            print(f"   (Нічні перераховані: {new_nights} ночей)")

        if new_total_price:
            updates.append("total_price=?")
            params.append(new_total_price)

        if not updates:
            print("Немає даних для оновлення.")
            return

        # Побудова та виконання SQL-запиту
        sql = f"UPDATE bookings SET {', '.join(updates)} WHERE booking_id=?"
        params.append(booking_id)

        cursor.execute(sql, tuple(params))
        conn.commit()
        print(f"✅ Бронювання ID {booking_id} успішно оновлено.")

    except sqlite3.Error as e:
        print(f"❌ Помилка оновлення бронювання: {e}")
    finally:
        conn.close()


def delete_booking():
    """Видаляє бронювання за booking_id."""
    print("\n--- ВИДАЛИТИ БРОНЮВАННЯ ---")
    booking_id = input("Введіть ID бронювання, яке потрібно видалити (booking_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM bookings WHERE booking_id=?", (booking_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Бронювання ID {booking_id} успішно видалено.")
        else:
            print(f"❌ Бронювання з ID {booking_id} не знайдено.")

    except sqlite3.Error as e:
        print(f"❌ Помилка видалення бронювання: {e}")
    finally:
        conn.close()


# ---- OPEX ----

def add_opex():
    """додає нову операційну витрату"""
    print("\n--- ДОДАТИ НОВУ ОПЕРАЦІЙНУ ВИТРАТУ ---")

    opex_date = input("Введіть дату витрати (YYYY-MM-DD): ")
    category = input("Введіть категорію (напр., Utilities, Cleaning, Repairs): ")

    try:
        amount = float(input("Введіть суму витрати (amount): "))
    except ValueError:
        print("❌ Некоректна сума.")
        return

    notes = input("Введіть примітки (notes, опціонально): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO opex (opex_date, category, amount, notes)
            VALUES (?, ?, ?, ?)
        """, (opex_date, category, amount, notes))

        conn.commit()
        print(f"✅ Витрата '{category}' на суму {amount} успішно додана. ID: {cursor.lastrowid}")
    except sqlite3.Error as e:
        print(f"❌ Помилка додавання витрати: {e}")
    finally:
        conn.close()


def update_opex():
    """оновлює за opex_id."""
    print("\n--- РЕДАГУВАТИ OPEX ---")
    opex_id = input("Введіть ID витрати, яку потрібно оновити (opex_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        #  наявність запису
        cursor.execute("SELECT * FROM opex WHERE opex_id=?", (opex_id,))
        if not cursor.fetchone():
            print(f"❌ Витрату з ID {opex_id} не знайдено.")
            return

        print("Введіть нові дані (залиште порожнім, щоб не змінювати):")

        # нові дані
        new_date = input(f"Нова дата (поточна: {get_current_value(conn, 'opex', 'opex_date', opex_id, 'opex_id')}): ")
        new_category = input(
            f"Нова категорія (поточна: {get_current_value(conn, 'opex', 'category', opex_id, 'opex_id')}): ")
        new_amount_str = input(
            f"Нова сума (поточна: {get_current_value(conn, 'opex', 'amount', opex_id, 'opex_id')}): ")

        new_notes = input(f"Нові примітки (поточні: {get_current_value(conn, 'opex', 'notes', opex_id, 'opex_id')}): ")

        updates = []
        params = []

        if new_date:
            updates.append("opex_date=?")
            params.append(new_date)
        if new_category:
            updates.append("category=?")
            params.append(new_category)
        if new_amount_str:
            try:
                new_amount = float(new_amount_str)
                updates.append("amount=?")
                params.append(new_amount)
            except ValueError:
                print("❌ Некоректна сума. Оновлення скасовано.")
                return

        if 'new_notes' in locals() and new_notes:
            updates.append("notes=?")
            params.append(new_notes)

        if not updates:
            print("Немає даних для оновлення.")
            return

        # SQL-запит
        sql = f"UPDATE opex SET {', '.join(updates)} WHERE opex_id=?"
        params.append(opex_id)

        cursor.execute(sql, tuple(params))
        conn.commit()
        print(f"✅ Витрату ID {opex_id} успішно оновлено.")

    except sqlite3.Error as e:
        print(f"❌ Помилка оновлення витрати: {e}")
    finally:
        conn.close()


def delete_opex():
    """видаляє за opex_id."""
    print("\n--- ВИДАЛИТИ OPEX ---")
    opex_id = input("Введіть ID витрати, яку потрібно видалити (opex_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM opex WHERE opex_id=?", (opex_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Витрату ID {opex_id} успішно видалено.")
        else:
            print(f"❌ Витрату з ID {opex_id} не знайдено.")

    except sqlite3.Error as e:
        print(f"❌ Помилка видалення витрати: {e}")
    finally:
        conn.close()


# ----- CAPEX ------


def add_capex():
    """додає нову до таблиці capex."""
    print("\n--- ДОДАТИ НОВУ КАПІТАЛЬНУ ІНВЕСТИЦІЮ ---")

    capex_date = input("Введіть дату інвестиції (YYYY-MM-DD): ")
    category = input("Введіть категорію (напр., Furniture, Construction, Equipment): ")

    try:
        amount = float(input("Введіть суму інвестиції (amount): "))
    except ValueError:
        print("❌ Некоректна сума.")
        return

    notes = input("Введіть примітки (notes, опціонально): ")

    # чи підлягає амортизації
    depreciable_input = input("Чи підлягає актив амортизації? (Так/Ні): ").lower()
    is_depreciable = 1 if depreciable_input in ('так', 'yes', 't', '1') else 0

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO capex (capex_date, category, amount, notes, is_depreciable)
            VALUES (?, ?, ?, ?, ?)
        """, (capex_date, category, amount, notes, is_depreciable))

        conn.commit()
        print(f"✅ Інвестицію '{category}' на суму {amount} успішно додано. ID: {cursor.lastrowid}")
    except sqlite3.Error as e:
        print(f"❌ Помилка додавання інвестиції: {e}")
    finally:
        conn.close()


def update_capex():
    """оновлює чинну за capex_id."""
    print("\n--- РЕДАГУВАТИ CAPEX ---")
    capex_id = input("Введіть ID інвестиції, яку потрібно оновити (capex_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        #  наявність запису
        cursor.execute("SELECT * FROM capex WHERE capex_id=?", (capex_id,))
        if not cursor.fetchone():
            print(f"❌ Інвестицію з ID {capex_id} не знайдено.")
            return

        print("Введіть нові дані (залиште порожнім, щоб не змінювати):")

        # поточні значення
        current_date = get_current_value(conn, 'capex', 'capex_date', capex_id, 'capex_id')
        current_category = get_current_value(conn, 'capex', 'category', capex_id, 'capex_id')
        current_amount = get_current_value(conn, 'capex', 'amount', capex_id, 'capex_id')
        current_notes = get_current_value(conn, 'capex', 'notes', capex_id, 'capex_id')
        current_depreciable = "Так" if get_current_value(conn, 'capex', 'is_depreciable', capex_id,
                                                         'capex_id') == 1 else "Ні"

        #  нові дані
        new_date = input(f"Нова дата (поточна: {current_date}): ")
        new_category = input(f"Нова категорія (поточна: {current_category}): ")
        new_amount_str = input(f"Нова сума (поточна: {current_amount}): ")
        new_notes = input(f"Нові примітки (поточні: {current_notes}): ")
        new_depreciable_input = input(f"Чи підлягає актив амортизації? (Так/Ні, поточна: {current_depreciable}): ")

        updates = []
        params = []

        if new_date:
            updates.append("capex_date=?")
            params.append(new_date)
        if new_category:
            updates.append("category=?")
            params.append(new_category)

        if new_amount_str:
            try:
                new_amount = float(new_amount_str)
                updates.append("amount=?")
                params.append(new_amount)
            except ValueError:
                print("❌ Некоректна сума. Оновлення скасовано.")
                return

        if new_notes:
            updates.append("notes=?")
            params.append(new_notes)

        if new_depreciable_input:
            new_is_depreciable = 1 if new_depreciable_input.lower() in ('так', 'yes', 't', '1') else 0
            updates.append("is_depreciable=?")
            params.append(new_is_depreciable)

        if not updates:
            print("Немає даних для оновлення.")
            return

        # SQL-запит
        sql = f"UPDATE capex SET {', '.join(updates)} WHERE capex_id=?"
        params.append(capex_id)

        cursor.execute(sql, tuple(params))
        conn.commit()
        print(f"✅ Інвестицію ID {capex_id} успішно оновлено.")

    except sqlite3.Error as e:
        print(f"❌ Помилка оновлення інвестиції: {e}")
    finally:
        conn.close()


def delete_capex():
    """видаляє за capex_id."""
    print("\n--- ВИДАЛИТИ CAPEX ---")
    capex_id = input("Введіть ID інвестиції, яку потрібно видалити (capex_id): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM capex WHERE capex_id=?", (capex_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Інвестицію ID {capex_id} успішно видалено.")
        else:
            print(f"❌ Інвестицію з ID {capex_id} не знайдено.")

    except sqlite3.Error as e:
        print(f"❌ Помилка видалення інвестиції: {e}")
    finally:
        conn.close()
