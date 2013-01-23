from flask import current_app as app, session, request, render_template
from flask.views import View
from flask.ext.login import current_user

from core.ViewLocator import ViewLocator
from core.Cache import Cache

import logging
import inspect
import re

class Controller(View):    
    __mobileAgentPattern = re.compile('iphone|ipad|ipod|android|blackberry|mini|windows\sce|palm');
    
    def __init__(self, action_name):
        super(Controller, self).__init__()
        
        self.__action_name = action_name
        self._app = app
        self._session = session
        self._logger = logging.getLogger(app.config['ENVIRONMENT'])
        self._cache = Cache()
        self._user = current_user

    def dispatch_request(self, *args, **kwargs):
        action = getattr(self, self.__action_name, None)
        if action is None:
            raise Exception('action_name', 'Action {0} not found'.format(self.__action_name))
        return action(*args, **kwargs)    
        
    def _is_mobile(self):        
        is_mobile = Controller.__mobileAgentPattern.search(request.user_agent.string.lower()) is not None;
        return is_mobile;
        
    def resolve_device_name(self):
        if self._is_mobile():
            return 'mobile'
        return '';
        
    def _view(self, view_name = None, **kwargs):
        if view_name is None:
            view_name = inspect.stack()[1][3];
            
        view_path = ViewLocator.resolve_view_name(self, view_name)        
        
        if 'app' not in kwargs:
            kwargs['app'] = self._app
        
        return render_template(view_path, **kwargs)             