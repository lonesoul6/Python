import psycopg2

# Define your database connection parameters
db_params = {
    'dbname': 'your_dbname',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Execute a SQL query
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

except Exception as error:
    print(f"Error executing query: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")
