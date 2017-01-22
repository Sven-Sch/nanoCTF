# -*- coding: utf-8 -*-


class DefaultConfig(object):
    """
    The default configuration of nanoCTF. It's not recommended to use this configuration by it's own.
    Either use a configuration class which extends this class or write your own configuration file.
    """
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5000
    SECRET_KEY = 'very-secure-key'
    MONGODB_DB = 'nanoctf'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    SECURITY_CONFIRMABLE = False
    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True

class ProductionConfig(DefaultConfig):
    """
    This configuration is used for productive usage.
    """
    pass


class TestConfig(DefaultConfig):
    """
    This configuration is only used by the unit tests.
    """
    TESTING = True
    MONGODB_DB = 'nanoctfTest'
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False

class DevConfig(DefaultConfig):
    """
    This configuration is only used during development.
    """
    DEBUG = True
    SECURITY_SEND_REGISTER_EMAIL = False
