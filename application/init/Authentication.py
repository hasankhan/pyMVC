from flask.ext.login import LoginManager
from services.UserService import UserService
from flask import url_for, request

def setup_authentication(app):
    login_manager = LoginManager()
    login_manager.setup_app(app)
    login_manager.login_view = '/login'
    user_service = UserService()
    
    @login_manager.user_loader
    def load_user(userId):
        user = user_service.get_user(user_id=userId)
        return user        