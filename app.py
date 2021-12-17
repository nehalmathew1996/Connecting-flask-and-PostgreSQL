from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9136@localhost/Test'
db=SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    #To check available data types https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
    __tablename__='User'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    mobile=db.Column(db.String(50),unique=True)
    email=db.Column(db.String(50),unique=True)
    role_id=db.Column(db.Integer)
    status=db.Column(db.String(50))
    password=db.Column(db.String(50))
    created_at=db.Column(db.DateTime, default= datetime.now)

# To create database 
# In python script 
# from app import db
# db.create_all()

@app.route('/')
def index():
    return "<h1> PostgreSQL practice !! "


# Adding new students
@app.route('/add/<name>/<mobile>/<email>/<role_id>/<status>/<password>')
def total(name,mobile,email,role_id,status,password):
    user= User(name=name,mobile=mobile,email=email,role_id=role_id,status=status,password=password)
    # Adding user to session , prepares user to be added to the database
    db.session.add(user)
    # Save insert to data base
    db.session.commit()
    return '<h1>User Created Successfully'

if __name__ == "__main__":
    app.run(debug=True)

