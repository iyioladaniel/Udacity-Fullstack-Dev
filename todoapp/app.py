#import important modules
from flask import Flask, redirect, render_template, request, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import sys

#create new flask app with html templates in template folder
app = Flask(__name__,template_folder='template')

#set app configuration url
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'

#instatiate db with sql alchemy
db = SQLAlchemy(app)
#db = SQLAlchemy(app, session_options={"expire_on_commit":False})

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.title} {self.description}'

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
    if not error:
        return jsonify(body)



@app.route("/")
def index():
    return render_template('dynamic-index.html', data=Todo.query.all)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')