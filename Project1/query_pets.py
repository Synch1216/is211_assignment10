#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('pets.db')
conn = conn.cursor()
print "Connect to pets database successfully";

person_id =''
while person_id !=-1:
  print ''
  person_id = input("Please enter Person_Id:")
  conn.execute("SELECT id FROM person WHERE id = ?", (person_id,))
  data=conn.fetchone()
  if data is None:
        print 'Person Id',person_id,'not exists.'
  else:
    for row in conn.execute('SELECT first_name,last_name,age FROM Person WHERE id =?',(person_id,)) :
      print row[0],row[1],',',row[2],'years old'
      print 'Got data successfully'

  for row2 in conn.execute('SELECT DISTINCT Person.first_name, Person.last_name,Pet.name,Pet.breed,Pet.age FROM Person,Pet, person_pet  where Person.id = person_pet.person_id AND person_pet.pet_id =pet.id and person.id==? ',(person_id,)):
     print row2[0],row2[1],'owned',row2[2],',a',row2[3],'that was',row2[4],'year old.'

print('Thank you')

conn.close()