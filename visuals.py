import tkinter as tk
from core_calculations import avg_grade, avg_attendance, num_passed, num_grades, num_failed

root = tk.Tk()
root.title('Learning')
root.geometry('500x400')

title = tk.Label(root, text='Welcome to my app')
title.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

def show(label_text, result):
    text = f"{label_text}: {result}" if result is not None else f"{label_text}: No data"
    result_label.config(text=text)

tk.Button(root, text="Average Grade", command=lambda: show("Average Grade", avg_grade())).pack(pady=10)
tk.Button(root, text="Average Attendance", command=lambda: show("Average Attendance", avg_attendance())).pack(pady=10)
tk.Button(root, text="Number Of Passes", command=lambda: show("Number Of Passes", num_passed())).pack(pady=10)
tk.Button(root, text="Number Of Fails", command=lambda: show("Number Of Fails", num_failed())).pack(pady=10)
tk.Button(root, text="Number Of Grades", command=lambda: show("Number Of Grades", num_grades())).pack(pady=10)

root.mainloop()
