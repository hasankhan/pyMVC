import logging
import logging.config

def setup_logging(app):
    logger_name = app.config['ENVIRONMENT']
    if logger_name not in app.config['LOGGING_CONFIG']['loggers']:
        raise RuntimeError('Logger {} is not configured'.format(logger_name))
    app.logger.handlers[:] = []
    logging.config.dictConfig(app.config['LOGGING_CONFIG'])