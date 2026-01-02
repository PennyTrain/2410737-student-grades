
import tkinter as tk
from core_calculations import avg_grade, avg_attendance, num_passed, num_grades, num_failed
from searching import update_suggestions, select_suggestion, perform_search
from graphs import make_graph
from scraping import web_scraped
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
    # https://www.pythontutorial.net/tkinter/tkinter-ttk/
    window_width = 650
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

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20, padx=20)

    buttons = [
        ("Average Grade", lambda: show("Average Grade", avg_grade())),
        ("Average Attendance", lambda: show("Average Attendance", avg_attendance())),
        ("Number Of Passes", lambda: show("Number Of Passes", num_passed())),
        ("Number Of Fails", lambda: show("Number Of Fails", num_failed())),
        ("Number Of Grades", lambda: show("Number Of Grades", num_grades())),
        ("Graph: Grades Vs Age", lambda: make_graph("age", "grade")),
        ("Graph: Attendance Vs Age", lambda: make_graph("age", "attendance")),
        ("Graph: Attendance Vs Grade", lambda: make_graph("attendance", "grade")),
    ]

    for index, (text, command) in enumerate(buttons):
        # every 2 buttons add another row for another 2 buttons
        row = index // 2
        col = index % 2

        ttk.Button(
            button_frame,
            text=text,
            style="Custom.TButton",
            command=command
        ).grid(row=row, column=col, padx=10, pady=10, sticky="ew")

    # Make both columns stretch evenly
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    # https://pythonguides.com/python-tkinter-search-box/
    # SEARCH FUNCTIONALITY
    search_var = tk.StringVar()
    search_label = ttk.Label(root, text="Search, Type Student Name:", style="Custom.TLabel")
    search_label.pack()
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

    def close_window():
        root.destroy()

    button = ttk.Button(root, text="Quit", style="Custom.TButton", command=close_window)
    button.pack()

    scrape_label = ttk.Label(root, text=web_scraped(), style="Custom.TLabel")
    scrape_label.pack()

    try:
        # this stops the text from being blury
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        # ignore if not on Windows or call is unavailable
        pass
    finally:
        # mainloop ensures the window remains visible, without it will appear and disappear quickly
        root.mainloop()
