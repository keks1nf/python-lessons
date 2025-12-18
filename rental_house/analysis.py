import calendar
import locale
import sqlite3
from datetime import datetime
from datetime import timedelta

import pandas as pd

# коректне форматування чисел
try:
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'Ukrainian_Ukraine.1251')
    except locale.Error:
        print("Помилка. Форматування чисел може бути некоректним.")

##todo вынести в отдельный класс и вызывать это
DATABASE_NAME = 'rental_db.sqlite'
DATE_FORMAT = '%Y-%m-%d'


# --- ДОПОМІЖНІ ФУНКЦІЇ ---


##todo вынести в отдельный класс и вызывать это, вместе с DATABASE_NAME
def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)

##todo вынести в отдельный класс и вызывать это, вместе с DATABASE_NAME
def get_current_value(conn, table, column, pk_value, pk_column):
    """отримує поточне значення стовпця для відображення в меню оновлення"""
    cursor = conn.cursor()
    cursor.execute(f"SELECT {column} FROM {table} WHERE {pk_column}=?", (pk_value,))
    result = cursor.fetchone()
    return result[0] if result is not None and result[0] is not None else 'N/A'


def get_period_dates():
    """дати початку та кінця періоду для аналітики"""
    print("\n--- ВИБІР ПЕРІОДУ ---")

    # поточний рік
    current_year = datetime.now().year
    default_start = f"{current_year}-01-01"
    default_end = f"{current_year}-12-31"

    start_date = input(f"Введіть дату початку (YYYY-MM-DD, за замовчуванням {default_start}): ") or default_start
    end_date = input(f"Введіть дату кінця (YYYY-MM-DD, за замовчуванням {default_end}): ") or default_end

    try:
        # Перевірка коректності дат
        datetime.strptime(start_date, DATE_FORMAT)
        datetime.strptime(end_date, DATE_FORMAT)
        return start_date, end_date
    except ValueError:
        print("❌ Некоректний формат дати. Використовуйте YYYY-MM-DD.")
        return None, None


def format_currency(amount):
    """форматує число як валюту"""
    return locale.format_string("%.2f", amount, grouping=True).replace(',', ' ').replace('.', ',')


def check_customer_exists(customer_id):
    """чи існує клієнт з даним ID (bookings)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM clients WHERE customer_id=?", (customer_id,))
        return cursor.fetchone() is not None
    finally:
        conn.close()

#todo убрать логику if table_name == 'capex' and 'is_depreciable' in column_names:
def get_all_records(table_name):
    """виводить всі записи з вказаної таблиці."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")

        column_names = [description[0] for description in cursor.description]
        print(f"\n--- ВСІ ЗАПИСИ З ТАБЛИЦІ '{table_name}' ---")
        print(" | ".join(column_names))
        print("-" * (sum(len(name) for name in column_names) + 3 * len(column_names)))

        records = cursor.fetchall()
        for record in records:
            display_record = list(record)
            if table_name == 'capex' and 'is_depreciable' in column_names:
                depreciable_index = column_names.index('is_depreciable')
                if len(display_record) > depreciable_index:
                    val = display_record[depreciable_index]
                    display_record[depreciable_index] = 'Так' if val == 1 else 'Ні'

            print(" | ".join(map(lambda x: str(x) if x is not None else 'NULL', display_record)))

    except sqlite3.OperationalError as e:
        print(
            f"❌ Помилка: Не вдалося виконати запит до таблиці {table_name}. Можливо, таблиця порожня або не існує. {e}")
    finally:
        conn.close()


def calculate_nights_in_period(start_date_str, end_date_str):
    """обчислює загальну кількість ночей (днів)"""
    try:
        dt_start = datetime.strptime(start_date_str, DATE_FORMAT).date()
        dt_end = datetime.strptime(end_date_str, DATE_FORMAT).date()
        return (dt_end - dt_start).days
    except ValueError:
        return 0


# --- 1. АНАЛІТИКА  ---

def calculate_occupancy_rate_single_unit(start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # загальна доступна кількість ночей
        total_available_nights = calculate_nights_in_period(start_date, end_date)

        if total_available_nights <= 0:
            print("❌ Помилка: Некоректний період для розрахунку.")
            return

        # бронювання, що перетинаються з періодом
        cursor.execute("""
            SELECT check_in, check_out 
            FROM bookings 
            WHERE check_out > ? AND check_in <= ?
        """, (start_date, end_date))
        bookings = cursor.fetchall()

        if not bookings:
            total_booked_nights = 0
            occupancy_rate = 0.0
        else:
            # унікальні зайняті ночі
            booked_dates = set()
            start_dt = datetime.strptime(start_date, DATE_FORMAT).date()
            end_dt = datetime.strptime(end_date, DATE_FORMAT).date()

            for check_in_str, check_out_str in bookings:
                try:
                    check_in = datetime.strptime(check_in_str, DATE_FORMAT).date()
                    check_out = datetime.strptime(check_out_str, DATE_FORMAT).date()
                except ValueError:
                    continue  # пропускаємо некоректні дати

                # ітерація по ночах
                current_date = max(check_in, start_dt)

                while current_date < check_out and current_date < end_dt:
                    # додаємо цю ніч (uniquely booked dates)
                    booked_dates.add(current_date)
                    current_date += timedelta(days=1)

            total_booked_nights = len(booked_dates)
            occupancy_rate = (total_booked_nights / total_available_nights) * 100

        # розрахунок ADR для зайнятих ночей у періоді
        cursor.execute("""
            SELECT COALESCE(SUM(total_price), 0), COALESCE(SUM(nights), 0)
            FROM bookings 
            WHERE check_out > ? AND check_in < ?
        """, (start_date, end_date))
        total_revenue, total_sum_nights = cursor.fetchone()

        # використовуємо коректні заброньовані ночі, якщо вони є.
        adr = total_revenue / total_sum_nights if total_sum_nights > 0 else 0

        print("\n=============================================")
        print(f"📈 ЗВІТ ПРО ЗАПОВНЮВАНІСТЬ за {start_date} до {end_date}")
        print(f"=============================================")
        print(f"📅 Загальна доступна кількість ночей: {total_available_nights}")
        print(f"   КОРИГУВАНА кількість зайнятих ночей: {total_booked_nights}")
        print("---------------------------------------------")

        # овербукінг
        if total_booked_nights > total_available_nights:
            print("❗❗ ОВЕРБУКІНГ ❗❗")
            print(f"Зайняті ночі ({total_booked_nights}) > Доступні ночі ({total_available_nights}).")

        print(f"🟢 РІВЕНЬ ЗАПОВНЮВАНОСТІ (Occupancy Rate): {occupancy_rate:,.2f}%")
        print("=============================================")
        print(f"💵 Середня ціна ночі (ADR): {adr:,.2f} UAH")

    except sqlite3.Error as e:
        print(f"❌ Помилка виконання запиту заповнюваності: {e}")
    finally:
        conn.close()


def calculate_financial_summary_full(start_date, end_date):
    """ фінансовий звіт, податки (3-я група)"""
    conn = get_db_connection()
    cursor = conn.cursor()

    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d') # вынести в константу '%Y-%m-%d'
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # константи для розрахунку податків (2024 рік, 3-я група)

    EP_RATE = 0.05  # Єдиний Податок 5%
    # MIN_ZARPLATA_2024 = 8000.00  # Мінімальна ЗП
    # ESV_RATE = 0.22  # ЄСВ 22%
    # ESV_MONTHLY = MIN_ZARPLATA_2024 * ESV_RATE
    # ESV_ANNUAL = ESV_MONTHLY * 12

    total_esv = 0
    current_date = start_date
    #todo расчет есв вынести в отдельную функцию
    while current_date <= end_date:
        if current_date.year == 2024 and current_date.month < 4:
            min_zp = 7100
        else:
            min_zp = 8000

        total_esv += min_zp * 0.22

        # переходимо до наступного місяця
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)

    ESV_ANNUAL = total_esv

    try:
        # 1. збір даних
        cursor.execute("SELECT COALESCE(SUM(total_price), 0) FROM bookings WHERE check_in >= ? AND check_out <= ?",
                       (start_date, end_date))
        total_revenue = cursor.fetchone()[0]

        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM opex WHERE opex_date BETWEEN ? AND ?",
                       (start_date, end_date))
        total_opex = cursor.fetchone()[0]

        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM capex WHERE capex_date BETWEEN ? AND ?",
                       (start_date, end_date))
        total_capex = cursor.fetchone()[0]

        # 2. розрахунок податків
        taxes_ep = total_revenue * EP_RATE
        taxes_esv = ESV_ANNUAL
        total_taxes = taxes_ep + taxes_esv

        # 3. розрахунок прибутку
        # дохід - операційні витрати
        profit_before_taxes = total_revenue - total_opex

        # чистий прибуток,
        # прибуток - Податки
        net_profit = profit_before_taxes - total_taxes

        profit_margin = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0

        # 4. звіт
        print(f"\n========================================================")
        print(f"💰  ФІНАНСОВИЙ ЗВІТ (ФОП 3-я група) за {start_date} до {end_date}")
        print(f"========================================================")

        print(f"I. ДОХОДИ (REVENUE)")
        print(f"--------------------------------------------------------")
        print(f"💰 Загальний Дохід (Revenue):  {format_currency(total_revenue)} UAH")
        print(f"")

        print(f"II. ВИТРАТИ (OPEX & CAPEX)")
        print(f"--------------------------------------------------------")
        print(f"📉 Операційні Витрати (OPEX):  {format_currency(total_opex)} UAH")
        print(f"🛠️ Капітальні Інвестиції (CAPEX): {format_currency(total_capex)} UAH")
        print(f"")

        print(f"III. ПОДАТКОВІ ЗОБОВ'ЯЗАННЯ (TAXES)")
        print(f"--------------------------------------------------------")
        print(f"❗ Єдиний Податок (5% від Revenue):  {format_currency(taxes_ep)} UAH")
        print(f"❗️ ЄСВ (Єдиний Соц. Внесок, 12 міс.): {format_currency(taxes_esv)} UAH")
        print(f"❗ УСЬОГО ПОДАТКІВ ДО СПЛАТИ: {format_currency(total_taxes)} UAH")
        print(f"")

        print(f"IV. ПРИБУТОК (PROFITABILITY)")
        print(f"--------------------------------------------------------")
        print(f"💰 Прибуток до Податків:      {format_currency(profit_before_taxes)} UAH")
        print(f"🟢 ЧИСТИЙ ПРИБУТОК (NET PROFIT): {format_currency(net_profit)} UAH")
        print(f"📉 Маржа Чистого Прибутку: {profit_margin:.2f}%")
        print(f"========================================================")

    except sqlite3.Error as e:
        print(f"❌ Помилка виконання аналітичного запиту: {e}")
    finally:
        conn.close()


def report_opex_by_category(start_date, end_date):
    """ звіт про операційні витрати (по категоріях)"""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT category, COALESCE(SUM(amount), 0) as total_amount
            FROM opex 
            WHERE opex_date BETWEEN ? AND ?
            GROUP BY category
            ORDER BY total_amount DESC
        """, (start_date, end_date))

        results = cursor.fetchall()

        print(f"\n--- OPEX ЗА КАТЕГОРІЯМИ ({start_date} до {end_date}) ---")
        if not results:
            print("Немає операційних витрат за вказаний період.")
            return

        print(f"{'Категорія':<15} | {'Сума, UAH':>15}")
        print("-" * 33)

        for category, amount in results:
            print(f"{category:<15} | {amount:15,.2f}")

    except sqlite3.Error as e:
        print(f"❌ Помилка створення звіту OPEX: {e}")
    finally:
        conn.close()


def display_monthly_occupancy():
    """завантаженість у % по місяцях"""
    try:
        year_input = int(input('Введіть рік для формування звіту (наприклад, 2024): '))

        df = pd.read_csv('bookings.csv')

        # datetime
        df['check_in'] = pd.to_datetime(df['check_in'])
        df['check_out'] = pd.to_datetime(df['check_out'])

        all_nights = []

        # кожне бронювання на окремі ночі
        for _, row in df.iterrows():
            #  від check_in до check_out
            nights = pd.date_range(start=row['check_in'], end=row['check_out'] - pd.Timedelta(days=1))
            all_nights.extend(nights)

        #  датафрейм з заброньованих ночей
        nights_df = pd.DataFrame({'date': all_nights})

        # групуємо за місяцями
        monthly_counts = nights_df[nights_df['date'].dt.year == year_input]['date'].dt.month.value_counts().sort_index()

        print(f"\n--- ЗВІТ ЗАВАНТАЖЕНОСТІ НА {year_input} РІК ---")
        print(f"{'Місяць':<12} | {'Зайнято':<8} | {'Всього':<7} | {'Завантаженість'}")
        print("-" * 55)

        for month in range(1, 13):
            #  днів у місяці
            days_in_month = calendar.monthrange(year_input, month)[1]
            #  ночей заброньовано
            booked_nights = monthly_counts.get(month, 0)
            # % завантаженості
            occupancy_rate = (booked_nights / days_in_month) * 100

            month_name = calendar.month_name[month]
            print(f"{month_name:<12} | {booked_nights:<8} | {days_in_month:<7} | {occupancy_rate:>6.1f}%")

    except Exception as e:
        print(f"Помилка при розрахунку завантаженості: {e}")


def display_full_seasonality_report():
    """ звіт: Місяць, Дохід, Витрати, Прибуток, Завантаженість"""
    try:
        # 1. доходи та розрахунок ночей
        df = pd.read_csv('bookings.csv')
        df['check_in'] = pd.to_datetime(df['check_in'])
        df['check_out'] = pd.to_datetime(df['check_out'])

        # збір даних за 12 місяців
        monthly_data = {m: {'revenue': 0, 'nights': 0, 'opex': 0} for m in range(1, 13)}
        report_year = int(input("Введіть рік, для формування звіту (наприклад, 2024):  "))

        # дохід та ночі по місяцях
        for _, row in df.iterrows():
            nights_range = pd.date_range(start=row['check_in'], end=row['check_out'] - pd.Timedelta(days=1))
            revenue_per_night = row['total_price'] / len(nights_range)

            for day in nights_range:
                if day.year == report_year:
                    monthly_data[day.month]['nights'] += 1
                    monthly_data[day.month]['revenue'] += revenue_per_night

        # 2. OPEX
        conn = sqlite3.connect('rental_db.sqlite')
        opex_df = pd.read_sql_query("SELECT amount, opex_date FROM opex", conn)
        opex_df['opex_date'] = pd.to_datetime(opex_df['opex_date'])
        conn.close()

        for _, row in opex_df.iterrows():
            if row['opex_date'].year == report_year:
                monthly_data[row['opex_date'].month]['opex'] += row['amount']

        # 3. звіт
        print(f"\n{f' ЗВІТ ПО СЕЗОННОСТІ ЗА {report_year} РІК':^70}")
        print("-" * 85)
        print(f"{'Місяць':<12} | {'Дохід':<12} | {'Витрати*':<12} | {'Прибуток':<12} | {'Завант.'}")
        print("-" * 85)

        ukr_months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
                      "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]

        for m in range(1, 13):
            rev = monthly_data[m]['revenue']
            # податки (5% ЄП + ЄСВ 1760 грн/міс)
            taxes = (rev * 0.05) + 1760
            exp = monthly_data[m]['opex'] + taxes
            profit = rev - exp

            days_in_month = calendar.monthrange(report_year, m)[1]
            occ = (monthly_data[m]['nights'] / days_in_month) * 100

            print(f"{ukr_months[m - 1]:<12} | {rev:>10.0f} | {exp:>10.0f} | {profit:>10.0f} | {occ:>6.1f}%")

        print("-" * 85)
        print("*Витрати включають: OPEX + Єдиний податок (5%) + ЄСВ")

    except Exception as e:
        print(f"Помилка створення звіту: {e}")


def display_available_days_report():
    """Звіт про вільні дні по місяцях"""
    try:
        year_input = input('Введіть рік для аналізу вільних днів (наприклад, 2024): ')
        report_year = int(year_input)

        df = pd.read_csv('bookings.csv')
        df['check_in'] = pd.to_datetime(df['check_in'])
        df['check_out'] = pd.to_datetime(df['check_out'])

        # всі заброньовані ночі в набір (set) для пошуку
        booked_nights = set()
        for _, row in df.iterrows():
            nights = pd.date_range(start=row['check_in'], end=row['check_out'] - pd.Timedelta(days=1))
            for night in nights:
                if night.year == report_year:
                    booked_nights.add(night.date())

        # 3. звіт
        print(f"\n{'━' * 60}")
        print(f"{f'🗓️ ЗВІТ ПРО ВІЛЬНІ ДНІ ЗА {report_year} РІК':^60}")
        print(f"{'━' * 60}")
        print(f"{'Місяць':<15} | {'Всього днів':<12} | {'Вільні дні':<12} | {'Вільні %'}")
        print("-" * 60)

        ukr_months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
                      "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]

        total_available_in_year = 0

        for m in range(1, 13):
            days_in_month = calendar.monthrange(report_year, m)[1]
            free_days_list = []

            for d in range(1, days_in_month + 1):
                current_date = datetime(report_year, m, d).date()
                if current_date not in booked_nights:
                    free_days_list.append(d)

            free_count = len(free_days_list)
            total_available_in_year += free_count
            free_percent = (free_count / days_in_month) * 100

            # Формуємо рядок з номерами днів (якщо їх небагато)
            days_str = ", ".join(map(str, free_days_list[:10])) + ("..." if free_count > 10 else "")

            print(f"{ukr_months[m - 1]:<15} | {days_in_month:>11} | {free_count:>11} | {free_percent:>7.1f}%")
            if free_count > 0:
                print(f"   ∟ Вільні числа: {days_str}")

        print("-" * 60)
        print(f"ЗАГАЛОМ ВІЛЬНИХ НОЧЕЙ ЗА РІК: {total_available_in_year}")
        print(f"{'━' * 60}")

    except ValueError:
        print("❌ Помилка: Введіть рік числом.")
    except Exception as e:
        print(f"❌ Помилка при розрахунку вільних днів: {e}")
