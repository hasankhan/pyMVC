from flask import Flask
from init.Routing import register_routes
from init.Configuration import initialize_config
from init.Logging import setup_logging
from init.Database import setup_database
from init.Authentication import setup_authentication
from init.Caching import setup_caching
from init.Bundles import setup_bundles
from init.Stats import setup_stats
from init.Admin import setup_admin

import os

def create_app():
	instance_path = os.path.abspath(os.path.dirname(__file__) + '/..')
	template_folder = os.path.join(instance_path, 'views')
	static_folder = os.path.join(instance_path, 'statics')
    
	app = Flask('application', static_folder=static_folder, template_folder=template_folder, instance_path=instance_path)
	app.secret_key = 'application'
		
	initialize_config(app)
	
	setup_logging(app)
	setup_database(app)
	setup_authentication(app)
	setup_caching(app)
	setup_bundles(app)
	setup_stats(app)
	setup_admin(app)

	register_routes(app)    
	
	return app


