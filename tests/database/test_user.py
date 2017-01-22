# -*- coding: utf-8 -*-

from tests import BaseTestCase
from nanoctf.core.dbmodel import User


class BasicDbTestCase(BaseTestCase):
    """
    This class provides unit tests for the `User` collection, e.g. create, update, delete, ... a user.
    """

    def test_create_user(self):
        # Create user
        test_user = User(
            name='Testuser',
            email='test@test.com',
            password='very_secret_password'
        )
        test_user.save()
        # read user from db
        db_user = User(name='Testuser')
        self.assertIsNotNone(db_user, 'Could not find the test user within the User collection.')
        self.assertTrue(db_user.active, 'The active flag is not set.')
