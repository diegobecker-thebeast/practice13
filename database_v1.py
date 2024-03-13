import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('countries.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Drop the existing 'countries' table (if it exists)
cur.execute('''DROP TABLE IF EXISTS countries''')

# Create a table for countries with an additional 'age' column
cur.execute('''CREATE TABLE countries (
                id INTEGER PRIMARY KEY,
                country_name TEXT,
                age INTEGER)''')

# Commit the transaction
conn.commit()

# Insert data into the table with age 18 or 16
countries = [
    ('USA', 18),
    ('Canada', 16),
    ('UK', 18),
    ('Australia', 16)
]
cur.executemany("INSERT INTO countries (country_name, age) VALUES (?, ?)", countries)

# Commit the transaction
conn.commit()

# Fetch data from the table
cur.execute("SELECT * FROM countries")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()