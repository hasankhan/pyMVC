from flask.ext.assets import Environment, Bundle
from webassets.loaders import YAMLLoader
   
def setup_bundles(app):
    assets_env = Environment(app)
    assets_env.url = '/statics'
    assets_env.manifest = 'file:Compiled/static-manifest-version'
    assets_env.cache = False
    assets_env.auto_build = False
    assets_env.debug = app.config.get('DEVELOPMENT') == True

    # load and register bundles
    config_path = app.instance_path + '/config/asset_bundles.yaml'
    bundles = YAMLLoader(config_path).load_bundles()
    for name, bundle in bundles.iteritems():
       assets_env.register(name, bundle)

    app.assets_env = assets_env