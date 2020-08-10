from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RF(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=30)])
    pwd = PasswordField('Password',
                           validators=[DataRequired(), Length(min=8, max=30)])
    age = IntegerField("Age",
                       validators=[DataRequired()])
    residence = StringField('Residence',
                            validators=[DataRequired()])
    prof = StringField('Current Or Last Job',
                      validators=[])
    #|||||
    ach1 = StringField("Achievement 1",
                       validators=[DataRequired()])
    ach2 = StringField("Achievement 2",
                       validators=[DataRequired()])
    ach3 = StringField("Achievement 3",
                       validators=[])
    ach4 = StringField("Achievement 4",
                       validators=[])
    jobtitle = StringField("Job you want",
                       validators=[DataRequired()])
    #|||||
    employer = StringField("Employer",
                           validators=[])
    schoolname = StringField("School Name",
                             validators=[DataRequired()])
    degree = StringField("Degree",
                        validators=[DataRequired()])
    study = StringField("A Study you have Done",
                        validators=[])
    date = StringField("Date of Graduation",
                       validators = [])
    #|||||
    skill1 = TextAreaField("Skill 1",
                      validators=[])
    skill2 = TextAreaField("Skill 2",
                      validators=[])
    skill3 = TextAreaField("Skill 3",
                      validators=[])
    skill4 = TextAreaField("Skill 4",
                      validators=[])
    project1 = TextAreaField("Project 1",
                      validators=[])
    #|||||
    project2 = TextAreaField("Project 2",
                      validators=[])
    project3 = TextAreaField("Project 3",
                      validators=[])
    project4 = TextAreaField("Project 4",
                      validators=[])
    submit = SubmitField("Sign Up")

class LF(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired()])
    password = PasswordField("Password",
                             validators=[DataRequired()])
    submit = SubmitField("Sign In")
    
    
