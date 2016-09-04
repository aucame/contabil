from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@200.98.174.103/new_schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class teste(db.Model):
	__tablename__ = 'new_table'
	id = db.Column('idnew_table', db.Integer, primary_key=True)

e = teste.query.all()
print(e)

for ex in e:
	print(ex.id)
