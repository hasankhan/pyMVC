from flask.ext.admin import AdminIndexView, BaseView, expose
from flask.ext.login import current_user

class ProtectedView(object):
    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_admin

class HomeView(ProtectedView, AdminIndexView):
    @expose()
    def index(self):
        return self.render('admin/index.html')

class SampleView(ProtectedView, BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/sample.html')