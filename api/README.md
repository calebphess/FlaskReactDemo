# Flask API #

## Description ##
A demo API built with flask using python.
It requires python 3 version 3.8.2 or later which can be installed from [Here](https://www.python.org/downloads/ "Install url for python 3"). I recommend installing and using *pyenv* for venv things but it's up to you. The ***Getting Started*** section assumes your python3 is set to 3.8.2 you can take whatever liberties in setting up the virtual environment that you feel are adequate.

## Getting Started ##
Move into the ***flask-demo*** folder and run the following commands
```
# set up the virtual environment
python3 -m venv venv`

# activate the new environment
source venv/bin/activate

# install requirements via the requirements.txt file
pip install -r requirements.txt

# set up the environment variables to run the dev flask server
# this should point to *GIT_PROJECT_TOP_DIRECTORY/api/flask-demo-app*
export FLASK_APP=export FLASK_APP=~/Development/git/FlaskReactDemo/api/flask-demo/app
export FLASK_ENV=development

# run the application
flask run
```

## Flask Notes ##
- When installed, flask acts as it's own binary
    - It uses some environment variables to tell it how to run
        - FLASK_APP is what directory the flask server is located in
        - FLASK_ENV allows you to specify whether it should be run in *development* mode or not
- the main start point of the app is ***app/__init__.py***