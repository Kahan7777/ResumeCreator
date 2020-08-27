import os
import pdfkit
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from resg import app, db, bcrypt
from resg.forms import RF, LF
from resg.models import User
from flask_login import login_user, current_user, logout_user, login_required
import requests


def r_3_download():
    name = current_user.name + ".html"
    sname = current_user.name + ".pdf"
    f = open(name, "w")
    f.write(f"""
    
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Untitled Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

            <!-- jQuery library -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            
            <!-- Popper JS -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            
            <!-- Latest compiled JavaScript -->
            <link href="https://fonts.googleapis.com/css?family=Calistoga" rel="stylesheet">
            <link href='https://fonts.googleapis.com/css?family=Forum' rel='stylesheet'>
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
        </head>
        <body class="img-fluid">
        <div class="row" style="background: url(file:///D:/Python/RG/resg/static/bgimg.jpg)">
            <div class="col-lg-3 offset-lg-2"><img src="file:///D:/Python/RG/resg/static/logo.jfif" class="rounded-circle img-thumbnail img-fluid" alt="Image"></div>
            <div class="col-lg-6">
                <h1 class="lead" style="font-size:400%">{ current_user.name }
                </h1>
                <br>
                <h4 style="font-family:'Forum'; ">{ current_user.prof }</h4>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-9">
            
        <div class="row">
        <div class="col-lg-2"></div>
                <div class="col-lg-2" style="background-color:#CFCFCF"><br><p style="font-size:125%">Achievements</p></div>
                <div class="col-lg-7">
                    <br>
                <div class="row">
                    <div class="col-md-1"><i class="fas fa-angle-double-right" style="font-size:170%; color:#1CDB1F"></i></div>
                        <div class="col-md-10">
                            <div class="card bg-light pl-3">

                                { current_user.ach1 }<br>
                                { current_user.ach2 }<br>
                                { current_user.ach3 }<br>
                                { current_user.ach4 }<br>

                            </div>
                    </div>
                </div>
                </div>
        </div>
            <div class="row">
            <div class="col-lg-2"></div>
            <div class="col-lg-2" style="background-color:#CFCFCF"><br><p style="font-size:125%">Skills</p></div>
            <div class="col-lg-7">
                <br>
                <div class="row">
                    <div class="col-md-1"><i class="fas fa-angle-double-right" style="font-size:170%; color:#1CDB1F"></i></div>
                        <div class="col-md-10">
                            <div class="card bg-light pl-3">

                                { current_user.skills1 }<br>
                                { current_user.skills2 }<br>
                                { current_user.skills3 }<br>
                                { current_user.skills4 } <br>

                            </div>
                    </div>
                </div>
            </div>
            </div>
            <div class="row">
                <div class="col-lg-2"></div>
                <div class="col-lg-2" style="background-color:#CFCFCF"><br><p style="font-size:125%">Projects</p></div>
                <div class="col-lg-7">
                    <br>
                <div class="row">
                    <div class="col-md-1"><i class="fas fa-angle-double-right" style="font-size:170%; color:#1CDB1F"></i></div>
                        <div class="col-md-10">
                            <div class="card bg-light pl-3">

                                { current_user.project1 }<br>
                                { current_user.project2 }<br>
                                { current_user.project3 }<br>
                                { current_user.project4 } <br>

                            </div>
                    </div>
                </div>
                </div>
        </div>
        </div>		
        <div class="col-lg-3">
                <div class="row">
                    <div class="col-md-6">
                        <p>Address</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.residence }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Phone No.</p>
                    </div>
                    <div class="col-md-6">
                        <p>+91 999955551</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Jobtitle</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.jobtitle }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Employer</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.employer }</p>
                    </div>
                </div>
            <hr class="alert-dark">
                <div class="row">
                    <div class="col-md-6">
                        <p>School Name</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.schoolname }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Degree</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.degree }</p>
                    </div>
                </div>
            <div class="row">
                    <div class="col-md-6">
                        <p>Study</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.study }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Date of Graduation</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.date }</p>
                    </div>
                </div>
            </div>
        </div>
        <!-- body code goes here -->
    </html>""")
    f.close()
    
    document = request.base_url
    pdf = requests.get(f'http://api.pdflayer.com/api/convert?access_key=5da898cb4c3452684eccbb64db2c3c32&document_url={document}')
    f = open('resg/pdfs/sankar.pdf', 'wb')
    f.write(pdf.content)
    f.close()

    '''html = render_template(
        name)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response'''














#SlenderBot Chromium
@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

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
        name = form.name.data + ".html"
        sname = form.name.data + ".pdf"
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
    r_3_download()
    name = "file:///D:/Python/RG/"+ current_user.name + ".pdf"
    name = "file:///D:/Python/RG/templates/login.html"

    print(name)
    return render_template("tem3.html", name=name)

@app.route("/resume/4")
@login_required
def resume_4():
    return render_template("tem4.html")


@app.route("/resume/download/next")
@login_required
def next():
    return render_template("download.html")