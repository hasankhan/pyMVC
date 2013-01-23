from flask import current_app

class Cache(object):    
    def __init__(self, app = None):
        self.__app = app or current_app
        
    def get(self, key):
        return self.__app.cache.get(key)
    
    def set(self, key, value, expire = None):
        self.__app.cache.set(key, value, expire)    