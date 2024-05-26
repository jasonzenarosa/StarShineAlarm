import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('database/StarShine.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
               username     TEXT PRIMARY KEY,
               password     TEXT NOT NULL,
               language     TEXT NOT NULL,
               timezone     TEXT NOT NULL,
               theme        TEXT NOT NULL,
               twentyfourhr INTEGER NOT NULL
            )
''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alarms (
               alarm_id     INTEGER PRIMARY KEY AUTOINCREMENT,
               username     TEXT NOT NULL,
               label        TEXT NOT NULL,
               hour         INTEGER NOT NULL,
               minute       INTEGER NOT NULL,
               sound        TEXT NOT NULL,
               triv_topic   TEXT NOT NULL
            )
''')

# Commit the changes and close the connection
connection.commit()
connection.close()
