import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from resg import app, db, bcrypt
from resg.forms import RF, LF
from resg.models import User
from flask_login import login_user, current_user, logout_user, login_required
#SlenderBot Chromium
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['POST','GET'])
def register():
    form = RF()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.pwd.data).decode('utf-8')
        usernew = User(name = form.name.data,
                       password = hashed_password,
                       age = form.age.data,
                       residence = form.residence.data,
                       prof = form.prof.data,
                       ach1 = form.ach1.data,
                       ach2 = form.ach2.data,
                       ach3 = form.ach3.data,
                       ach4 = form.ach4.data,
                       jobtitle = form.jobtitle.data,
                       employer = form.employer.data,
                       schoolname = form.schoolname.data,
                       degree = form.degree.data,
                       study = form.study.data,
                       date = form.date.data,
                       skills1 = form.skill1.data,
                       skills2 = form.skill2.data,
                       skills3 = form.skill3.data,
                       skills4 = form.skill4.data,
                       project1 = form.project1.data,
                       project2 = form.project2.data,
                       project3 = form.project3.data,
                       project4 = form.project4.data)
        #we can try and encrypt stuff but I don't think it is nessesary... We can do that after the project is finished!
        db.session.add(usernew)
        db.session.commit()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", form=form)
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LF()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Uncessesful", "danger")
            
    return render_template("login.html", form=form)
        
