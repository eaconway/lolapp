import os
from services import *

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DATABASE_URL = os.environ['SQLALCHEMY_DATABASE_URL']

def connect_to_db(app):
	db.app = app
	#app.config['SQLALCHEMY ']
	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)


class Color(db.Model):
	__tablename__ = 'colors'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)


if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print('Database connected at: {}'.format(DATABASE_URL))