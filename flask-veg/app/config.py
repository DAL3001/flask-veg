"""Flask configuration."""
TESTING = True
DEBUG = True
SECRET_KEY = 'key1'
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:xxxyyyzzz@flask-api.cqvuzfsssdnv.eu-west-2.rds.amazonaws.com:5432/flask"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'connect_timeout': 5
    }
}