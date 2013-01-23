from flask import request, flash, redirect, url_for, jsonify
from core.Controller import Controller
from models.account.RegisterModel import RegisterModel
from services.UserService import UserService, DuplicateUserException
from services.entities.User import User

class AccountController(Controller):

    def __init__(self, action_name, user_service = None):
        super(AccountController, self).__init__(action_name)        
        self.__user_service = user_service or UserService()    
        
    def register(self):
        model = RegisterModel(request.form, csrf_context=self._session)
        return self._view(model=model)

    def register_post(self):
        model = RegisterModel(request.form, csrf_context=self._session)
        if model.validate():
            user = User()
            user.username = model.username.data
            user.email = model.email.data
            user.ignite_id = 'blah'

            try:                
                self.__user_service.create_user(user)
                self._session['username'] = model.username.data
                flash('You were successfully registered in')
                return redirect(url_for('index'))
            except DuplicateUserException:
                    model.username.errors.append('user already exists')
        
        return self._view('register.html', model=model)
        
    def user_exists(self):
        username = request.args.get('username', '')
        exists = self.__user_service.get_user(username = username) is not None
        return jsonify(result = exists)        