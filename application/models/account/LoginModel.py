from wtforms import BooleanField, TextField, validators 
from core.SecureForm import SecureForm

class LoginModel(SecureForm):
    username = TextField('Username', [validators.Required()])
    remember_me = BooleanField('Remember me')