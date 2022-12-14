from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#link flask to db instance using SQLAlchemy
db = SQLAlchemy(app)

#Connect to db with flask by set configuration variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/dbname'

#currently db is an interface for interacting with our database
#db.Model lets us create & manipulate data models
#db.session lets us create and manipulate database transactions

#Create table called person
class Person(db.Model):
    #to customise the table name
    __tablename__ = 'persons'
    
    #create id column
    id = db.Column(db.Integer, primary_key=True)
    
    #create name column
    name = db.Column(db.String(), nullable=False)

#create table command - creates table if table doesn't exist
db.create_all()

#run application by calling path if no module imported, run app
if __name__ == '__main__':
    #set debug to true
    app.debug = True
    
    #run application
    app.run(host="0.0.0.0", port=3000)