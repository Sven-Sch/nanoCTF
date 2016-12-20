#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
General Flask settings
"""
DEBUG = True

# Themes
# THEME_PATHS = '/themes'
DEFAULT_THEME = 'nanoctf'

"""
Database configuration
"""
MONGODB_DB = "nanoctf"
MONGODB_HOST = 'nanoctf'
MONGODB_PORT = 27017
MONGODB_USERNAME = None
MONGODB_PASSWORD = None

"""
Extensions needed by the core of nanoCTF.
if you plan to add new extensions use EXTRA_EXTENSIONS

DO NOT CHANGE THIS LIST
"""
CORE_EXTENSIONS = [
    'nanoctf.core.admin.configure_admin',
    'nanoctf.ext.security.configure',
    'nanoctf.ext.themes.configure',
    'nanoctf.ext.views.configure'
]

"""
Security configuration (flask_security)

Detailed information: https://pythonhosted.org/Flask-Security/configuration.html
"""
# Password encryption (see: passlib)
# Possible values: pbkdf2_sha512 | bcrypt | sha512_crypt
SECURITY_PASSWORD_HASH = 'bcrypt'
# Create endpoint for email confirmation
SECURITY_CONFIRMABLE = True
# Create endpoint for password resets ("forgot password")
SECURITY_RECOVERABLE = True
# Create endpoint for user registration
SECURITY_REGISTERABLE = True
# Create endpoint to allow users to change their password
SECURITY_CHANGEABLE = True
# Should (Last-)Login IP and time of users be stored
SECURITY_TRACKABLE = True
# Salt for HMAC (used if password hash is not "plaintext")
SECURITY_PASSWORD_SALT = 'V3RyS3cr3t'

SECURITY_SEND_REGISTER_EMAIL = False

"""
Flask's secret to sign session cookies.

This should really be secret for security, use os.urandom or uuid4 to generate
in your shell:

$ python -c "import uuid; print(str(uuid.uuid4()).replace('-', ''))"
or
$ python -c "import os, binascii; print(binascii.hexlify(os.urandom(30)))"
"""
SECRET_KEY = "S3cr3Tk3Y"
