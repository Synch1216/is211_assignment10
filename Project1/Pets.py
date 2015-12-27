import sqlite3

conn = sqlite3.connect('pets.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE person (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
);''')
print "Person Table created successfully";

conn.execute('''CREATE TABLE pet (
id INTEGER PRIMARY KEY,
name TEXT,
breed TEXT,
age INTEGER,
dead INTEGER
);''')
print "Pet Table created successfully";

conn.execute('''CREATE TABLE person_pet (
person_id INTEGER,
pet_id INTEGER
);''')
print "Person_pet Table created successfully";

conn.close()