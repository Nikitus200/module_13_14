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
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
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



def add_user(username, email, age):
    connect = sql3.connect("datebase.db")
    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', '1000')")
    connect.commit()
    connect.close()

def is_included(username):
    connect = sql3.connect("datebase.db")
    cursor = connect.cursor()
    result = cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
    if result.fetchone() is None:
        return False
    else:
        return True
    connect.commit()
    connect.close()


if __name__ == "__main__":
    connect.close()