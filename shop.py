import sqlite3
from datetime import datetime

DB = "shop.db"



def init_db():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        category TEXT,
                        price REAL NOT NULL)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        order_date TEXT,
                        FOREIGN KEY(customer_id) REFERENCES customers(id))''')

        cur.execute('''CREATE TABLE IF NOT EXISTS order_items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER NOT NULL,
                        FOREIGN KEY(order_id) REFERENCES orders(id),
                        FOREIGN KEY(product_id) REFERENCES products(id))''')

        conn.commit()



def add_customer():
    name = input("Імʼя покупця: ")
    email = input("Email: ")

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO customers(name, email) VALUES(?,?)", (name, email))
        conn.commit()
        print(" Покупця додано!")


def add_product():
    name = input("Назва товару: ")
    category = input("Категорія: ")
    price = float(input("Ціна: "))

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO products(name, category, price) VALUES(?,?,?)",
                    (name, category, price))
        conn.commit()
        print(" Товар додано!")


def create_order():
    customer_id = int(input("ID покупця: "))

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO orders(customer_id, order_date) VALUES(?, ?)",
                    (customer_id, datetime.now()))
        order_id = cur.lastrowid
        print(f"Замовлення створене! ID: {order_id}")

        while True:
            product_id = input("ID товару (або \"stop\"): ")
            if product_id.lower() == "stop":
                break
            quantity = int(input("Кількість: "))

            cur.execute("INSERT INTO order_items(order_id, product_id, quantity) VALUES(?,?,?)",
                        (order_id, int(product_id), quantity))

        conn.commit()
        print(" Замовлення сформовано!")


def show_total_order_cost():
    order_id = int(input("ID замовлення: "))

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT SUM(products.price * order_items.quantity)
                       FROM order_items 
                       JOIN products ON products.id = order_items.product_id
                       WHERE order_id = ?''', (order_id,))

        total = cur.fetchone()[0]
        print(f" Загальна сума замовлення: {total if total else 0} грн")


def top_customers():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT customers.name,
                              SUM(products.price * order_items.quantity) AS total
                       FROM customers
                       JOIN orders ON customers.id = orders.customer_id
                       JOIN order_items ON orders.id = order_items.order_id
                       JOIN products ON order_items.product_id = products.id
                       GROUP BY customers.id
                       ORDER BY total DESC
                       LIMIT 5''')

        rows = cur.fetchall()
        print("\n Топ клієнти:")
        for name, total in rows:
            print(f"{name}: {total} грн")


def category_stats():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT category, SUM(price * quantity) AS revenue
                       FROM products
                       JOIN order_items ON products.id = order_items.product_id
                       GROUP BY category
                       ORDER BY revenue DESC''')

        rows = cur.fetchall()
        print("\n Виторг по категоріях:")
        for category, revenue in rows:
            print(f"{category}: {revenue} грн")


# ----------- ІНТЕРФЕЙС ВИКЛИКУ ------------ #
def menu():
    print("\n Меню:")
    print("1 → Додати покупця")
    print("2 → Додати товар")
    print("3 → Створити замовлення")
    print("4 → Порахувати вартість замовлення")
    print("5 → Топ клієнтів")
    print("6 → Статистика по категоріях")
    print("0 → Вихід")


def main():
    init_db()

    while True:
        menu()
        choice = input("Оберіть дію: ")

        if choice == "1": add_customer()
        elif choice == "2": add_product()
        elif choice == "3": create_order()
        elif choice == "4": show_total_order_cost()
        elif choice == "5": top_customers()
        elif choice == "6": category_stats()
        elif choice == "0":
            print("Вихід із програми")
            break
        else:
            print("Невідома команда!")


if __name__ == '__main__':
    main()
