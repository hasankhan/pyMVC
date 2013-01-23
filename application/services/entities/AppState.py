from datetime import datetime
from services.entities.Database import db, DEFAULT_TABLE_ARGS

class AppState(db.Model):
    __tablename__ = 'appStates'
    __table_args__ = DEFAULT_TABLE_ARGS

    Id = db.Column('id', db.INTEGER(unsigned=True), primary_key=True)
    Name = db.Column('name',  db.VARCHAR(256), nullable=False, index=True)
    Value = db.Column('value',  db.VARCHAR(256), nullable=False)
    
    def __repr__(self):
        return '<AppState {self.Id}:{self.Name}={self.Value}>'.format(self=self)