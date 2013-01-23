from wtforms.ext.csrf.session import SessionSecureForm
from datetime import timedelta

class SecureForm(SessionSecureForm):
    SECRET_KEY = 'Enj09jpkj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
    TIME_LIMIT = timedelta(minutes=20)