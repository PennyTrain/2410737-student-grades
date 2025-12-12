import tkinter as tk
import sqlite3

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()

# https://pythonguides.com/python-tkinter-search-box/

def update_suggestions(search_var, suggestion_list):
    search_term = search_var.get().strip().lower()

    # Fetch all rows
    c.execute("SELECT first_name, last_name FROM student")
    rows = c.fetchall()

    # Build a set of unique FULL names only
    full_names = {f"{first} {last}" for first, last in rows}

    matching_suggestions = []

    if search_term:
        for full in full_names:
            first, last = full.split(" ", 1)

            # Match if user types start of first name, last name, or full name
            if (
                first.lower().startswith(search_term)
                or last.lower().startswith(search_term)
                or full.lower().startswith(search_term)
            ):
                matching_suggestions.append(full)
    else:
        matching_suggestions = sorted(full_names)

    # Update the listbox
    suggestion_list.delete(0, tk.END)
    for suggestion in matching_suggestions:
        suggestion_list.insert(tk.END, suggestion)




def select_suggestion(event, search_var, suggestion_list, perform_search):
    if suggestion_list.curselection():
        selected_suggestion = suggestion_list.get(suggestion_list.curselection())
        search_var.set(selected_suggestion)
        perform_search()


def perform_search(search_var, details_label):
    search_term = search_var.get().strip()

    # CASE 1: User typed "First Last"
    if " " in search_term:
        first_name, last_name = search_term.split(" ", 1)
        c.execute(
            """
            SELECT * FROM student
            WHERE lower(first_name) = lower(?)
            AND lower(last_name) = lower(?)
            """,
            (first_name.strip(), last_name.strip())
        )

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

    students = c.fetchall()

    if not students:
        details_label.config(text="Student not found.")
        return

    # Show ALL matching students
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




def completed(value):
    return value != 0




