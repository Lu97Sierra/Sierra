class BaseConfig:
    USER_DB = 'postgres'
    PASS_DB = '867163789'
    URL_DB = 'localhost'
    NAME_DB ='finalproject'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SECRET_KEY = "secretKEY1232"
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False