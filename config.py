

class Config:

    SECRET_KEY = 'Morara'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:123456789@localhost/pizza'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):

    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {'development': DevConfig, 'production': ProdConfig}
