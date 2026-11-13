from datetime import date
import tkinter as tk
from tkinter import messagebox


def calculate_age():
  try:
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    birth_date = date(year, month, day)
    today = date.today()

    if birth_date > today:
      messagebox.showerror("Invalid Date", "Birth date cannot be in the future.")
      return

    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )

    result_label.config(text=f"Your Present Age: {age} years")

  except ValueError:
    messagebox.showerror(
        "Invalid Input", "Please enter a valid numeric date, month, and year."
    )


root = tk.Tk()
root.title("Age Calculator")
root.geometry("320x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

tk.Label(input_frame, text="Date (DD):", font=("Arial", 11)).grid(
    row=0, column=0, padx=5, pady=5, sticky="e"
)
day_entry = tk.Entry(input_frame, width=15)
day_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Month (MM):", font=("Arial", 11)).grid(
    row=1, column=0, padx=5, pady=5, sticky="e"
)
month_entry = tk.Entry(input_frame, width=15)
month_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Year (YYYY):", font=("Arial", 11)).grid(
    row=2, column=0, padx=5, pady=5, sticky="e"
)
year_entry = tk.Entry(input_frame, width=15)
year_entry.grid(row=2, column=1, padx=5, pady=5)

calc_button = tk.Button(
    root,
    text="Calculate Age",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate_age,
)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#333333")
result_label.pack(pady=5)

root.mainloop()
