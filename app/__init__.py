# --*-- coding: utf-8 --*--
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
bootstrap = Bootstrap()
monent = Moment()
nav = Nav();
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	monent.init_app(app)

	bootstrap.init_app(app)
	nav.register_element("top",
						 Navbar("lifeblog", View(u"首页", 'main.index'),
								View("android", 'main.androidpage'),
								View(u'关于', 'main.about')))
	nav.init_app(app)
	db.init_app(app)
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app
