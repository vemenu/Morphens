#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    '''Base config class'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'Flasky Admin <flask@example.com>'

    @staticmethod
    def init_app(self):
        pass

class DevelopemntConfig(Config):
    '''Development config class'''
    DUBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    '''Test config class'''
    Testing = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///'+ os.path.join(basedir,'data_test.sqlite')

class ProductionConfig(Config):
    '''Production config class'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
    'development':DevelopemntConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopemntConfig
}
