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
#
#
#c = 1
#while c <= 10:
#    cursor.execute(" DELETE FROM Users WHERE id = ?", (c,))
#    c += 3
#cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT SUM(balance) FROM Users ")
all_balances = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(balance) FROM Users")
total_users = cursor.fetchone()[0]

print(all_balances / total_users)


connection.commit()
connection.close()