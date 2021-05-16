from CleanBlog.models import User, Post
from flask import render_template, flash, redirect, url_for
from CleanBlog import app, db
from CleanBlog.forms import PostForm, RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', title = 'HOME',posts = posts)

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.is_submitted():
        print('test')
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'Logged In successfully', 'success')
            return redirect(url_for('index'))
        else :
            flash(f'Your email or password wrong !!!', 'danger')
            return render_template('login.html', title = 'LOGIN', form=form)
    return render_template('login.html', title = 'LOGIN', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f'Logout successfully', 'success')
    return redirect(url_for('index'))

@app.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, subtitle=form.subtitle.data, post_text=form.post_text.data, user = current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Post is created', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title = 'Create Post', form=form)
