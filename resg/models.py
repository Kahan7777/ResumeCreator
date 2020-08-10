from resg import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(ident):
  return User.query.get(int(ident))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #for login/register . Name will also be used in the Resume
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    #Now basic things that will be displayed near the heading(sub)
    age = db.Column(db.Integer)
    residence = db.Column(db.String(1000))
    prof = db.Column(db.String(100))
    
    #achievments
    ach1 = db.Column(db.String(100))
    ach2 = db.Column(db.String(100))
    ach3 = db.Column(db.String(100))
    ach4 = db.Column(db.String(100))

    #experience 
    jobtitle = db.Column(db.String(100))
    employer = db.Column(db.String(100))

    #Education
    schoolname = db.Column(db.String(100))
    degree = db.Column(db.String(100))
    study = db.Column(db.String(100))
    date = db.Column(db.String(100))

    #skills
    skills1 = db.Column(db.String(100))
    skills2 = db.Column(db.String(100))
    skills3 = db.Column(db.String(100))
    skills4 = db.Column(db.String(100))

    #Projects
    project1 = db.Column(db.String(10000))
    project2 = db.Column(db.String(10000))
    project3 = db.Column(db.String(10000))
    project4 = db.Column(db.String(10000))
    
    
