class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = "adsdfdgergadfgf"


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True


# 测试环境
class TestingConfig(Config):
    TESTING = True
