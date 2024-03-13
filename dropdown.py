import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit():
    selected_options = []
    for key, value in checkboxes.items():
        if value.get() == 1:
            selected_options.append(key)
    dropdown_selection = dropdown.get()

    if not selected_options:
        messagebox.showerror("Error", "Please select at least one option.")
    elif dropdown_selection == "":
        messagebox.showerror("Error", "Please select a country.")
    else:
        selected_options_str = ', '.join(selected_options)
        # Create a new window to display selection results
        results_window = tk.Toplevel(root)
        results_window.title("Selection Results")
        results_window.geometry("300x200")

        # Set background color for the results window
        results_window.configure(bg="#f0f0f0")

        # Label to display selection results
        results_label = tk.Label(results_window, text=f"I want to go to: {dropdown_selection}\nTo: {selected_options_str}", font=("Arial", 12), bg="#f0f0f0", fg="blue")
        results_label.pack(pady=10)

        # Close button for the results window
        close_button = tk.Button(results_window, text="Close", command=results_window.destroy, font=("Arial", 12), bg="red", fg="white")
        close_button.pack(pady=10)

# Create main window
root = tk.Tk()
root.title("Age Calculator")

# Instructions label
instructions_label = tk.Label(root, text="Select what you would like to do:", font=("Arial", 12, "bold"), foreground="blue")
instructions_label.pack(pady=(10, 0))

# Create checkboxes
checkboxes = {}
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)
options = ["Drink", "Drive", "Smoke", "Own a Firearm", "Vote"]

for option in options:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(checkbox_frame, text=option, variable=var, font=("Arial", 10), foreground="blue")
    checkbox.pack(anchor=tk.W)
    checkboxes[option] = var

# Create dropdown bar
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(pady=10)
dropdown_label = tk.Label(dropdown_frame, text="Select where you want to go:", font=("Arial", 12, "bold"), foreground="blue")
dropdown_label.pack(side=tk.LEFT)
dropdown = ttk.Combobox(dropdown_frame, values=["India", "Thailand", "Turkey"], font=("Arial", 10), state="readonly")
dropdown.pack(side=tk.LEFT)

# Set default dropdown selection
dropdown.set("")

# Submit button
submit_button = tk.Button(root, text="Generate", command=submit, font=("Arial", 12, "bold"), foreground="white", background="blue")
submit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()