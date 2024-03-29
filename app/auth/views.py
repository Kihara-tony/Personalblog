from flask import render_template,redirect,url_for,flash,request       
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db  
from ..email import mail_message

user = [
    {
        'email':'tonykiharatonkin6@gmail.com',
        'password':'tonyqtjds2'
    }
]

@auth.route('/login',methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if login_form.email.data == 'tonykiharatonkin6@gmail.com' and login_form.password.data == 'tonyqtjds2':
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.blogs'))
        flash('Invalid Author or Password')
    title = 'My One Time Blog Login'
    return render_template('auth/login.html',title = title,login_form = login_form)
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.blogs'))


@auth.route('/register',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message('Welcome to My One Time Blog App','email\welcome_user',user.email,user = user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form)