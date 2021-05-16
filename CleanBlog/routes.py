from CleanBlog.models import User, Post
from flask import render_template, flash, redirect, url_for
from CleanBlog import app, db
from CleanBlog.forms import RegisterForm, LoginForm
from flask_login import login_user

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', title = 'HOME')

@app.route("/about")
def about():
    return render_template('about.html', title = 'ABOUT')

@app.route("/post")
def post():
    return render_template('post.html', title = 'POST')

@app.route("/contact")
def contact():
    return render_template('contact.html', title = 'CONTACT')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.name.data} account created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'REGISTER', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('test')
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'Logged In successfully', 'success')
            return redirect(url_for('index'))
        else :
            flash(f'Your email or password wrong !!!', 'danger')
    return render_template('login.html', title = 'LOGIN', form=form)