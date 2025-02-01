import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        percentage = float(entry.get())
        if 80 <= percentage <= 100:
            grade = "A+"
        elif 70 <= percentage < 80:
            grade = "A"
        elif 60 <= percentage < 70:
            grade = "B"
        elif 50 <= percentage < 60:
            grade = "C"
        elif 40 <= percentage < 50:
            grade = "D"
        elif 0 <= percentage < 40:
            grade = "F"
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid percentage between 0 and 100.")
            return
        result_label.config(text=f"Your percentage is {percentage}% and your grade is {grade}.", fg="green")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")

def reset_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    root.destroy()

# Creating the main window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x280")
root.resizable(False, False)

# Adding a header
header = tk.Label(root, text="Grade Calculator By Ali Raza", font=("Helvetica", 16, "bold"), fg="dark red")
header.pack(pady=20)

# Input for percentage
input_frame = tk.Frame(root)
input_frame.pack(pady=15)
tk.Label(input_frame, text="Enter Percentage:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
entry = tk.Entry(input_frame, font=("Helvetica", 12), width=15)
entry.grid(row=0, column=1)

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

calculate_btn = tk.Button(button_frame, text="Calculate", fg ="#000", font=("Arial", 12), bg="darkorange", command=calculate_grade)
calculate_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(button_frame, text="Reset", font=("Arial", 12), bg="white", command=reset_fields)
reset_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg="#C7290F", command=exit_app)
exit_btn.grid(row=0, column=2, padx=10)

# Result display area
result_label = tk.Label(root, text="", font=("Arial", 12), fg="green", wraplength=350, justify="center")
result_label.pack(pady=20)

# Running the application
root.mainloop()
