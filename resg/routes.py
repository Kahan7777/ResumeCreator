import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from resg import app, db, bcrypt
from resg.forms import RF, LF, UA
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
        name = current_user.name + ".html"
        sname = "resg/static/" + current_user.name + ".pdf"
        f = open(name, "w")
        f.write("")
        f.close()
        f = open(sname, "w")
        f.write("")
        f.close()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register1.html", form=form)
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LF()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Unsuccesful", "danger")
            
    return render_template("login.html", form=form)
        
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
@app.route("/account")
@login_required
def account():
    skills = str(current_user.skills1) + " | " + str(current_user.skills2) + " | " + str(current_user.skills3) + " | " + str(current_user.skills4) + " | " 
    return render_template('account.html', skills=skills)

@app.route("/home-resumes")
@login_required
def home_resumes():
    return render_template("home-resume.html")
@app.route("/resume/1")
@login_required
def resume_1():
    return render_template("tem1.html")

@app.route("/resume/2")
@login_required
def resume_2():
    
    return render_template("tem2.html")
     

@app.route("/resume/3")
@login_required
def resume_3():
    
    return render_template("tem3.html")

@app.route("/resume/4")
@login_required
def resume_4():
    
    return render_template("tem4.html")

@app.route("/resume/download")
@login_required
def next():
    name = "Dear " + current_user.name + ","
    return render_template("download_tem.html", name=name)

@app.route("/account/update", methods=["GET", "POST"])
@login_required 
def accupd():
    form = UA()
    if form.validate_on_submit():
        current_user.name = form.name.data                             
        current_user.age = form.age.data
        current_user.residence = form.residence.data
        current_user.prof = form.prof.data 
        current_user.ach1 = form.ach1.data 
        current_user.ach2 = form.ach2.data 
        current_user.ach3 = form.ach3.data 
        current_user.ach4 = form.ach4.data 
        current_user.jobtitle = form.jobtitle.data 
        current_user.employer = form.employer.data 
        current_user.schoolname = form.schoolname.data 
        current_user.degree = form.degree.data 
        current_user.study = form.study.data 
        current_user.date = form.date.data 
        current_user.skills1 = form.skill1.data 
        current_user.skills2 = form.skill2.data 
        current_user.skills3 = form.skill3.data 
        current_user.skills4 = form.skill4.data 
        current_user.project1 = form.project1.data 
        current_user.project2 = form.project2.data 
        current_user.project3 = form.project3.data 
        current_user.project4 = form.project4.data

        db.session.commit()
        return redirect("/account")
    form.name.data = current_user.name
    form.residence.data = current_user.residence
    form.age.data = current_user.age
    form.ach1.data = current_user.ach1
    form.ach2.data = current_user.ach2
    form.ach3.data = current_user.ach3
    form.ach4.data = current_user.ach4
    form.prof.data = current_user.prof
    form.jobtitle.data = current_user.jobtitle
    form.employer.data = current_user.employer
    form.skill1.data = current_user.skills1
    form.skill2.data = current_user.skills2
    form.skill3.data = current_user.skills3
    form.skill4.data = current_user.skills4
    form.schoolname.data = current_user.schoolname
    form.study.data = current_user.study
    form.degree.data = current_user.degree
    form.date.data = current_user.date
    form.project1.data  = current_user.project1
    form.project2.data = current_user.project2
    form.project3.data = current_user.project3
    form.project4.data = current_user.project4
    return render_template("account-update.html", form=form)