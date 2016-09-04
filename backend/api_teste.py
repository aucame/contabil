from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@200.98.174.103/new_schema'
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'new_table'
	id = db.Column('idnew_table', db.Integer, primary_key=True)
	#data = db.Column('data', db.Unicode)