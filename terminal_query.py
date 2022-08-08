import flask_hello_app
from flask_hello_app import db, Person

 
# Select all persons with name Amy
Person.query.filter_by(name='Amy').all()


results = Person.query.filter_by(name='Amy').all()
results[0]
results[0].name
results[0].id

#create new object i.e. record called Bob
person = Person(name='Bob')
person.name

#Add created record to db
db.session.add(person)
db.session.commit()

#Select all records in Person class ie table
Person.query.all()

#Create multiple records
person1 = Person(name='Anne')
person2 = Person(name='David')

#Save multiple records in db at once
db.session.add_all([person1,person2,Person(name='Rachael')])
db.session.commit()
Person.query.all()