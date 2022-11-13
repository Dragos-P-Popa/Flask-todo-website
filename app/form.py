from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired

#WTForm for creating a new <Assignment>
class AssignemntForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='Title can\'t be blank')]) # Must exist. Title
    module = StringField('Module', validators=[DataRequired(message='Module code can\'t be blank')]) # Must exist. Module code
    date = DateField('Deadline', validators=[]) # Deadline
    notes = TextAreaField('Notes', validators=[]) # Additional notes