class Config(object):
    @staticmethod
    def init_app(app):
        pass


class ProConfig(Config):
    pass




class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/test1"
    SECRET_KEY = 'hard to guess'




