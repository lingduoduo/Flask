# -*- coding: utf-8 -*-
#本地开发环境配置文件
from config.base_setting import *

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/mysql"
SECRET_KEY = "python123456"