#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('pets.db')
print "Opened pets database successfully";

conn.execute("INSERT INTO PERSON (id,first_name,last_name,age) \
      VALUES (1, 'James','Smith', 41 )");

conn.execute("INSERT INTO PERSON (id,first_name,last_name,age) \
      VALUES (2, 'Diana','Greene', 23 )");

conn.execute("INSERT INTO PERSON (id,first_name,last_name,age) \
      VALUES (3, 'Sara','White', 27)");

conn.execute("INSERT INTO PERSON (id,first_name,last_name,age) \
      VALUES (4, 'William','Gibson', 23 )");

conn.execute("INSERT INTO PET (id, name,breed,age,dead) \
      VALUES (1, 'Rusty','Dalmation', 4,1 )");

conn.execute("INSERT INTO PET (id, name,breed,age,dead) \
      VALUES (2, 'Bella','Alaskan Malamute', 3,0 )");

conn.execute("INSERT INTO PET (id, name,breed,age,dead) \
      VALUES (3, 'Max','Cocker Spaniel', 1,0 )");

conn.execute("INSERT INTO PET (id, name,breed,age,dead) \
      VALUES (4, 'Rocky','Beagle', 7,0 )");

conn.execute("INSERT INTO PET (id, name,breed,age,dead) \
      VALUES (5, 'Rufus','Cocker Spaniel', 1, 0 )");

conn.execute("INSERT INTO PET (id, name,breed,age,dead) \
      VALUES (6, 'Spot','Bloodhound', 2,1 )");

conn.execute("INSERT INTO PERSON_PET (person_id, pet_id) \
      VALUES (1, 1 )");

conn.execute("INSERT INTO PERSON_PET (person_id, pet_id) \
      VALUES (1, 2 )");

conn.execute("INSERT INTO PERSON_PET (person_id, pet_id) \
      VALUES (2, 3 )");

conn.execute("INSERT INTO PERSON_PET (person_id, pet_id) \
      VALUES (2, 4)");

conn.execute("INSERT INTO PERSON_PET (person_id, pet_id) \
      VALUES (3, 5 )");

conn.execute("INSERT INTO PERSON_PET (person_id, pet_id) \
      VALUES (4, 6 )");




conn.commit()
print "Records is successfully inserted into Person table";
print "Records is successfully inserted into Pet table";
print "Records is successfully inserted into Person_Pet table";
conn.close()