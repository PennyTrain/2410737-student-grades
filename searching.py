
import tkinter as tk
import sqlite3

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()

# https://pythonguides.com/python-tkinter-search-box/

def update_suggestions(search_var, suggestion_list):
    search_term = search_var.get()
    
    # Fetch all rows from the query
    c.execute("SELECT first_name, last_name FROM student")
    rows = c.fetchall()  # This returns a list of tuples like [('John', 'Doe'), ('Jane', 'Smith')]

    # Combine first and last names into a single string
    suggestions = [f"{first} {last}" for first, last in rows]

    # Filter suggestions based on search term
    matching_suggestions = [s for s in suggestions if s.lower().startswith(search_term.lower())]

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
    search_term = search_var.get()
    
    # Split the name into first and last
    try:
        first_name, last_name = search_term.split(" ", 1)
    except ValueError:
        first_name, last_name = search_term, ""  # Handle single name case
    
    # Query full student details
    c.execute("SELECT * FROM student WHERE first_name = ? OR last_name = ?", (first_name, last_name))
    student = c.fetchone()  # Returns a tuple like (id, first_name, last_name, grade, age, etc.)
    
    if student:
        # Format details for display
        details_text = f"""
        ID: {student[0]}
        First Name: {student[1]}
        Last Name: {student[2]}
        Age: {student[3]}
        Email: {student[4]}
        Country: {student[5]}
        Attendance: {student[6]}
        Assignment Completed: {completed(student[7])}
        Grade: {student[8]}
        """
    else:
        details_text = "Student not found."
    

    # Update label
    details_label.config(text=details_text)


def completed(value):
    return value != 0

