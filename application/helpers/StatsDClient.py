import statsd

class StatsDClient(object):
    def __init__(self, client):
        self.counter = client.get_client(class_=statsd.Counter)
        self.timer = client.get_client(class_=statsd.Timer)

    def increment(self, metric):
        self.counter.increment(metric)

    def time(self, metric, time):
        self.increment(metric)
        self.timer.send(metric, time)
