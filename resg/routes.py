import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from resg import app, db, bcrypt
from resg.forms import RF
from resg.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    form = RF()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", form=form)

