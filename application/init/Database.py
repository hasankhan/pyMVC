from flask.ext.script import Command
from services.entities.Database import db
from services.entities import *

def setup_database(app):
    db.app = app
    db.init_app(app)
    app.db = db
    
class DropDatabase(Command):
    def run(self):
        db.drop_all()

class CreateDatabase(Command):
    def run(self):
        db.create_all()