import sqlite3

# Connect to the database
conn = sqlite3.connect('Python.db')  # Make sure the path is correct

# Create a cursor object
cursor = conn.cursor()

# Check if the table exists
cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='users';")

# Fetch the result
table_exists = cursor.fetchone()

if table_exists:
    print("Table 'users' exists.")
else:
    print("Table 'users' does not exist.")

# Close the connection
conn.close()
