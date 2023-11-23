from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form=NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
        form=form, name='',
        known=session.get('known', False),
        current_time=datetime.utcnow())