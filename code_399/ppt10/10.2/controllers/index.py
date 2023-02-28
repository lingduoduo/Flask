# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.models.user import User
from application import app
from common.libs.Helper import ops_render
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

    #app.logger.info( session['uid'] )

    return ops_render( "index.html",context )
