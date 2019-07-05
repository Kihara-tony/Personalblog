class Config:
    '''
    General configuration parent class
    '''
    pass
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
    Config: THe parent configuration class with general configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
    Config: THe parent configuration class with General configuration settings
    '''
    pass
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    