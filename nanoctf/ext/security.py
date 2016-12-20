#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This core extension is customization of ``flask_security``, which provides
methods and classes for:

* Session based authentication
* Role management
* Password encryption
* Basic HTTP authentication
* Token based authentication
* Token based account activation (optional)
* Token based password recovery / resetting (optional)
* User registration (optional)
* Login tracking (optional)
* JSON/Ajax Support

The users and roles are stored in a MongoDB database and the models for the
database are in the extension ``accounts``.
"""
import flask_security
import wtforms
import nanoctf.modules.accounts.models as account_models
from nanoctf.core.templates import render_template


class Security(flask_security.Security):
    """
    This class extends ``flask_security.Security`` to render web frontend themes provided by **nanoCTF**. It simply
    overrides the ``render_template`` method to invoke the render method of **nanoCTF**.
    """
    def render_template(self, *args, **kwargs):
        return render_template(*args, **kwargs)


class ExtendedRegisterForm(flask_security.forms.RegisterForm):  # pylint: disable=too-many-ancestors
    """
    This class extends ``flask_security.RegisterForm`` with some additional fields. These additional fields (username,
    firstname and lastname) are required, i.e. the user has to enter a value for these fields.
    """
    username = wtforms.StringField('Username',
                                   validators=[flask_security.forms.Required('You have to enter a username!')])
    firstname = wtforms.StringField('Firstname',
                                    validators=[flask_security.forms.Required('You have to enter your firstname!')])
    lastname = wtforms.StringField('Lastname',
                                   validators=[flask_security.forms.Required('You have to enter your lastname!')])


def configure(app, db):
    """

    Args:
        app:
        db:
    Returns:

    """
    register_form = ExtendedRegisterForm
    confirm_register_form = ExtendedRegisterForm
    app.security = Security(
        app=app,
        datastore=flask_security.MongoEngineUserDatastore(db, account_models.User, account_models.Role),
        register_form=register_form,
        confirm_register_form=confirm_register_form
    )
