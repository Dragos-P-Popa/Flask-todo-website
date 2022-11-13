# Used to delete all entries from database

from app import *

with app.app_context():
	models.Assignment.query.delete()
	
