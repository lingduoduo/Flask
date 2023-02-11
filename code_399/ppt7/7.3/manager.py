# -*- coding: utf-8 -*-
from application import app,db
from www import *

if __name__ == "__main__":
    from common.models.user import User
    app.app_context().push()
    db.create_all()
    # app.run( host = "0.0.0.0", port=4999, debug=True )

