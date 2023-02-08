# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, I Love Python"


@app.route("/my")
def my():
    return "my page"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4999, debug=True)
