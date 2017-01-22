Configuration
=============

.. todo:: write introduction

There are several Configuration classes for different stages. All these configuration classes are in
:file: nanoctf.config.__init__.py:

DefaultConfig
    This is the default configuration. Other configuration classes should extend this class and add or overwrite
    configuration values.

ProductionConfig
    This configuration is used for the production stage.

DevConfig
    Only used by developers.

TestConfig
    Only used to run the tests.


Writing your own configuration
------------------------------

.. code-block:: python

   class MyConfiguration(DefaultConfig):
      FOO = 'BAR'
