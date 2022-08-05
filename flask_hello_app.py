from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)

#link flask to db instance using SQLAlchemy
db = SQLAlchemy(app)

#Connect to db with flask by set configuration variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/dbname'

#turn of SQLAlchemy track notifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    name = db.Column(db.String(), nullable=False, unique=True)
    
    #use this attribute to debug
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
    
#create new table product with constraints
class Products(db.Model):
    
    #create product_id column
    product_id = db.Column(db.Integer,primary_key=True)
    
    #person id
    supplier_id = db.Column(db.Integer, ForeignKey('person.id'), nullable=False, default=1)
    
    #prices
    unit_price = db.Column(db.Float,db.CheckConstraint('unit_price>0'), nullable=False)
    
    #quantity
    quantity = db.Column(db.Integer, db.CheckConstraint('quantity>0'),nullable=False)

#create table command - creates table if table doesn't exist
db.create_all()


#run application with python decorator
@app.route('/')
def index():
    #create new object as first record in table persons
    person = Person.query.first()
    
    #return Hello and name attribute in person
    return "Hello " + person.name