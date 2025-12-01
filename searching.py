
import tkinter as tk

# https://pythonguides.com/python-tkinter-search-box/
def update_suggestions(search_var, suggestion_list):
    search_term = search_var.get()
    suggestions = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

    matching_suggestions = [s for s in suggestions if s.lower().startswith(search_term.lower())]

    suggestion_list.delete(0, tk.END)
    for suggestion in matching_suggestions:
        suggestion_list.insert(tk.END, suggestion)

def select_suggestion(event, search_var, suggestion_list, perform_search):
    if suggestion_list.curselection():
        selected_suggestion = suggestion_list.get(suggestion_list.curselection())
        search_var.set(selected_suggestion)
        perform_search()

def perform_search(search_var):
    search_term = search_var.get()
    print("Performing search for:", search_term)
