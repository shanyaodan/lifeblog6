# _*_ coding: utf-8 _*_
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '\xf2\x95\xc6\x92[%\xe4bR\xf7\x15\xf5i\xeb7\xd3`Q|4\xb1e$/'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[DYC]'
    FLASK_MAIL_SENDER = 'DYC <woshiduyongchang@163.com>'
    FLASK_ADMIN = "脆弱的杜大哥"

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = ''
    MAIL_PORT = 123
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'woshiduyongchang@163.com'
    MAIL_PASSWORD = '735383226'
    SQLALCHEMY_DATABASE_URI ='mysql://root:mysql@localhost/my_blog'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI =''

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/my_blog'

config ={
    'development': DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}