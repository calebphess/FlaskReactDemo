# library imports
import os

from flask import Flask

# create and configure the app
# instance_relative_config states that the 
#     config files are relative to the instance folder
app = Flask(__name__)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from endpoint import *

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)