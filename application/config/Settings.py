
class BaseSettings(object):
    ENABLE_ASYNC = True
    
    LOGGING_CONFIG = {
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
               'formatter': 'short',
               'level': 'DEBUG'
           }
       },
       'formatters': {
           'short': {
               'format': '%(levelname)s: %(message)s'
           },
           'full': {
               'format': '%(levelname)s|%(asctime)s|%(pathname)s:%(lineno)s|%(message)s'
           }
       },
       'loggers': {
           'development': {
               'handlers': ['console'],
               'level': 'DEBUG'
           },
           'staging': {
               'handlers': ['console'],
               'level': 'DEBUG'
           },
           'production': {
               'handlers': ['console'],
               'level': 'DEBUG'
           },
       },
       'version': 1
   }
    
class DevelopmentSettings(BaseSettings):
    ENVIRONMENT = 'development'
    DEVELOPMENT = True
    ENABLE_ASYNC = True    
    
class StagingSettings(BaseSettings):
    ENVIRONMENT = 'staging'
    STAGING = True
    
class ProductionSettings(BaseSettings):
    ENVIRONMENT = 'production'
    PRODUCTION = True
    
settings = {'development': DevelopmentSettings(),
            'staging': StagingSettings(),
            'production': ProductionSettings()}