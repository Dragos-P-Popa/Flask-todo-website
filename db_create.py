from config import SQLALCHEMY_DATABASE_URI
from app import db
from app import *
import os.path

with app.app_context():
	db.create_all()
