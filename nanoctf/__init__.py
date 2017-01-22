# -*- coding: utf-8 -*-
"""
The nanoctf module contains the core of *nanoctf* (app instance, views/routes).

:author: Sven Sch.
"""

from flask import Flask
from flask import render_template
from flask_security import Security, MongoEngineUserDatastore
from nanoctf.data import db
from nanoctf.core.dbmodel import User, Role
from nanoctf.core.forms import ExtendedRegisterForm

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')
app.config.from_object('nanoctf.config.DevConfig')

db.init_app(app)

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)


@app.route('/')
@app.route('/index')
def index():
    """
    Renders the HTML template for the *index* page, i.e. HTTP requests to `/` and `/index`.

    :return: The rendered `index.html` page from `templates` folder
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
