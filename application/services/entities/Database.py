from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_TABLE_ARGS = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}