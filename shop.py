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
        customer_id = cur.lastrowid
        
        print(f"Покупця додано! ID: ${customer_id}")

def add_product_price():
    try:
        price = float(input("Ціна: "))
    except ValueError:
        print("Некоректна ціна! Введіть корректну ціну")
        price = add_product_price()
    return price

def add_product():
    name = input("Назва товару: ")
    category = input("Категорія: ")
    price = add_product_price()

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO products(name, category, price) VALUES(?,?,?)",
                    (name, category, price))
        conn.commit()
        print("Товар додано!")

def get_customer_by_id(customer_id):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        row = cur.fetchone()
       
        return row

def get_product_by_id(product_id):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cur.fetchone()

        return row

def show_all_customers():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        print("\nВсі покупці:")
        for row in rows:
            print(f"ID: {row[0]}. Name: {row[1]}, Email: {row[2]}")

def show_all_products():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        print("\nВсі товари:")
        for row in rows:
            print(f"ID: {row[0]}. Name: {row[1]}, Category: {row[2]}, Price: {row[3]} грн")

def add_order_quantity():
    try:
        quantity = int(input("Кількість: "))
    except ValueError:
        print("Некоректна кількість! Введіть корректну кількість")
        quantity = add_order_quantity()
    
    return quantity

def add_order_customer_id():
    try:
        customer_id = int(input("ID покупця: "))

        customer = get_customer_by_id(customer_id)
        if customer:
            return customer_id
        else:
            print("Покупця не знайдено! Введіть корректний ID покупця")
            return add_order_customer_id()
    
    except ValueError:
        print("Некоректний ID покупця! Введіть корректний ID покупця")
        customer_id = add_order_customer_id()
    
    return customer_id


def add_order_product_id():
    try:
        product_id = input("ID товару (або \"stop\"): ")
        
        if str(product_id).lower() == "stop":
            return None
        
        product = get_product_by_id(int(product_id))
        
        if product:
            return product_id
        else:
            print("Товар не знайдено! Введіть корректний ID товару")
            return add_order_product_id()
    except ValueError:
        print("Некоректний ID товару! Введіть корректний ID товару")
        return add_order_product_id()

def create_order():
    customer_id = add_order_customer_id()

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO orders(customer_id, order_date) VALUES(?, ?)",
                    (customer_id, datetime.now()))
        order_id = cur.lastrowid
        print(f"Замовлення створене! ID: {order_id}")

        while True:
            product_id = add_order_product_id()

            if not product_id:
                break
            
            quantity = add_order_quantity()

            cur.execute("INSERT INTO order_items(order_id, product_id, quantity) VALUES(?,?,?)",
                        (order_id, int(product_id), quantity))

        conn.commit()
        print("Замовлення сформовано!")


def show_all_orders():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        print("\nВсі замовлення:")
        
        for row in rows:
            print(f"ID: {row[0]}, Customer ID: {row[1]}, Order Date: {row[2]}")


def show_total_order_cost():
    order_id = int(input("ID замовлення: "))

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT SUM(products.price * order_items.quantity)
                       FROM order_items 
                       INNER JOIN products ON products.id = order_items.product_id
                       WHERE order_id = ?''', (order_id,))

        total = cur.fetchone()[0]
        print(f"Загальна сума замовлення: {total if total else 0} грн")


def top_customers():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT customers.name,
                              SUM(products.price * order_items.quantity) AS total
                       FROM customers
                       INNER JOIN orders ON customers.id = orders.customer_id
                       INNER JOIN order_items ON orders.id = order_items.order_id
                       INNER JOIN products ON order_items.product_id = products.id
                       GROUP BY customers.id
                       ORDER BY total DESC
                       LIMIT 5''')

        rows = cur.fetchall()
        print("\nТоп клієнти:")
        for name, total in rows:
            print(f"{name}: {total} грн")


def category_stats():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()

        cur.execute('''SELECT category, SUM(price * quantity) AS revenue
                       FROM products
                       INNER JOIN order_items ON products.id = order_items.product_id
                       GROUP BY category
                       ORDER BY revenue DESC''')

        rows = cur.fetchall()
        print("\n Виторг по категоріях:")
        for category, revenue in rows:
            print(f"{category}: {revenue} грн")


def menu():
    print("\nМеню:")
    print("1 Додати покупця")
    print("2 Додати товар")
    print("3 Створити замовлення")
    print("4 Порахувати вартість замовлення")
    print("5 Топ клієнтів")
    print("6 Статистика по категоріях")
    print("7 Показати всіх покупців")
    print("8 Показати всі товари")
    print("9 Показати всі замовлення")
    print("0 Вихід")


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
        elif choice == "7": show_all_customers()
        elif choice == "8": show_all_products()
        elif choice == "9": show_all_orders()
        elif choice == "0":
            print("Вихід із програми")
            break
        else:
            print("Невідома команда!")


if __name__ == '__main__':
    main()
