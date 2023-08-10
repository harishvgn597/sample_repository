import sqlite3
connection = sqlite3.connect('database.db')

cursor = connection.cursor()

username=input('enter username ')
email=input('enter email ')
password=input('enter password ')
department=input('enter dept id ')

cursor.execute("INSERT INTO users (username, email, password, department_id) VALUES (?, ?, ?, ?)", (username, email, password, department))

connection.commit()

print('inserted ')

connection.close()