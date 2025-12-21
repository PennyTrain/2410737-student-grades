import tkinter as tk
from core_calculations import avg_grade, avg_attendance, num_passed, num_grades, num_failed
from searching import update_suggestions, select_suggestion, perform_search
from graphs import make_graph
import styles
from tkinter import ttk
# ttk contains the new widgets from 2007

# create an instance of the tk.Tk class, this will create the application window 
# convention: the main window in Tkinter is called root
def app():
    root = tk.Tk()

# CONTROLLING THE WINDOW
# This changes the title of the window
    root.title('Student Grades')
# window geomtry/ size and postion of the window
# width x height and then +x +y 
# +y = 50, means that the windows veritcal position will be 50 pixels below the top of the screen
# root.geometry('600x400+50+50')
#https://www.pythontutorial.net/tkinter/tkinter-ttk/
    window_width = 500
    window_height = 985
# get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
# find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    styles.apply_styles(root)
    styles.apply_background(root)
# Title of the window
    message = ttk.Label(root, text="Student Grade Analysis", style="Custom.TLabel")
    message.pack()

    result_label = ttk.Label(root, text="", style="Custom.TLabel")
    result_label.pack()

    def show(label_text, result):
        text = f"{label_text}: {result}" if result is not None else f"{label_text}: No data"
        result_label.config(text=text)
# https://www.w3schools.com/python/python_lambda.asp
    ttk.Button(root, text="Average Grade", style="Custom.TButton",command=lambda: show("Average Grade", avg_grade())).pack(pady=10)
    ttk.Button(root, text="Average Attendance", style="Custom.TButton",command=lambda: show("Average Attendance", avg_attendance())).pack(pady=10)
    ttk.Button(root, text="Number Of Passes", style="Custom.TButton",command=lambda: show("Number Of Passes", num_passed())).pack(pady=10)
    ttk.Button(root, text="Number Of Fails", style="Custom.TButton",command=lambda: show("Number Of Fails", num_failed())).pack(pady=10)
    ttk.Button(root, text="Number Of Grades", style="Custom.TButton",command=lambda: show("Number Of Grades", num_grades())).pack(pady=10)
    ttk.Button(root, text="Grades Vs Age", style="Custom.TButton",command=lambda: ("Grades Vs Age", make_graph('age', 'grade'))).pack(pady=10)
    ttk.Button(root, text="Attendance Vs Age", style="Custom.TButton",command=lambda: ("Attendance Vs Age", make_graph('age', 'attendance'))).pack(pady=10)
    ttk.Button(root, text="Attendance Vs Grade", style="Custom.TButton",command=lambda: ("Attendance Vs Grade", make_graph('attendance', 'grade'))).pack(pady=10)

# https://pythonguides.com/python-tkinter-search-box/
# SEARCH FUNCTIONALITY
    search_var = tk.StringVar()

    search_entry = ttk.Entry(
        root,
        textvariable=search_var,
        style="Neon.TEntry"
    )
    search_entry.pack()

    suggestion_list = tk.Listbox(root)
    styles.style_listbox(suggestion_list)
    suggestion_list.pack(pady=5, fill="x", padx=20)

    details_label = ttk.Label(root, style="Custom.TLabel")
    details_label.pack(anchor="w")

    search_var.trace("w", lambda *args: update_suggestions(search_var, suggestion_list))
    suggestion_list.bind(
        "<<ListboxSelect>>",
        lambda event: select_suggestion(
            event,
            search_var,
            suggestion_list,
            lambda: perform_search(search_var, details_label)
        )
    )
    search_entry.bind("<Return>", lambda event: perform_search(search_var, details_label))



    try:
    # this stops the text from being blury
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        # mainloop ensures the window remains visible, without it will appear and disappear quickly
        root.mainloop()
