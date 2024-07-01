import psycopg2
from psycopg2 import sql

# Database connection URL
DATABASE_URL = 'postgresql://Python_owner:5UyRYngoDIs1@ep-wild-sun-a55dt1ok.us-east-2.aws.neon.tech/Python?sslmode=require'

# Establishing the connection
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Define table name and the data to insert
table_name = 'user_details'
data = [
    {'name': 'Hariharan Dakshnamurthy','email': 'hariharan.dakshnamurthy@mallow-tech.com'},
    {'name': 'Portgas D Ace', 'email': 'PortgasDAce@yahoo.in'}
]

# Construct the INSERT INTO statement
insert_query = sql.SQL(
    "INSERT INTO {table} ({fields}) VALUES ({values})"
).format(
    table=sql.Identifier(table_name),
    fields=sql.SQL(', ').join(map(sql.Identifier, data[0].keys())),
    values=sql.SQL(', ').join(map(sql.Placeholder, data[0].keys()))
)

# Execute the query with the provided data
cur.executemany(insert_query, data)
conn.commit()

# Close the connection
cur.close()
conn.close()

print("Data inserted successfully.")
