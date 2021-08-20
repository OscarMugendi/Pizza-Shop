
from app.main.forms import ProfileUpdate,OrderForm
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user,current_user


from . import auth
from ..models import User
from .forms import UserRegistration, UserLogin
from .. import db

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistration()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    address=form.address.data,
                    contact=form.contact.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',
                           registratration_form=form,
                           title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginform = UserLogin()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=loginform.email.data).first()
        if user is not None and user.passwordVerification(
                loginform.password.data):
            login_user(user, loginform.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid Credentials!')
    title = "User Login"
    return render_template('auth/login.html',
                           login_form=loginform,
                           title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/profile')
@login_required
def profile():
    
    title = "Profile"

    return render_template('auth/profile.html', title=title)

@auth.route('/profile/update',methods=['POST','GET'])
@login_required
def updateuser():
    form=ProfileUpdate()
    if form.validate_on_submit():
        user=User.query.filter_by(username=current_user.username).first()
        user.bio= form.bio.data
        
        db.session.add(user)
        db.session.commit()
            
    
    return render_template('auth/update.html',form=form)

