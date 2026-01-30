import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True

