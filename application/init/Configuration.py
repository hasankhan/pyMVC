from configobj import ConfigObj
from config.Settings import settings
import os

def initialize_config(app):
    config_name = os.environ.get('APP_CONFIG', 'development')
    
    cfg_file = "{0}/config/{1}.cfg".format(app.instance_path, config_name)
    config_obj = ConfigObj(cfg_file)
    
    settings_obj = settings[config_name]
    
    # merge cfg settings with py settings
    for key, value in config_obj.iteritems():
           setattr(settings_obj, key, value)
           
    app.config.from_object(settings_obj)
    