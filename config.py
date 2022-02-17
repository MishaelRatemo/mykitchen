import os

class Config:
    RECIPE_API_BASE_URL ='https://api.spoonacular.com/food/search?&apiKey={}'
    RECIPE_COMPLEX_API_URL = 'https://api.spoonacular.com/recipes/complexSearch?query={}?&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    RECIPE_API_KEY = os.environ.get('RECIPE_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mykitchen'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOADED_PHOTOS_DEST ='app/static/uploads'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
    
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mykitchen'
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mykitchen'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}