#Rohan Shrestha (Rohan Shrestha@isu.edu)
#Database Project
INSTRUCTIONS FOR RUNNING THE DATABASE PROJECt


This program is a Python-based CRUD application for managing
Artists, Albums, Categories, and Songs in a MySQL database.
It also provides three reports based on the project requirements.

1. SOFTWARE REQUIREMENTS: 
• Python 3.12.x (recommended version: 3.12.7) . Please donot use python 3.13 or 3.14 above because it doesn't support mysql-connector-python.
• XAMPP (for MySQL server and phpMyAdmin)
• VS Code or any Python IDE
• Python libraries: mysql-connector-python

To install the MySQL connector, run:pip install mysql-connector-python
 


2. SETTING UP THE DATABASE IN XAMPP
1. Install xampp 8.2.4
1. Open XAMPP and go to manage servers and start all(it should turn green).
3. Search http://localhost/dashboard/ in your browser and once it opens click php my admin.
4. In phpMyAdmin, click "New" and create a database named:  songdb

5. Click the SQL tab and paste the following table-creation
   script into the SQL box, then click "Go":

CREATE TABLE Artist (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE Album (
    AlbumID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    Year INT
);

CREATE TABLE Category (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE Song (
    SongID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL
);

CREATE TABLE Plays (
    SongID INT,
    ArtistID INT,
    PRIMARY KEY (SongID, ArtistID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID),
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE IsIn (
    SongID INT,
    CategoryID INT,
    PRIMARY KEY (SongID, CategoryID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

CREATE TABLE IsOn (
    SongID INT,
    AlbumID INT,
    PRIMARY KEY (SongID, AlbumID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID),
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID)
);




3. SETTING UP THE PYTHON PROGRAM

Make sure the file db.py contains the correct MySQL connection:

import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # XAMPP default has NO password
        database="songdb"
    )


4. RUNNING THE PROGRAM:

1. Open the project folder in VS Code.
2. Make sure Python 3.12 is selected as the interpreter:
     - Press Ctrl + Shift + P
     - Select: Python: Select Interpreter
     - Choose Python 3.12.x

3. Open the Terminal in VS Code.
4. Navigate to the folder containing main.py.
5. Run the program using:

      python main.py

6. The main menu will appear with these options:

 MENU:
1. Artist CRUD
2. Album CRUD
3. Category CRUD
4. Song CRUD
5. Reports
0. Exit

7. Follow on-screen instructions to create, view, update, or delete items in the database.


5. REPORTS INCLUDED

The Reports menu provides:
1. List all songs performed by a selected artist.
2. List all artists with albums released in a given year.
3. List all albums that contain songs in a selected category.



6. DATA STORAGE AND PERSISTENCE

All information created through the Python application
  is stored in the MySQL database "songdb".
You can view all inserted data using phpMyAdmin.



7. PROBLEMS THAT MIGHT OCCUR:
If MySQL connection fails, make sure:
      - MySQL is running in XAMPP
      - The database name is exactly: songdb
      - The password in db.py matches your MySQL root password

If "module not found" appears:
      Reinstall connector:
          pip install mysql-connector-python

If VS Code runs Python 3.14 instead of 3.12:
      Use Python: Select Interpreter and choose 3.12

It might show up 1 error in db.py, its shows but the 
program still runs but if the program doesn't run, 
are using python 3.13 or above. Make sure to use python 3.12.x
