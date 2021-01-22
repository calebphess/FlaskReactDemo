# library imports
import os

from flask import Flask


def create_app():
    # create and configure the app
    # instance_relative_config states that the 
    #     config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # @app.route defines the url off of the BASE url e.g. www.appname.com/api + @app.route
    # in dev this will be literally http://localhost:5000/hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app