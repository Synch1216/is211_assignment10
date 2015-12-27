import sqlite3

conn = sqlite3.connect('music.db')
print "Created and Opened database successfully";

conn.execute('''CREATE TABLE artist (
id INTEGER PRIMARY KEY,
name TEXT,
album_name TEXT
);''')
print "Artist Table created successfully";

conn.execute('''CREATE TABLE Album (
album_name TEXT PRIMARY KEY,
artist_name TEXT
);''')
print "Album Table created successfully";

conn.execute('''CREATE TABLE Song (
song_name TEXT PRIMARY KEY,
artist_name TEXT,
track_name TEXT,
Song_Time Float
);''')
print "Song Table created successfully";


conn.close()