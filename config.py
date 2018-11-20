import os
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:ewerton@localhost/catequese_conectada'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///catequese_conectada.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SEND_FILE_MAX_AGE_DEFAULT = 0
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

SECRET_KEY = 'qbbkqetk'
