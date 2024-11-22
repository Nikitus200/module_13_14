import sqlite3 as sql3


connect = sql3.connect("datebase.db")
cursor = connect.cursor()


def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    """)
    connect.commit()

def get_all_products():
    connect = sql3.connect("datebase.db")
    cursor = connect.cursor()
    cursor.execute("""
    SELECT title, description, price FROM Products
    """)
    result = cursor.fetchall()
    connect.commit()
    connect.close()
    return result
def add_products(title, description, price):
    cursor.execute(f"INSERT INTO Products (title, description, price) VALUES ('{title}', '{description}', '{price}')")
    connect.commit()
if __name__ == "__main__":
    connect.close()