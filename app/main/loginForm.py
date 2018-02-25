# --*-- coding: utf-8 --*--
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required

class LoginForm(FlaskForm):
	name = StringField(label=u"用户名",validators=[Required()])
	pwd = PasswordField(label=u"密码",validators=[Required()])
	submit = SubmitField('Submit')

