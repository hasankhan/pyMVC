from datetime import datetime
from services.entities.Database import db, DEFAULT_TABLE_ARGS
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = DEFAULT_TABLE_ARGS

    id = db.Column('id', db.INTEGER(unsigned=True), primary_key=True)
    created = db.Column('created', db.TIMESTAMP, nullable=False, default=datetime.utcnow, index=True)
    is_admin = db.Column('isAdmin', db.BOOLEAN, nullable=False, default=False) 
    username = db.Column('username', db.VARCHAR(256), nullable=True)
    display_name = db.Column('displayName', db.VARCHAR(256), nullable=True)
    first_name = db.Column('firstName', db.VARCHAR(50), nullable=True)
    last_name = db.Column('lastName', db.VARCHAR(50), nullable=True)
    email = db.Column('email', db.VARCHAR(255), nullable=True)
    profile_pic = db.Column('profilePic', db.VARCHAR(255), nullable=True)
    gender = db.Column('gender', db.SMALLINT , nullable=True)
    
    #this method is required by flask-login
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return '<User {self.Username}>'.format(self=self)