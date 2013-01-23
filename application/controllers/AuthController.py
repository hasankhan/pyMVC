from flask import request, redirect, url_for, jsonify
from core.Controller import Controller
from models.account.LoginModel import LoginModel
from services.UserService import UserService
from flask.ext.login import login_user, logout_user

class AuthController(Controller):
    def __init__(self, action_name, user_service = None):
        super(AuthController, self).__init__(action_name)
        self.__user_service = user_service or UserService()

    def login(self):
        model = LoginModel(request.form, csrf_context=self._session)
        next = request.args.get('next', url_for('index'))
        return self._view(model=model, next = next)
        
    def login_post(self):
        model = LoginModel(request.form, csrf_context=self._session)
        next = request.args.get('next', url_for('index'))
        if model.validate():
            user = self.__user_service.get_user(username = model.username.data)
            if user is None:
                model.username.errors.append('invalid username')
            else:
                login_user(user, model.remember_me.data)
                return redirect(next)
        return self._view('login.html', model=model, next = next)
        
    def user(self):
        result = {'DisplayName': self._user.DisplayName if hasattr(self._user, 'DisplayName') else None}
        return jsonify(result)
        
    def logout(self):
        logout_user()
        return redirect (url_for('index'), 302)            