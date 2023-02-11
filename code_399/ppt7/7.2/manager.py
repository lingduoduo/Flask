# -*- coding: utf-8 -*-
from application import app
from www import *
if __name__ == "__main__":
    app.run( host = "0.0.0.0",  port=4999, debug=True )