import sqlite3 as sql3

connection = sql3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS  Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")



#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",
#                                                                                             f"example{i}@gmail.com", f"{10 * i}", "1000"))

#for i in range(1, 11):
#    if i % 2 == 1:
#        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))


#c = 1
#while c <= 10:
#    cursor.execute(" DELETE FROM Users WHERE id = ?", (c,))
#    c += 3

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


connection.commit()
connection.close()