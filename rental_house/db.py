import sqlite3

DATABASE_NAME = 'rental_db.sqlite'


def setup_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Створення таблиці clients (Клієнти)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        email VARCHAR(255) UNIQUE,
        country VARCHAR(255)
    )
    """)

    # Створення таблиці bookings (Бронювання)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        check_in DATE NOT NULL,
        check_out DATE NOT NULL,
        nights INTEGER,
        total_price DECIMAL(10, 2),
        FOREIGN KEY (customer_id) REFERENCES clients(customer_id)
    )
    """)

    # Створення таблиці opex (Операційні Витрати)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS opex (
        opex_id INTEGER PRIMARY KEY AUTOINCREMENT,
        opex_date DATE NOT NULL,
        category VARCHAR(255) NOT NULL, -- Електрика, Вода, Комісії, тощо.
        amount DECIMAL(10, 2) NOT NULL,
        notes VARCHAR(255)
    )
    """)

    # Створення таблиці capex (Капітальні Інвестиції)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS capex (
        capex_id INTEGER PRIMARY KEY AUTOINCREMENT,
        capex_date DATE NOT NULL,
        category VARCHAR(255) NOT NULL, -- Будівництво, Меблі, Техніка, тощо.
        amount DECIMAL(10, 2) NOT NULL,
        notes VARCHAR(255),
        is_depreciable BOOLEAN
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calendar  (
    date DATE NOT NULL,
    is_weekend BOOLEAN,
    is_high_season BOOLEAN
     )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pricing  (
    season VARCHAR(50),
    date_from DATE,
    date_to DATE,
    weekday_price DECIMAL(10, 2) NOT NULL,
    weekend_price DECIMAL(10, 2) NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("База даних та таблиці успішно створені.")


if __name__ == '__main__':
    setup_database()
