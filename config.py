class BaseConfig(object):
    CONFIG = "BaseConfig"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'askbrj32oi45ybakz0935ssjh3'


class ProdConfig(BaseConfig):
    CONFIG = "ProdConfig"
    pass


class StgConfig(BaseConfig):
    CONFIG = "StgConfig"
    DEVELOPMENT = True
    DEBUG=True


class DevConfig(BaseConfig):
    CONFIG = "DevConfig"
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(BaseConfig):
    NAME = 'TestConfig'
    TESTING = True
