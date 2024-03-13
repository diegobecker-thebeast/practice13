import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('countries.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Prompt the user for age requirement (16 or 18)
age_input = input("Enter age requirement (16 or 18): ")
if age_input not in ['16', '18']:
    print("Invalid age requirement. Please enter either '16' or '18'.")
    exit()

# Fetch data from the table based on the user's age requirement
cur.execute("SELECT country_name FROM countries WHERE age=?", (age_input,))
rows = cur.fetchall()

# Display the countries
if rows:
    print(f"Countries with age requirement {age_input}:")
    for row in rows:
        print(row[0])
else:
    print("No countries found with the specified age requirement.")

# Close the connection
conn.close()