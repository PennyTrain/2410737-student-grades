import sqlite3
import matplotlib.pyplot as plt
# the import to make graphs
import pandas as pd
# library for data analysis
import numpy as np
# numerical tool (helps do math)

conn = sqlite3.connect("student-data/student_grades.db")
df = pd.read_sql_query("SELECT age, grade, attendance FROM student;", conn)
# here I am using pandas to help me get the data from student_grades 
# it is returning the results as a pandas dataframe
# I can do this without Pandas like this
# conn = sqlite3.connect("student-data/student_grades.db")
# c = conn.cursor()
# c.execute("SELECT age, grade, attendance FROM student")
conn.close()

avg_grade_by_age = df.groupby("age")["grade"].mean().reset_index().sort_values("age")
avg_att_by_age = df.groupby("age")["attendance"].mean().reset_index().sort_values("age")
avg_att_by_grade = df.groupby("grade")["attendance"].mean().reset_index().sort_values("grade")
# with df.groupby I am splitting the rows into groups by the column
# and then with .mean() I am finding the groups mean
# reset_index() turns the grouped index back into normal columns for easy plotting

def grade_age():
    # This function displays a graph comparing the age and grade
    plt.bar(avg_grade_by_age["age"], avg_grade_by_age["grade"])
    # creates a bar chart
    plt.title("Average Grade by Age")
    # gives the graph a title
    plt.xlabel("Age")
    # labels the x axis
    plt.ylabel("Average Grade")
    # labels the y axis
    plt.tight_layout()
    # adjusts the spacing to that the labels do not overlap
    plt.show()
    # displays the graph


def attendance_age():
    # this function displays a graph comparing the age and attendance
    plt.bar(avg_att_by_age["age"], avg_att_by_age["attendance"])
    plt.title("Average Attendance by Age")
    plt.xlabel("Age")
    plt.ylabel("Average Attendance")
    plt.tight_layout()
    plt.show()

def attendance_grade():
    # this function displays a graph comparing attendance and grade
    plt.scatter(df["attendance"], df["grade"])
    # displays a scatter plot for each student
    plt.title("Grades vs Attendance")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Grade")
    z = np.polyfit(df["attendance"], df["grade"], 1)
    # does a least squares liniar fit, and returns slope
    plt.plot(df["attendance"], np.polyval(z, df["attendance"]))
    # this finds the fitted line at the x-values to plot a trend line
    plt.tight_layout()
    plt.show()

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

def make_graph(x, y):
    plt.close('all')
    # closes any open matplotlib windows, so that the plots do not stack
    plt.rcParams.update(plt.rcParamsDefault)
    # resets all the styles I have applies to make sure they do not stack
    if x == 'attendance' and y == 'grade':
        pink_theme()
        # applies theme
        attendance_grade()
        # gets correct graph based on button value
    elif x == 'age' and y == 'grade':
        pink_theme()
        grade_age()

    elif x == 'age' and y == 'attendance':
        pink_theme()
        attendance_age()
    else:
        print("That graph type isn't defined yet.")