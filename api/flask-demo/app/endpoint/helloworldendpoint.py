from __main__ import app


# a simple page that says hello
# @app.route defines the url off of the BASE url e.g. www.appname.com/api + @app.route
# in dev this will be literally http://localhost:5000/hello
@app.route('/hello')
def hello():
    return 'Hello, World!'