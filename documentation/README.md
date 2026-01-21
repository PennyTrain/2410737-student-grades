My prompt was simply to take it out of first person and make it sound "better"

I have made python code to analyze all the data in an SQLlite database based on queries, I have created the sqlite3 database based on a csv file filled withall of the information, and then used the python programming with multiple packages to manipulate the data, the packages I have used are 
sys, os, sqlite3, unittest, atexit,csv, matplotlib, pandas, numpy, requests, beautifulsoup, tkinter (ttk and tk)
^me
AI:
This Student Grades Project involves developing Python code to analyze data stored in an SQLite database using SQL queries. The SQLite3 database was created from a CSV file containing all student grade information. Python programming was then used, along with multiple packages, to manipulate, analyze, and visualize the data. The packages used in this project include sys, os, sqlite3, unittest, atexit, csv, matplotlib, pandas, numpy, requests, BeautifulSoup, and tkinter (tk and ttk).


The buttons display different data values based on the button clicked, I am only manipulating one tkinter label here to return the correct value, 3 of the buttons then display different grades, For the buttons I am using a list of button definitions and repeating them based on a list. This makes for a scalable and dynamic design
User stories
as a first time visitor, I want the applications to be clear
as a first time user I want to easily navigate
as a first time user I want the application to be as aesthetically pleasing as possible given limmit resources for creating a python GUI
As a returning visitor, I want a range of information accessible to me
As a returning visitor, I want it to be consistent
As an organization I want the applications to be accessible and easy to use to the interested parties
^me
AI:
The graphical user interface uses Tkinter buttons to display different data values based on user interaction. A single Tkinter label is dynamically updated to return the correct value depending on which button is selected. Three of the buttons are dedicated to displaying different grades. Button creation is handled through a list of button definitions that are iterated over, allowing for a scalable and dynamic design that supports future expansion.
User Stories
As a first-time visitor, the application should be clear and easy to understand.
As a first-time user, the application should be easy to navigate.
As a first-time user, the application should be as aesthetically pleasing as possible given the limited resources available for creating a Python GUI.
As a returning visitor, a range of information should be easily accessible.
As a returning visitor, the application should provide a consistent experience.
As an organization, the application should be accessible, intuitive, and easy to use for all interested parties.


I used github kanban boards in order to help me track my progress and understand what left was needed to be done, I did this to ensure I followed an agile workflow, aswell as MOSCOW, the must have, should have, could have... As a could have, Ideally I wanted the users to be able to choose the inputs for their own graphs. As a user I would like to choose 3 different age groups from one country and calculate each ones average grade.. However this was a bit too advanced for my ksill level... I gope to add it in the future and list this as one of my future enhancements. I did attempt this however struggled on limiting tkinter boxes based on user input, Say I want to graph 3 different countries, I striggled with the CRUD functionality of creating input boxes for the user 
^me
AI:
GitHub Kanban boards were used to track project progress and identify remaining tasks throughout development. This approach helped maintain an agile workflow and ensured that work was organized and incremental. The MoSCoW prioritization method was also applied to define project requirements, categorizing features into must-have, should-have, could-have, and won’t-have items.
One proposed could-have feature was to allow users to define custom inputs for generating their own graphs. Ideally, users would be able to select three different age groups from a single country and calculate the average grade for each group. However, this functionality proved to be beyond the current skill level required for the project timeline. As a result, it has been identified as a potential future enhancement.
An attempt was made to implement this feature, but challenges were encountered when trying to dynamically limit and generate Tkinter input fields based on user selections. Specifically, difficulties arose with the CRUD functionality needed to create and manage user input boxes—for example, when allowing users to graph data for multiple countries. These limitations highlighted areas for future learning and improvement, and the feature is planned for inclusion in later iterations of the project.


Original Idea, I have played with python previously making an in terminal quiz, where the user inputted, and read directly from the terminal, I then used some fancy html and packages to ensure that I could display it on a terminal and then I deployed it to heroku... I wanted to do the same for this, as it would ease my workload considering I know how to do it. Instea dof creating a whole GUI.... But then I realized whats the point in going to university sitting in a classroom for 3 hours every week to ignore, not learn, and stick with what I know. However in my future enhancements I would also like to deploy this and add it to a portfolio!
me ^
AI:
Previous experience with Python included developing an in-terminal quiz application that accepted user input directly through the terminal. That project used HTML styling and additional packages to enhance terminal display and was successfully deployed to Heroku. Initially, the same approach was considered for this project, as it would have reduced development time by building on existing knowledge rather than creating a full graphical user interface.

However, during development it became clear that relying solely on familiar tools would limit learning outcomes. The purpose of attending university and engaging in weekly lectures and practical sessions is to develop new skills and explore unfamiliar technologies. For this reason, the decision was made to build a full GUI using Tkinter, rather than remaining within a terminal-based interface. Despite this, deploying the application online and adding it to a professional portfolio remains a planned future enhancement.


Features:
At the bottom I have scapred all contact information of another website, One I built myself!
I have created a user input feild to plug in different students names and search my sqlite3 database, the search function works by searching both last and first names
I have 3 different graphing buttons (i can graph: age vs grade, age vs attendance, and grade vs age)
I have some core calculation buttons, these display the average grade, avg attendance, num of pases, num of fails, num of grades.
I have included a neon theme throughout the tkinter gui. and I have also styled my graphs to match the same kind of neon theme.
I have tested this to ensure it is working, a lot of the time I used something called 'TikTok Testing' it is a term I learned at work, which is basically testing it end to end and taking a video, attaching it to the ticket and ensuring it all works! For my essay I have taken screenshots
me ^
AI:
Contact information displayed at the bottom of the interface is scraped from a separate website, which was also developed independently. 
A user input field allows searching the SQLite3 database for students by name. The search functionality supports both first and last name queries.
Three graphing options are available:
Age vs Grade
Age vs Attendance
Grade vs Age
Core calculation buttons provide:
Average grade
Average attendance
Number of passes
Number of fails
Total number of grades
A consistent neon-themed design is applied throughout the Tkinter GUI, with graph styling matched to the same aesthetic.

How to play:
open up the main.py file, and press the run button
click whichever button desired
click quit when done 
me^
AI:
How to Run the Application
Open the main.py file.
Click the Run button.
Select the desired feature using the on-screen buttons.
Click Quit to exit the application.








Things I have noticed
A random file was introduced when running my program? I know I should go and get a proper reference, however in the panick of "what have I just spawned???" I asked ai to get a quick answer and this is what I got... As I found it super weird that once I fixed all my syntax, I suddenly started auto generating random files
'Thought for 6s
Yesss, love a “slay and debug” arc 💅
That student_grades.db-journal file is totally normal and created by SQLite itself, not a bug in your code.
What it is
When SQLite writes to your database (student_grades.db), it uses a journal file to keep things safe in case something goes wrong (crash, power cut, etc).
That’s the student_grades.db-journal file you’re seeing.
It’s used to store changes temporarily while a transaction is in progress, so SQLite can either:
fully commit the change, or
roll back cleanly if something fails.'
me^
ai:
During development, an unexpected file appeared when running the program, which initially caused concern. After investigation, it was determined that this behavior is normal. SQLite automatically generates a .db-journal file when writing changes to a database. This journal file is used to temporarily store transaction data, allowing SQLite to safely commit changes or roll them back in the event of an error or interruption. Once transactions are completed successfully, the file may be removed automatically.




I have not used logging debug module as I was taught that console logs make bad practice to be in production. so therefore the only thing that prints are my tests 