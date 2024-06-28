import psycopg2

# Define your database connection parameters
db_params = {
    'dbname': 'your_dbname',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

# Connect to the database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    print("Connection to NeonDB established successfully!")
    
    # You can now execute SQL queries using cursor.execute()
    # Example: cursor.execute("SELECT * FROM your_table")

except Exception as error:
    print(f"Error connecting to NeonDB: {error}")

# Close the connection
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")
