from core.Controller import Controller
from flask.ext.login import login_required

class HomeController(Controller):

    def index(self):
        self._logger.debug('home page served')
        name = getattr(self._user, 'username', 'unknown')
        message = u'Welcome %(name)s' % {'name': name}
        self._app.stats.increment('index')

        return self._view(message = message)
        
    @login_required
    def client(self, **args):
        import datetime
        
        now = datetime.datetime.now()        
        self._logger.debug('going to client page')
        return self._view(now=str(now))
