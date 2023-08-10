import sqlite3
connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    department_id INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

connection.commit()

cursor.execute("INSERT INTO departments (name) VALUES (?)", ('IT',))
cursor.execute("INSERT INTO departments (name) VALUES (?)", ('Finance',))
cursor.execute("INSERT INTO departments (name) VALUES (?)", ('HR',))

cursor.execute("INSERT INTO users (username, email, password, department_id) VALUES (?, ?, ?, ?)", ('john_doe', 'john@example.com', 'hashed_password_here', 1))
cursor.execute("INSERT INTO users (username, email, password, department_id) VALUES (?, ?, ?, ?)", ('jane_smith', 'jane@example.com', 'hashed_password_here', 2))
cursor.execute("INSERT INTO users (username, email, password, department_id) VALUES (?, ?, ?, ?)", ('bob_smith', 'bob@example.com', 'hashed_password_here', 3))

connection.commit()

cursor.execute('''SELECT users.id, users.username, users.email, departments.name
                  FROM users
                  JOIN departments ON users.department_id = departments.id''')

result = cursor.fetchall()
for row in result:
    user_id, username, email, department_name = row
    print(f"User ID: {user_id}, Username: {username}, Email: {email}, Department: {department_name}")

connection.close()
