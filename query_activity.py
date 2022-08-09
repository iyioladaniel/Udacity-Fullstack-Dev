'''
Person table

Implement a query to filter all users by name 'Bob'.
Implement a LIKE query to filter the users for records with a name that includes the letter "b".
Return only the first 5 records of the query above.
Re-implement the LIKE query using case-insensitive search.
Return the number of records of users with name 'Bob'


'''
from flask_hello_app import db, Person

Person.query.filter_by(name='Bob')

Person.query.filter(Person.name.like('%b%'))

Person.query.filter(Person.name.like('%b%')).limit(5)

Person.query.filter(Person.name.ilike('%b%'))

Person.query.filter(Person.name.like('Bob')).count()