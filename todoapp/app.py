#import important modules
import sys
from flask_migrate import Migrate
import requests
from flask import (Flask, abort, jsonify, redirect, render_template, request,
                   url_for, make_response)
from flask_sqlalchemy import SQLAlchemy

#create new flask app with html templates in template folder
app = Flask(__name__,template_folder='template')

#set app configuration url
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'

#instatiate db with sql alchemy
db = SQLAlchemy(app)
#db = SQLAlchemy(app, session_options={"expire_on_commit":False})

migrate = Migrate(app,db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean,nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.title} {self.description}>'

class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)

    def __repr__(self):
        return f'<TodolList {self.id} {self.name}>'

db.create_all()

@app.route('/todoapp/create', methods=['POST'])
def create():
    error = False
    body = {}
    try:
        title1 = request.get_json()['title']
        desc1 = request.get_json()['description']

        todo1 = Todo(title=title1,description=desc1)
        db.session.add(todo1)
        db.session.commit()

        body['title'] = todo1.title
        body['description'] = todo1.description
    #return render_template('dynamic-index.html',data=Todo.query.all)

    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/todoapp/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except: 
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

@app.route('/todoapp/<todo_id>/delete', methods=['DELETE'])
def set_delete_todo(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except: 
        db.session.rollback()
    finally:
        db.session.close()
    return make_response(jsonify({'success': True}), 201)

@app.route("/")
def index():
    return render_template('dynamic-index.html', todos=Todo.query.order_by(Todo.id).all)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
