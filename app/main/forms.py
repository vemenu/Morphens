#!user/bin/env python
# -*- coding:utf-8 -*-

'''登录表单'''

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('what is  you name?', validators=[Required()])
    pwd = PasswordField('please input passwd')
    submit = SubmitField('Submit')
