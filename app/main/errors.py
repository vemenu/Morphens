#!user/bin/env python
# -*- coding:utf-8 -*-

'''错误处理程序'''

from flask import render_template
from . import main


#蓝本内不要使用errorhandler修饰，要使用app_errorhandler修饰器修饰
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

