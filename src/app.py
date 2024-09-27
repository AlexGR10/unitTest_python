from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_restful import Api, Resource, reqpars, abort, fields, marshal_with, abort

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def _repr_(self):
        return f"User (username ={self.username}, email = {self.email})"