# -*- coding: utf-8 -*-

from tests import BaseTestCase


class BasicDbTestCase(BaseTestCase):
    """
    This class provides basic unit tests for the database, e.g. is the database available.
    """

    def test_is_database_initialized(self):
        """
        Checks whether the important database config values are set and whether the database object is not `None`.
        """
        self.assertIsNotNone(self.db, 'The database object is None.')
        self.assertIsNotNone(self.app.config['MONGODB_DB'], 'Found no config entry for MONGODB_DB.')
        self.assertIsNotNone(self.app.config['MONGODB_HOST'], 'Found no config entry for MONGODB_HOST.')
        self.assertIsNotNone(self.app.config['MONGODB_PORT'], 'Found no config entry for MONGODB_PORT.')

    def test_is_testdatabase_used(self):
        """
        Checks whether the config value of the database name ends with `Test`. This ensures that not the production
        database is filled with test datasets.
        """
        self.assertIsNotNone(self.app.config, 'The config object of the app is None.')
        self.assertTrue(self.app.config['MONGODB_DB'].endswith('Test'),
                        'The name of the test database does not end with "Test"')
