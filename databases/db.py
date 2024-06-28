import sqlite3

# Connect to the database
conn = sqlite3.connect('Python.db')  # Replace 'your_database.db' with your database file name

# Create a cursor object
cursor = conn.cursor()

# Create Table Command
create_table_command = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL UNIQUE
)
"""

# Define the new values and the condition for updating
values = ('hariharan', 24.00, 6)

# Execute the update command
cursor.execute(create_table_command)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
