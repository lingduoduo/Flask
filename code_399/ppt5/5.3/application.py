# -*- coding: utf-8 -*-
from flask import Flask
from indexController import index_page
from postController import post_page

app = Flask( __name__ )

app.register_blueprint( index_page,url_prefix = "/python" )
app.register_blueprint( post_page,url_prefix = "/post" )

if __name__ == "__main__":
    app.run( host = "0.0.0.0", port=4999, debug=True )