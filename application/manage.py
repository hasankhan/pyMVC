from flask.ext.script import Manager, Server
from flask.ext.assets import ManageAssets
from init import create_app
from init.Database import DropDatabase, CreateDatabase

if __name__ == '__main__':
    manager = Manager(create_app())
    manager.add_command('runserver', Server(host='0.0.0.0'))
    manager.add_command('assets', ManageAssets())
    manager.add_command('dropdb', DropDatabase())
    manager.add_command('createdb', CreateDatabase())
    manager.run()