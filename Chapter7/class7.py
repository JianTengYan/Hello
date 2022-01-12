#Using make_db_classes.
import shelve
from class5 import Person 
from class6 import Manager

bob =Person ('Bob Smith', 42, 30000, 'software') 
sue =Person ('Sue Jones', 45, 40000, 'hardware')
tom =Manager('Tom Doe', 50, 50000)

db= shelve.open('class-shelve')
db['bob'] =bob
db['sue'] = sue
db['tom'] =tom
db.close()

#Using dump_db_classes

import shelve 
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)

bob = db ['bob']
print (bob.lastName()) 
print (db['tom'].lastName())

#Using update_db_classes

import shelve
db = shelve.open('class-shelve')

sue = db['sue'] 
sue.giveRaise(.25)
db['sue'] =sue

tom= db['tom']
tom.giveRaise(.20) 
db['ton'] = tom 
db.close()
