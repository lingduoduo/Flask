# -*- coding: utf-8 -*-
from application import app, manager
from flask_script import Server, Command
from jobs.launcher import runJob
from www import *

##web server
manager.add_command("runserver", Server(host="0.0.0.0", port=4999, use_debugger=True, use_reloader=True))

manager.add_command( "runjob", runJob )

##create_table
@Command
def create_all():
    from application import db
    from common.models.user import User
    db.create_all()
manager.add_command("create_all", create_all)
def main():
    manager.run()


if __name__ == "__main__":
    # app.run( host = "0.0.0.0",debug=True )
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
