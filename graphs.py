import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

conn = sqlite3.connect("student-data/student_grades.db")
df = pd.read_sql_query("SELECT age, grade, attendance FROM student;", conn)
conn.close()

avg_grade_by_age = df.groupby("age")["grade"].mean().reset_index().sort_values("age")
avg_att_by_age = df.groupby("age")["attendance"].mean().reset_index().sort_values("age")
avg_att_by_grade = df.groupby("grade")["attendance"].mean().reset_index().sort_values("grade")

def grade_age():
    """Average Grade by Age"""
    plt.bar(avg_grade_by_age["age"], avg_grade_by_age["grade"],
            color="skyblue", edgecolor="black")
    plt.title("Average Grade by Age")
    plt.xlabel("Age")
    plt.ylabel("Average Grade")
    plt.tight_layout()
    plt.show()

def attendance_age():
    """Average Attendance by Age"""
    plt.bar(avg_att_by_age["age"], avg_att_by_age["attendance"],
            color="lightgreen", edgecolor="black")
    plt.title("Average Attendance by Age")
    plt.xlabel("Age")
    plt.ylabel("Average Attendance")
    plt.tight_layout()
    plt.show()

def attendance_grade():
    plt.scatter(df["attendance"], df["grade"], alpha=0.6, edgecolor="black")
    plt.title("Grades vs Attendance")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Grade")
    z = np.polyfit(df["attendance"], df["grade"], 1)
    plt.plot(df["attendance"], np.polyval(z, df["attendance"]))
    plt.tight_layout()
    plt.show()

def make_graph(x, y):
    if x == 'attendance' and y == 'grade':
        attendance_grade()
    elif x == 'age' and y == 'grade':
        grade_age()
    elif x == 'age' and y == 'attendance':
        attendance_age()
    else:
        print("That graph type isn't defined yet.")