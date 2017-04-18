#!user/bin/env python
# -*- coding:utf-8 -*-

'''蓝本中的路由'''

from datetime import datetime

from flask import abort
from flask import render_template,session,redirect,url_for

from app.models import User
from . import main
from .forms import NameForm


@main.route('/',methods = ['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #...
        return redirect(url_for('main.index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           know = session.get('know',False),
                           current_time = datetime.utcnow()
                           )


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
