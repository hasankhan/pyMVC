from core.Cache import Cache

class CachedRepository(object):
    def __init__(self, cache, repository):
        self._cache = cache or Cache()
        self._repository = repository
        
    def _get_or_add(self, key, getFunc, expire = None):
        value = self._cache.get(key)        
        if value is None:
            value = getFunc()
            self._cache.set(key, value, expire)
        return value