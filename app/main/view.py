# --*-- coding: utf-8 --*--
from . import main
from flask import render_template
from .loginForm import LoginForm

@main.route('/', methods=['GET', 'POST'])
def index():
	return  render_template('cust_index.html',title="home")
@main.route('/android')
def androidpage():
	return  render_template('cust_index.html',title="android")
@main.route('/about')
def about():
	return  render_template('cust_index.html',title="about")

@main.route('/login',methods=['GET', 'POST'])
def login():
	form = LoginForm()

	return  render_template('login.html',title="login",form = form)
