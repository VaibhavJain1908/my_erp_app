import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///erp.db'  # Change this for production
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "e680e30435279fe9ef0662238c7e0654"
