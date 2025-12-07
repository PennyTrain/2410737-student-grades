from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
# the import to make graphs
import pandas as pd
# library for data analysis
import numpy as np

def apply_styles(root):
    style = ttk.Style(root)

    # Use a theme (e.g., 'clam', 'alt', 'default', 'classic')
    style.theme_use('alt')

    # Button style
    style.configure(
        "Custom.TButton",
        font=("Helvetica", 12, "bold"),
        foreground="white",
        background="#ff0084",
        padding=(10, 10)  # (x-padding, y-padding)
    )


    # Label style
    style.configure(
        "Custom.TLabel",
        font=("Helvetica", 11),
        foreground="#333"
    )

    # Optional: hover effect for buttons
    style.map(
        "Custom.TButton",
        background=[("active", "#005f99")]
    )


def pink_theme():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["axes.facecolor"] = "#ffe6f2"
    plt.rcParams["figure.facecolor"] = "#ffb6c1"
    plt.rcParams["axes.labelcolor"] = "#000000"
    plt.rcParams["text.color"] = "#000000"
    plt.rcParams["axes.edgecolor"] = "#e91e63"
    plt.rcParams["xtick.color"] = "#000000"
    plt.rcParams["ytick.color"] = "#000000"
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#cc00ff"])  # all plots pink
    # plt.rcParams customizes global defaults like background
    # plt.style.use applies a style sheet

def blue_theme():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["axes.facecolor"] = "#c0f0ff"
    plt.rcParams["figure.facecolor"] = "#9c88f5"
    plt.rcParams["axes.labelcolor"] = "#000000"
    plt.rcParams["text.color"] = "#000000"
    plt.rcParams["axes.edgecolor"] = "#1e21e9"
    plt.rcParams["xtick.color"] = "#000000"
    plt.rcParams["ytick.color"] = "#000000"
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#04044e"])  # all plots pink
    # plt.rcParams customizes global defaults like background
    # plt.style.use applies a style sheet

def purple_theme():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["axes.facecolor"] = "#dec0ff"
    plt.rcParams["figure.facecolor"] = "#d888f5"
    plt.rcParams["axes.labelcolor"] = "#000000"
    plt.rcParams["text.color"] = "#000000"
    plt.rcParams["axes.edgecolor"] = "#a91ee9"
    plt.rcParams["xtick.color"] = "#000000"
    plt.rcParams["ytick.color"] = "#000000"
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#300241"])  # all plots pink
    # plt.rcParams customizes global defaults like background
    # plt.style.use applies a style sheet

