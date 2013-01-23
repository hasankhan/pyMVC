from services.entities.Database import db
from services.entities.AppState import AppState
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from controllers.AdminController import *

def setup_admin(app):
    admin = Admin(app, url='/admin', index_view=HomeView(url='/admin'))
    
    admin.add_view(SampleView(name='Sample'))
    admin.add_view(ModelView(AppState, db.session))