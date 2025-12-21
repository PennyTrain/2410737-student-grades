from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
from tkinter import ttk

# Apply global ttk styling + neon theme for labels/buttons/entries

def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("alt")

    # ---- NEON LABEL ----
    style.configure(
        "Custom.TLabel",
        foreground="#0affff",     # neon cyan text
        background="black",
        font=("Consolas", 11)
    )

    # ---- NEON BUTTON ----
    style.configure(
        "Custom.TButton",
        font=("Consolas", 12, "bold"),
        foreground="black",
        background="#39ff14",     # neon green
        padding=(10, 8),
        borderwidth=0
    )
    style.map(
        "Custom.TButton",
        background=[("active", "#0affff")],
        foreground=[("active", "black")]
    )

    # ---- NEON ENTRY (ttk.Entry) ----
    style.configure(
        "Neon.TEntry",
        foreground="#0affff",
        fieldbackground="black",
        background="black",
        borderwidth=1,
        insertcolor="#39ff14"    # neon caret if supported by OS
    )
    style.map(
        "Neon.TEntry",
        foreground=[("focus", "#39ff14")],   # glow text when focused
    )



# Apply root window background + ttk global background
def apply_background(root):
    root.configure(bg="black")  # neon theme background

    style = ttk.Style(root)
    style.configure("TFrame", background="black")
    style.configure("TLabel", background="black")
    style.configure("Custom.TLabel", background="black")



# Style a Tk Listbox (classic widget — not ttk)
def style_listbox(listbox):
    listbox.configure(
        bg="black",
        fg="#0affff",                  # neon cyan text
        highlightthickness=1,
        highlightbackground="#39ff14", # neon green border
        selectbackground="#39ff14",    # neon green selection
        selectforeground="black",
        borderwidth=0
    )

# GRAPHING STYLES

def neon_cyan_theme():
    plt.style.use("dark_background")

    plt.rcParams["figure.facecolor"] = "#000000"    
    plt.rcParams["axes.facecolor"] = "#000000"
    plt.rcParams["axes.edgecolor"] = "#0affff"      
    plt.rcParams["axes.labelcolor"] = "#0affff"
    plt.rcParams["xtick.color"] = "#0affff"
    plt.rcParams["ytick.color"] = "#0affff"
    plt.rcParams["text.color"] = "#0affff"
    plt.rcParams["grid.color"] = "#073b3b"        
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#0affff"])  


def neon_green_theme():
    plt.style.use("dark_background")
    plt.rcParams["figure.facecolor"] = "#000000"
    plt.rcParams["axes.facecolor"] = "#000000"
    plt.rcParams["axes.edgecolor"] = "#39ff14"   
    plt.rcParams["axes.labelcolor"] = "#39ff14"
    plt.rcParams["xtick.color"] = "#39ff14"
    plt.rcParams["ytick.color"] = "#39ff14"
    plt.rcParams["text.color"] = "#39ff14"
    plt.rcParams["grid.color"] = "#0f3306"       
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#39ff14"])

def neon_magenta_theme():
    plt.style.use("dark_background")
    plt.rcParams["figure.facecolor"] = "#000000"
    plt.rcParams["axes.facecolor"] = "#000000"
    plt.rcParams["axes.edgecolor"] = "#ff00ff"   
    plt.rcParams["axes.labelcolor"] = "#ff00ff"
    plt.rcParams["xtick.color"] = "#ff00ff"
    plt.rcParams["ytick.color"] = "#ff00ff"
    plt.rcParams["text.color"] = "#ff00ff"
    plt.rcParams["grid.color"] = "#330033"          
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#ff00ff"])
