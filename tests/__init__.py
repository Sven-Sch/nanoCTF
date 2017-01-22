# -*- coding: utf-8 -*-
"""
This class is "copied" from https://realpython.com/blog/python/python-web-applications-with-flask-part-iii/
and just a bit modified.

:author: Author of the Blog post (RealPython)
         Sven Sch.
"""
from flask_testing import TestCase
from flask_security import MongoEngineUserDatastore, Security
from nanoctf import app
from nanoctf.data import db
from nanoctf.core.dbmodel import Role, User


class BaseTestCase(TestCase):
    """
    A base test case for almost all nanoCTF tests.
    """

    def create_app(self):
        """
        Creates the nanoCTF app and loads the test configuration.

        :return: the nanoCTF app with loaded test configuration
        """
        app.config.from_object('nanoctf.config.TestConfig')
        return app

    def setUp(self):
        """
        Invorked before each test. It's used to create a database connection
        """
        # TODO refactor this
        self.db = db
        # make sure to load mongoengine extension only once
        if 'mongoengine' not in self.app.extensions:
            self.db.init_app(self.app)
        # make sure to load flask security
        if 'security' not in self.app.extensions:
            self.user_datastore = MongoEngineUserDatastore(self.db, User, Role)
            self.security = Security(self.app, self.user_datastore)

    def tearDown(self):
        """
        Invoked after each test. It's used to cleanup.
        """
        # Drop the complete database after each test
        self.db.connection.drop_database(app.config['MONGODB_DB'])
