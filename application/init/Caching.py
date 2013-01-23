from werkzeug.contrib.cache import SimpleCache

def setup_caching(app):
    app.cache = SimpleCache()