import statsd
from helpers.StatsDClient import StatsDClient

def setup_stats(app):
       host = app.config.get('STATSD_HOST')
       port = app.config.get('STATSD_PORT')
       name = app.config.get('STATSD_PREFIX', '')

       connection = statsd.Connection(host=host, port=port, sample_rate=1)
       client =  statsd.Client(name, connection)
       app.stats = StatsDClient(client)
