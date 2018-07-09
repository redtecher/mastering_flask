from .forms import LoginForm,RegisterForm
from . import login
from flask import redirect,render_template,flash
from flask import url_for
from webapp.models import User

@login.route('/login',methods=['GET','POST'])
def login1():
    form =LoginForm()
    if form.validate_on_submit():
        flash("you have been logged in",category = "success")
        return redirect(url_for('main.home'))

    return render_template('login.html',form=form)


@login.route('/logout',methods=['GET','POST'])
def logout():
    flash('You have been logged out',category="success")
    return redirect(url_for('main.home'))


@login.route('/register',methods=['GET','POST'])
def register():
    form =RegisterForm()
    if form.validate_on_submit():
        new_user = User()
        new_user.username = form.username.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)      
        db.session.commit()
        flash('you user have been created ,Please login',category="success")
        return redirect(url_for('login.login1'))

    return render_template('register.html',form=form)  