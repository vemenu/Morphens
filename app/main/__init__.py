#!user/bin/env python
# -*- coding:utf-8 -*-

'''main 蓝本子包构造文件'''
from flask import Blueprint

main = Blueprint('main', __name__)  # 实例化蓝本对象

#将views ，errors导入main蓝本
from . import views, errors  # 记得在工厂函数create_app()内注册蓝本

# 将权限常量加入上下文处理器，以便模板调用
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
