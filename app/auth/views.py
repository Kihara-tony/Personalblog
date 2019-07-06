from flask import render_template,redirect,url_for,flash,request       
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db  
from ..email import mail_message

user = [
    {
        'email':'tonykiharatonkin6@gmail.com'
        'password':'tonyqtjds2'
    }
]

@auth.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if form.email.data == 'tonykiharatonkin6@gmail.com' and form.password.data == 'tonyqtjds2':
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid Author or Password')