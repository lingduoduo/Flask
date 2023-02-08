# -*- coding: utf-8 -*-
from flask import Flask, Blueprint

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello ,I Love python"

index_page = Blueprint("index_page", __name__)
@index_page.route("/")
def index_page_index():
    return "index page for http://127.0.0.1:4999/python/"

app.register_blueprint(index_page, url_prefix="/python")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4999, debug=True)
