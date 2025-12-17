import sqlite3

DATABASE_NAME = 'rental_db.sqlite'


# --- Базові операції з БД ---
def execute_query(query, params=(), fetch_one=False, fetch_all=False):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        if fetch_one:
            return cursor.fetchone()
        if fetch_all:
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Помилка бази даних: {e}")
        return None
    finally:
        conn.close()


# --- CUSTOMERS ---

def add_client(name, phone, email, country):
    query = "INSERT INTO clients (name, phone, email, country) VALUES (?, ?, ?, ?)"
    return execute_query(query, (name, phone, email, country))


def get_client(client_id):
    query = "SELECT * FROM clients WHERE customer_id = ?"
    return execute_query(query, (client_id,), fetch_one=True)


def update_client(client_id, name, phone, email, country):
    query = "UPDATE clients SET name = ?,  phone = ?, email = ?, country = ? WHERE customer_id = ?"
    return execute_query(query, (name, phone, email, country, client_id))


def delete_client(client_id):
    query = "DELETE FROM clients WHERE customer_id = ?"
    return execute_query(query, (client_id,))


# --- BOOKINGS ---

def add_booking(customer_id, check_in, check_out, nights, total_price):
    query = "INSERT INTO bookings (customer_id, check_in, check_out, nights, total_price) VALUES (?, ?, ?, ?, ?)"
    return execute_query(query, (customer_id, check_in, check_out, nights, total_price))


def get_booking(booking_id):
    query = "SELECT * FROM bookings WHERE booking_id = ?"
    return execute_query(query, (booking_id,), fetch_one=True)


def update_booking(booking_id, check_in, check_out, total_price, rejected=False, rejection_date=None):
    query = "UPDATE bookings SET check_in = ?, check_out = ?, total_price = ?, rejected = ?, rejection_date = ? WHERE booking_id = ?"
    return execute_query(query, (check_in, check_out, total_price, rejected, rejection_date, booking_id))


def delete_booking(booking_id):
    query = "DELETE FROM bookings WHERE booking_id = ?"
    return execute_query(query, (booking_id,))


# --- OPEX ---

def add_opex(opex_date, category, amount, notes=""):
    query = "INSERT INTO opex (opex_date, category, amount, notes) VALUES (?, ?, ?, ?)"
    return execute_query(query, (opex_date, category, amount, notes))


def get_opex(opex_id):
    query = "SELECT * FROM opex WHERE opex_id = ?"
    return execute_query(query, (opex_id,), fetch_one=True)


def update_opex(opex_id, opex_date, category, amount, notes=""):
    query = "UPDATE opex SET opex_date = ?, category = ?, amount = ?, notes = ? WHERE opex_id = ?"
    return execute_query(query, (opex_date, category, amount, notes, opex_id))


def delete_opex(opex_id):
    query = "DELETE FROM opex WHERE opex_id = ?"
    return execute_query(query, (opex_id,))


# --- IV. КАПІТАЛЬНІ ІНВЕСТИЦІЇ (CAPEX) ---

def add_capex(capex_date, category, amount, notes="", is_depreciable=True):
    query = "INSERT INTO capex (capex_date, category, amount, notes, is_depreciable) VALUES (?, ?, ?, ?, ?)"
    return execute_query(query, (capex_date, category, amount, notes, is_depreciable))


def get_capex(capex_id):
    query = "SELECT * FROM capex WHERE capex_id = ?"
    return execute_query(query, (capex_id,), fetch_one=True)


def update_capex(capex_id, capex_date, category, amount, notes="", is_depreciable=True):
    query = "UPDATE capex SET capex_date = ?, category = ?, amount = ?, notes = ?, is_depreciable = ? WHERE capex_id = ?"
    return execute_query(query, (capex_date, category, amount, notes, is_depreciable, capex_id))


def delete_capex(capex_id):
    query = "DELETE FROM capex WHERE capex_id = ?"
    return execute_query(query, (capex_id,))


# --- ДОДАТКОВА ФУНКЦІЯ ПЕРЕГЛЯДУ ---
def get_all_records(table_name):
    query = f"SELECT * FROM {table_name}"
    return execute_query(query, fetch_all=True)


'''
booking_df = pd.read_csv('bookings.csv')

print(booking_df.info())

booking_df['check_in'] = pd.to_datetime(booking_df['check_in'], format='%Y-%m-%d')
booking_df['check_out'] = pd.to_datetime(booking_df['check_out'], format='%Y-%m-%d')
print(booking_df.info())

calendar_df = pd.read_csv('calendar.csv')

print(calendar_df.info())
'''
