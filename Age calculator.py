#@26. Age calculator

import tkinter as tk
from datetime import date

root=tk.Tk()
root.title("Age Calculator")

label=tk.Label(root,text="Enter your birth year:")
label.pack()

entry=tk.Entry(root)
entry.pack()

result_label=tk.Label(root,text="")
result_label.pack()

def calculate_age():
  birth_year=int(entry.get())
  current_year=date.today().year
  current_year=date.today().year
  age=current_year-birth_year

  result_label.config(text=f"Your age is:{age}")
  return age

button=tk.Button(root,text="Calculate Age",command=calculate_age)
button.pack()

root.mainloop()
