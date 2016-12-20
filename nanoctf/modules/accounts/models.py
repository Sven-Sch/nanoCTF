#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the database models (documents) for the core of **nanoCTF**.
"""
import flask_security
from nanoctf.core.db import DB


class Role(DB.Document, flask_security.RoleMixin):
    """
    The database model for user roles. It only contains a unique name and a description of the role. These roles are
    used by ``flask_security`` to allow/deny access to methods.
    """

    name = DB.StringField(max_length=80, unique=True)
    description = DB.StringField(max_length=255)


class User(DB.DynamicDocument, flask_security.UserMixin):  # pylint: disable=too-many-ancestors
    """
    The flexible user document to store the users data to the database. It's possible to set extra fields to this class,
    which will also be stored to the database.
    """

    username = DB.StringField(max_length=255, unique=True)
    email = DB.EmailField(max_length=255, unique=True)
    firstname = DB.StringField(max_length=255)
    lastname = DB.StringField(max_length=255)
    password = DB.StringField(max_length=255)
    active = DB.BooleanField(default=True)
    confirmed_at = DB.DateTimeField()
    last_login_at = DB.DateTimeField()
    current_login_at = DB.DateTimeField()
    last_login_ip = DB.StringField(max_length=15)
    current_login_ip = DB.StringField(max_length=15)
    login_count = DB.IntField(default=0)
    roles = DB.ListField(DB.ReferenceField(Role), default=[])
