import mysql.connector

# Replace these with your MySQL server credentials
host = 'localhost'
user = 'root'
password = ''
database = 'new_database'  # The database you created in the previous step

# Connect to the MySQL server and select the database
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL server and selected database.")
    else:
        print("Failed to connect to MySQL server.")

    # Create a new table
    create_table_query = """
    CREATE TABLE employees (
        employee_id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE,
        hire_date DATE,
        salary DECIMAL(10, 2)
    )
    """

    cursor = connection.cursor()
    cursor.execute(create_table_query)
    print("Table 'employees' created successfully.")

    # Insert data into the table
    insert_data_query = """
    INSERT INTO employees (first_name, last_name, email, hire_date, salary)
    VALUES (%s, %s, %s, %s, %s)
    """

    # Sample data to be inserted
    employee_data = [
        ("John", "Doe", "john@example.com", "2023-08-07", 50000.00),
        ("Jane", "Smith", "jane@example.com", "2023-08-07", 60000.00)
        # Add more data rows as needed
    ]

    cursor.executemany(insert_data_query, employee_data)
    connection.commit()

    print("Data inserted successfully.")

except mysql.connector.Error as error:
    print("Error: ", error)

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
