# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.models.user import User
index_page = Blueprint( "index_page",__name__ )

@index_page.route("/")
def index():
    ##传值
    name = "python"
    ##
    context = {"name": name}
    context['user'] = {"nickname": "Ling",
                       "email": "linghypshen@gmail.com",
                       "linkedin": "https://www.linkedin.com/in/ling-huang-87249924/"}

    result = User.query.all()
    context['result'] = result

    return render_template( "index.html",**context )
