# -*- coding: utf-8 -*-
#本地开发环境配置文件
from config.base_setting import *
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/movie_cat"
SECRET_KEY = "python123456"
DOMAIN = {
    "www":"http://192.168.0.124"
}


#RELEASE_PATH = "/home/www/release_version"
