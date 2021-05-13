# SQL 

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
dbs = SQLAlchemy(app)

class Human(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    name = dbs.Column(dbs.String)
    age = dbs.Column(dbs.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Name: {self.name} Age: {self.age}'