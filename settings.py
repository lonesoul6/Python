# Add these at the top of your settings.py
from os import getenv
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Define your database connection parameters from environment variables
db_params = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': getenv('PGDATABASE'),
    'USER': getenv('PGUSER'),
    'PASSWORD': getenv('PGPASSWORD'),
    'HOST': getenv('PGHOST'),
    'PORT': getenv('PGPORT', 5432),
    'OPTIONS': {
      'sslmode': 'require',
    }
}}

# Append the endpoint ID option to the connection string
db_params['host'] += f'?options=endpoint%3D{os.getenv("ENDPOINT_ID")}'

# Connect to the database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    print("Connection to NeonDB established successfully!")
    
    # Execute a SQL query
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    
    # Print the results
    for row in rows:
        print(row)

except Exception as error:
    print(f"Error connecting to NeonDB: {error}")

# Close the connection
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")
