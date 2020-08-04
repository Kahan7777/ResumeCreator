from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RF(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=30)])
    sirname = StringField('Sirname',
                           validators=[DataRequired(), Length(min=2, max=30)])
    age = IntegerField("Age",
                       validators=[DataRequired(), Length(min=16, max=90)])
    residence = StringField('Residence',
                            validators=[DataRequired()])
    job = StringField('Current Or Last Job',
                      validators=[DataRequired(), Length(min=16,max=90)])
    Submit = SubmitField("Sign Up")

    
    
    
