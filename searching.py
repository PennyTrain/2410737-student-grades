import tkinter as tk
import sqlite3

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()

# https://pythonguides.com/python-tkinter-search-box/

def update_suggestions(search_var, suggestion_list):
    # search_var is tied to the user input of search
    # suggestion_list is also tk 
    search_term = search_var.get().strip().lower()
    # this gets the input and makes it all lower case and gets rid of 
    # all the trailing space
    # Fetch all rows
    c.execute("SELECT first_name, last_name FROM student")
    rows = c.fetchall()

    full_names = {f"{first} {last}" for first, last in rows}
    # only gets original names, avoids duplicates

    matching_suggestions = []
    # empty to store all the output based on what the user types

    if search_term:
        #^ checks if user typed something
        for full in full_names:
            # loops through the names
            first, last = full.split(" ", 1)
            # 1 means split only once! 

            # this checks if the user types, first or full or last names!
            if (
                first.lower().startswith(search_term)
                or last.lower().startswith(search_term)
                or full.lower().startswith(search_term)
            ):
                # if match add to empty array
                matching_suggestions.append(full)
    else:
        # if search box is empty show all names sorted alphabetically 
        matching_suggestions = sorted(full_names)

    # Update the listbox
    suggestion_list.delete(0, tk.END)
    # adds each matched name into array and insets in listbox
    for suggestion in matching_suggestions:
        # tk.END = append to end
        suggestion_list.insert(tk.END, suggestion)




def select_suggestion(event, search_var, suggestion_list, perform_search):
    # event = a tkinter event, like in .js like a mouseclick or hover
    # perform search = if i click someone who has appeared in the drop down,
    #  it is a function to run
    if suggestion_list.curselection():
        # curselection = checks if anything is selected, 'currentselection'
        selected_suggestion = suggestion_list.get(suggestion_list.curselection())
        # if true reads current selected item
        search_var.set(selected_suggestion)
        # sets search box text to full name of current selection
        perform_search()
        #selecting a suggestion triggers searching


def perform_search(search_var, details_label):
    # details label in order to display the results
    search_term = search_var.get().strip()

    # CASE 1: User typed "First Last"
    if " " in search_term:
        first_name, last_name = search_term.split(" ", 1)
        # if user types a space assume full name
        c.execute(
            """
            SELECT * FROM student
            WHERE lower(first_name) = lower(?)
            AND lower(last_name) = lower(?)
            """,
            (first_name.strip(), last_name.strip())
        )
        #  gets student names, is case sensitive

    else:
        # CASE 2: Single word → match first OR last name
        c.execute(
            """
            SELECT * FROM student
            WHERE lower(first_name) = lower(?)
            OR lower(last_name) = lower(?)
            """,
            (search_term.lower(), search_term.lower())
        )
        # this is for if only one word is typed
        # it searches both last_names and first_names for the
        # correct student

    students = c.fetchall()

    if not students:
        details_label.config(text="Student not found.")
        return
    # error handling, therefore if no student has that name,
    # it tells the user

    # when selected it displays the current users information in 
    # a label below the search list box
    details_text = ""
    for student in students:
        details_text += f"""
        ID: {student[0]}
        First Name: {student[1]}
        Last Name: {student[2]}
        Age: {student[3]}
        Email: {student[4]}
        Country: {student[5]}
        Attendance: {student[6]}
        Assignment Completed: {completed(student[7])}
        Grade: {student[8]}
        -------------------------
        """

    details_label.config(text=details_text)
    #^ updates GUI



def completed(value):
    print(value)
    return value != 0

# this is a little helper to make sure boolean values are stated
# instead of 1s and 0s like in the database




