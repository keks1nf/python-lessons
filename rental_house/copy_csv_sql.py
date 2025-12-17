import os
import sqlite3

import pandas as pd

DATABASE_NAME = 'rental_db.sqlite'

# 'Ім'я файлу' : 'Назва SQL-таблиці'
CSV_TO_TABLE_MAP = {
    'clients.csv': 'clients',
    'bookings.csv': 'bookings',
    'opex.csv': 'opex',
    'capex.csv': 'capex',
    'pricing.csv': 'pricing',
    'calendar.csv': 'calendar'
}


def import_all_csv_to_sqlite():
    """Імпортує дані з CSV-файлів у відповідні SQL-таблиці"""
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
                df = pd.read_csv(file_path, dtype={'amount': float})

                # --- ОЧИЩЕННЯ СТОВПЦІВ ---
                df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df.columns = df.columns.str.strip()  # Видаляємо пробіли

                if table_name == 'opex':
                    required_cols = ['opex_id', 'opex_date', 'category', 'amount', 'notes']
                    df = df[required_cols]
                    print("   (Проведено обробку: Забезпечено коректний порядок стовпців для opex)")

                elif table_name == 'capex':
                    required_cols = ['capex_id', 'capex_date', 'category', 'amount', 'notes', 'is_depreciable']
                    df = df[required_cols]
                    print("   (Проведено обробку: Забезпечено коректний порядок стовпців для capex)")

                # 3. Запис даних у SQL-таблицю
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
