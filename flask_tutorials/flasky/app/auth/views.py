from flask import render_template, redirect, request, url_for, flash
from . import auth
from ..models import User
from .forms import LoginForm

from flask_login import login_required, login_user, logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next=request.args.get('next')
            if next is None or not next.startswith('/'):
                next=url_for('main.index')
            return redirect(next)
        flash('Invalid Username or Password')
    return render_template('auth/login.html', form=form)


@auth.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowd'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('main.index'))
