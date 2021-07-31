'''from flask import Flask, render_template, session, request, flash, url_for, redirect

from shop_app import app, bcrypt, db
from shop_app.admin.models import User
from shop_app.admin.forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/home.html")

@app.route('/inventory')
def inventory():
    return render_template("/inventory.html")

@app.route('/Autoparts')
def Autoparts():
    return render_template("/Autoparts.html")

@app.route('/contact')
def contact():
    return render_template('/Contact.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data}, Welcome and Thank you for registering' , 'success')
        return redirect(url_for('index'))
    return render_template('admin/register.html', form = form, title = "Rgistration Page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    return render_template('admin/login.html', form = form, title = "Login Page")
'''