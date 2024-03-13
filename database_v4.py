import sqlite3
import tkinter as tk
from tkinter import messagebox

def get_countries():
    # Connect to the in-memory database
    conn = sqlite3.connect(':memory:')
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

    # Fetch data from the table based on the user's input
    action = action_var.get()
    if action == 'age':
        age_input = age_entry.get()
        if age_input not in ['16', '18']:
            messagebox.showerror("Error", "Invalid age requirement. Please enter either '16' or '18'.")
            return

        cur.execute("SELECT country_name FROM countries WHERE age=?", (age_input,))
    elif action == 'drive':
        user_age = int(user_age_entry.get())
        if user_age < 16:
            messagebox.showerror("Error", "Invalid age. Driving age is only for 16 or 18.")
            return

        driving_age = 18 if user_age >= 18 else 16
        cur.execute("SELECT country_name FROM countries WHERE age <= ?", (driving_age,))
    else:
        messagebox.showerror("Error", "Invalid action. Please enter 'age' or 'drive'.")
        return

    rows = cur.fetchall()

    # Close the connection
    conn.close()

    # Display the countries
    if rows:
        country_list = "\n".join([row[0] for row in rows])
        messagebox.showinfo("Countries", f"Countries:\n{country_list}")
    else:
        messagebox.showinfo("Countries", "No countries found.")

# Create a tkinter window
root = tk.Tk()
root.title("Country Selection")

# Action selection
action_var = tk.StringVar(value="")
action_label = tk.Label(root, text="Select action:")
action_label.grid(row=0, column=0, padx=5, pady=5)
action_option_menu = tk.OptionMenu(root, action_var, "drive")
action_option_menu.grid(row=0, column=1, padx=5, pady=5)

# User age input (for 'drive' action)
user_age_label = tk.Label(root, text="Enter your age:")
user_age_label.grid(row=2, column=0, padx=5, pady=5)
user_age_entry = tk.Entry(root)
user_age_entry.grid(row=2, column=1, padx=5, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_countries)
submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the tkinter event loop
root.mainloop()