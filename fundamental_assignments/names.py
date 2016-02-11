users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 }
otherusers = {
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for i in users:
  for key, value in enumerate(users[i]):
    spot = key + 1
    print "Students " + str(spot) + " This person's name is " + value['first_name'] + " " + value['last_name'] 

for i in otherusers:
  for key, value in enumerate(otherusers[i]):
    dot = key + 1
    print "Instructors " + str(dot) + " This person's name is " + value['first_name'] + " " + value['last_name']