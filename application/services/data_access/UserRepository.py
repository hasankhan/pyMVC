from services.entities.Database import db
from services.entities.User import User
from services.data_access.CachedRepository import CachedRepository

class UserRepository:
    def get_user_by_username(self, username):
        return db.session.query(User)\
                         .filter(User.username == username)\
                         .first()
                         
    def get_user_by_id(self, id):
        return db.session.query(User)\
                        .filter(User.id == id)\
                        .first()
                        
    def add_user(self, user):
        db.session.add(user)
        db.session.commit()
        
    def update_user(self, user):
        db.session.merge(user)
        db.session.commit()
                
class CachedUserRepository(CachedRepository):
    def __init__(self, cache = None, repository = None):
        super(CachedUserRepository, self).__init__(cache, repository or UserRepository())
        
    def get_user_by_username(self, username):
        return self._get_or_add('user_name:{}'.format(username), lambda: self._repository.get_user_by_username(username))
        
    def get_user_by_id(self, id):
        return self._get_or_add('user_id:{}'.format(id), lambda: self._repository.get_user_by_id(id))            
        
    def add_user(self, user):
        self._repository.add_user(user)
        
    def update_user(self, user):
        self._repository.update_user(user)
        
        
    