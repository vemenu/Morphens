#!user/bin/env python
# -*- coding:utf-8 -*-

'''main 蓝本子包构造文件'''

from flask import Blueprint

#实例化蓝本对象
main = Blueprint('main',__name__)

#将views ，errors导入main蓝本
#记得在工厂函数create_app()内注册蓝本
from . import views,errors