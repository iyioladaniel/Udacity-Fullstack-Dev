from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_migrate import Migrate

app = Flask(__name__)

#link flask to db instance using SQLAlchemy
db = SQLAlchemy(app)

#Connect to db with flask by set configuration variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todo'

#turn of SQLAlchemy track notifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)

#currently db is an interface for interacting with our database
#db.Model lets us create & manipulate data models
#db.session lets us create and manipulate database transactions

#Create table called person
class Todo(db.Model):
    #to customise the table name
    __tablename__ = 'todo'
    
    #create id column
    id = db.Column(db.Integer, primary_key=True)
    
    #short name for todo
    todo = db.Column(db.String(),nullable=False, unique=False)
    #create name column
    description = db.Column(db.String(), nullable=True)
    
    #use this attribute to debug
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.todo}, desc: {self.description}>'
    
#create table command - creates table if table doesn't exist
db.create_all()

todo1 = Todo(todo="UAT form", description="I need to create a form to collect feedback for Intranet UAT")
db.session.add(todo1)
db.session.commit()

'''
#run application with python decorator
@app.route('/')
def index():
    #create new object as first record in table persons
    todo_view = Todo.query.first()
    
    #return Hello and name attribute in person
    return "Hello " + todo_view.todo + "\nHere's the description: " + todo_view.description

'''