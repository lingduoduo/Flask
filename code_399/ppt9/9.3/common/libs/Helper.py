# -*- coding: utf-8 -*-
from flask import jsonify
def ops_renderJSON( code = 200,msg = "Success~~",data = {} ):
    resp = { "code":code,"msg":msg,"data":data }
    return jsonify( resp )

def ops_renderErrJSON( msg = "Please try again~~",data = {} ):
    return ops_renderJSON( code = -1,msg = msg,data = data )