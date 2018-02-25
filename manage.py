#!/usr/bin/env python
# --*-- coding: utf-8 --*--
from app import create_app
from flask_script import Manager


app = create_app('default')
mamager =Manager(app)

@mamager.command
def dev():
	from livereload import Server
	live_server =Server(app.wsgi_app)
	live_server.watch('**/*.*')
	live_server.serve(open_url=False)

if __name__== '__main__':
	mamager.run()