import os
import sqlite3

import pandas as pd

DATABASE_NAME = 'rental_db.sqlite'

# Словник відповідності: 'Ім'я файлу' : 'Назва SQL-таблиці'
CSV_TO_TABLE_MAP = {
    'clients.csv': 'clients',
    'bookings.csv': 'bookings',
    'opex.csv': 'opex',
    'capex.csv': 'capex',
    'pricing.csv': 'pricing',
    'calendar.csv': 'calendar'
}


def import_all_csv_to_sqlite():
    """Імпортує дані з CSV-файлів у відповідні SQL-таблиці з попередньою обробкою."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        print(f"Підключено до бази даних: {DATABASE_NAME}")

        for file_path, table_name in CSV_TO_TABLE_MAP.items():

            if not os.path.exists(file_path):
                print(f"⚠️ Файл не знайдено: {file_path}. Пропускаємо.")
                continue

            print(f"\n---> Обробка файлу: {file_path} -> Таблиця: {table_name}")

            try:
                # Читання CSV. Використовуємо dtype={'amount': float} для запобігання помилок формату.
                df = pd.read_csv(file_path, dtype={'amount': float})

                # --- УНІВЕРСАЛЬНА ПЕРЕОБРОБКА (ОЧИЩЕННЯ СТОВПЦІВ) ---
                # Видаляємо неназвані стовпці, які часто з'являються через зайві коми
                df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df.columns = df.columns.str.strip()  # Видаляємо пробіли з назв стовпців

                # --- СПЕЦІАЛІЗОВАНА ПЕРЕОБРОБКА ---

                if table_name == 'opex':
                    # Згідно з вашою схемою (db_setup), таблиця 'opex' має стовпці:
                    # opex_id, opex_date, category, amount.
                    # Файл 'opex.csv' має стовпці: opex_id, opex_date, category, amount, notes.
                    # Ми залишаємо лише перші 4 стовпці.
                    required_cols = ['opex_id', 'opex_date', 'category', 'amount']
                    df = df[required_cols]
                    print("   (Проведено обробку: Видалено стовпець 'notes' для відповідності SQL-схемі)")

                elif table_name == 'capex':
                    # Згідно з вашою схемою, таблиця 'capex' має 5 стовпців.
                    # Файл 'capex.csv' має: capex_id, capex_date, category, amount, notes, is_depreciable. (6 стовпців)
                    # Ми вибираємо стовпці, що відповідають SQL-схемі (включаючи notes та is_depreciable)
                    required_cols = ['capex_id', 'capex_date', 'category', 'amount', 'notes', 'is_depreciable']
                    df = df[required_cols]
                    print("   (Проведено обробку: Забезпечено коректний порядок стовпців для capex)")

                # 3. Запис даних у SQL-таблицю
                # 'replace' - видаляє старі дані та вставляє нові (чистий імпорт)
                df.to_sql(table_name, conn, if_exists='replace', index=False)

                print(f"✅ Успішно імпортовано {len(df)} рядків у таблицю '{table_name}'.")

            except Exception as e:
                print(f"❌ ПОМИЛКА ІМПОРТУ ДЛЯ ТАБЛИЦІ '{table_name}' з файлу '{file_path}': {e}")
                print(f"   Деталі помилки: {e}")
                print(
                    f"   Стовпці у DataFrame: {df.columns.tolist() if 'df' in locals() else 'Не вдалося прочитати CSV'}")

    finally:
        if conn:
            conn.close()
            print("\nВідключено від бази даних. Спробу імпорту завершено.")


if __name__ == '__main__':
    import_all_csv_to_sqlite()
