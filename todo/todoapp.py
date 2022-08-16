from os import abort
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify
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
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=True)
    
    #use this attribute to debug
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.todo}, desc: {self.description}>'
    
#create table command - creates table if table doesn't exist
#comment out db.create since we are using migrations now.
#db.create_all()

#todo1 = Todo(todo="UAT form", description="I need to create a form to collect feedback for Intranet UAT")
#db.session.add(todo1)
#db.session.commit()


#run application with python decorator
@app.route('/todo/create', methods=['POST'])
def create_todo():
    body={}
    error = False
    try:
        todos = request.get_json()['todo']
        description = request.get_json()['description']
        todo = Todo(todo=todos, description=description)
        body['description'] = todo.description
        body['todo'] = todo.todo
        db.session.add(todo)
        db.session.commit()
    except:
        error=True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error ==  True:
            abort(400)
        else:
            return jsonify(body)



@app.route('/')
def index():
    return render_template('index_html', data=Todo.query.all())

#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)