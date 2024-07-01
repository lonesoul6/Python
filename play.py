import psycopg2
from psycopg2 import sql

# Database connection URL
DATABASE_URL = 'postgresql://Python_owner:5UyRYngoDIs1@ep-wild-sun-a55dt1ok.us-east-2.aws.neon.tech/Python?sslmode=require'

# Establishing the connection
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute(""" INSERT INTO user_details(name,email)
            VALUES ('Hariharan','hariharandakshnamurthy@gmail.com')""")

# Define table name and columns
table_name = 'user_details'
columns = {
    'id': 'SERIAL PRIMARY KEY',
    'name': 'VARCHAR(100)',
    'email': 'VARCHAR(100)',
    'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
}

# Construct the CREATE TABLE statement
create_table_query = sql.SQL(
    "CREATE TABLE {table} ({fields})"
).format(
    table=sql.Identifier(table_name),
    fields=sql.SQL(', ').join(
        sql.SQL('{} {}').format(sql.Identifier(col), sql.SQL(col_type))
        for col, col_type in columns.items()
    )
)

# # Execute the query
# cur.execute(create_table_query)
conn.commit()

# Close the connection
cur.close()
conn.close()

print(f"Details updated succesfully.")

# print(cur.fetchall())
