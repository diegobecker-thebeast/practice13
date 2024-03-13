import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect(':memory:')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table for countries with 'age' and 'drinking_age_db' columns
cur.execute('''CREATE TABLE countries (
                id INTEGER PRIMARY KEY,
                country_name TEXT,
                age INTEGER,
                drinking_age_db INTEGER)''')

# Insert data into the table
countries = [
    ('USA', 18, 21),
    ('Canada', 16, 21),
    ('UK', 18, 21),
    ('Australia', 16, 21)
]
cur.executemany("INSERT INTO countries (country_name, age, drinking_age_db) VALUES (?, ?, ?)", countries)

# Prompt the user for the action they want to perform
action = input("What do you want to do? (Enter 'age' for age-based selection or 'drive' for driving age): ")

if action.lower() == 'age':
    # Prompt the user for age requirement (16 or 18)
    age_input = input("Enter age requirement (16 or 18): ")
    if age_input not in ['16', '18']:
        print("Invalid age requirement. Please enter either '16' or '18'.")
        exit()

    # Fetch data from the table based on the user's age requirement
    cur.execute("SELECT country_name FROM countries WHERE age=?", (age_input,))
    rows = cur.fetchall()

elif action.lower() == 'drive':
    # Prompt the user for their age
    user_age = int(input("How old are you? "))

    # Determine the driving age requirement based on the user's age
    if user_age >= 18:
        driving_age = 18
    elif user_age >= 16:
        driving_age = 16
    else:
        print("Invalid age")
        exit()

    # Fetch data from the table where driving age is equal to or less than the determined driving age
    cur.execute("SELECT country_name FROM countries WHERE age <= ?", (driving_age,))
    rows = cur.fetchall()

else:
    print("Invalid action. Please enter 'age' or 'drive'.")
    exit()

# Display the countries
if rows:
    print("Countries:")
    for row in rows:
        print(row[0])
else:
    print("No countries found.")

# Close the connection
conn.close()