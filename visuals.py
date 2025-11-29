import tkinter as tk
from core_calculations import avg_grade, avg_attendance, num_passed, num_grades, num_failed
from tkinter import ttk
# ttk contains the new widgets from 2007

# create an instance of the tk.Tk class, this will create the application window 
# convention: the main window in Tkinter is called root
root = tk.Tk()

# CONTROLLING THE WINDOW
# This changes the title of the window
root.title('PennysProj')
# window geomtry/ size and postion of the window
# width x height and then +x +y 
# +y = 50, means that the windows veritcal position will be 50 pixels below the top of the screen
# root.geometry('600x400+50+50')
window_width = 500
window_height = 500
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# Title of the window
message = tk.Label(root, text="Student Grade Analysis")
message.pack()

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

try:
    # this stops the text from being blury
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    # mainloop ensures the window remains visible, without it will appear and disappear quickly
    root.mainloop()


#REFERENCES
#https://www.pythontutorial.net/tkinter/tkinter-ttk/

