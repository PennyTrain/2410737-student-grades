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