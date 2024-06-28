
import os
import psycopg2

# Load the environment variable
database_url = os.getenv('DATABASE_URL')
# Connect to the PostgreSQL database
conn = psycopg2.connect(database_url)
with conn.cursor() as cur:
    cur.execute("SELECT version()")
    print(cur.fetchone())
# Close the connection
conn.close()
