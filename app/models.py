from app import db

# DB models for an Assignment
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique identifier
    status = db.Column(db.String(28)) # Complete or Incomplete
    title = db.Column(db.String(500))  # Assignment title
    module = db.Column(db.String(500)) # Module code
    date = db.Column(db.Date) # Deadline
    notes = db.Column(db.String(500)) # Additional notes