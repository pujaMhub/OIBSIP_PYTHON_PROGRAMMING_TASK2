import tkinter as tk
from tkinter import ttk

def calculate_bmi(*args):
    try:
        weight = float(weight_var.get())
        height_cm = float(height_var.get())
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category, color, value = "Underweight", "#F48FB1", 10
        elif bmi < 24.9:
            category, color, value = "Normal", "#F06292", 30
        elif bmi < 29.9:
            category, color, value = "Overweight", "#EC407A", 60
        else:
            category, color, value = "Obese", "#D81B60", 90

        bmi_value_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}", fg=color)
        progress_bar["value"] = value
        style.configure("pink.Horizontal.TProgressbar", background=color)

    except ValueError:
        bmi_value_label.config(text="BMI: --")
        category_label.config(text="Category: --")
        progress_bar["value"] = 0

def reset():
    weight_var.set("")
    height_var.set("")
    bmi_value_label.config(text="BMI: --")
    category_label.config(text="Category: --")
    progress_bar["value"] = 0

root = tk.Tk()
root.title("Pink BMI Calculator 💗")
root.geometry("360x320")
root.configure(bg="#FCE4EC")  # Light pink background

# Variables
weight_var = tk.StringVar()
height_var = tk.StringVar()

weight_var.trace_add("write", calculate_bmi)
height_var.trace_add("write", calculate_bmi)

# Title
tk.Label(root, text="💖 BMI Calculator 💖", font=("Segoe UI", 18, "bold"),
         bg="#FCE4EC", fg="#AD1457").pack(pady=10)

frame = tk.Frame(root, bg="#FCE4EC")
frame.pack(pady=10)

# Input fields
tk.Label(frame, text="Weight (kg):", font=("Segoe UI", 12), bg="#FCE4EC", fg="#880E4F").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(frame, textvariable=weight_var, font=("Segoe UI", 12), relief="flat", highlightbackground="#F8BBD0",
         highlightthickness=2, width=15).grid(row=0, column=1, pady=5)

tk.Label(frame, text="Height (cm):", font=("Segoe UI", 12), bg="#FCE4EC", fg="#880E4F").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(frame, textvariable=height_var, font=("Segoe UI", 12), relief="flat", highlightbackground="#F8BBD0",
         highlightthickness=2, width=15).grid(row=1, column=1, pady=5)

# Output labels
bmi_value_label = tk.Label(root, text="BMI: --", font=("Segoe UI", 14, "bold"), bg="#FCE4EC", fg="#880E4F")
bmi_value_label.pack(pady=(10, 2))

category_label = tk.Label(root, text="Category: --", font=("Segoe UI", 12), bg="#FCE4EC", fg="#880E4F")
category_label.pack()

# Progress bar
style = ttk.Style()
style.theme_use('default')
style.configure("pink.Horizontal.TProgressbar", troughcolor="#F8BBD0", background="#EC407A", thickness=20)

progress_bar = ttk.Progressbar(root, style="pink.Horizontal.TProgressbar", length=300, mode="determinate", maximum=100)
progress_bar.pack(pady=15)

# Reset button
tk.Button(root, text="Reset", command=reset, font=("Segoe UI", 12, "bold"),
          bg="#F48FB1", fg="white", activebackground="#F06292",
          relief="flat", padx=10, pady=5).pack(pady=5)

root.mainloop()
