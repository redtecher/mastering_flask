from flask import render_template
from . import auth
from flask import redirect
from flask import request
from webapp.models import User
from flask import url_for,flash
from flask_login import login_user
from .forms import LoginForm,RegisterForm
@auth.route('/login',methods=['GET','POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user,remember=form.remember_me)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password')


    return render_template('auth/login.html',form=form)





@auth.route('/register',methods=['GET','POST'])
def register():
    pass