#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains subclasses of ``MongoEngines`` classes like ``Document`` and ``DynamicDocument``. It also contains
the global database variable to provide a connection to the database.
"""
from flask_mongoengine import Document, DynamicDocument, BaseQuerySet, MongoEngine


class NanoctfQuerySet(BaseQuerySet):
    """
    A base queryset with handy extras
    """
    pass


class NanoctfDocument(Document):
    """
    Abstract document with extra helpers in the queryset class
    """

    meta = {'abstract': True, 'queryset_class': NanoctfQuerySet}


class NanoctfDynamicDocument(DynamicDocument):
    """
    Abstract Dynamic document with extra helpers in the queryset class
    """

    meta = {'abstract': True, 'queryset_class': NanoctfQuerySet}


DB = MongoEngine()
# db.ListField = ListField
DB.Document = NanoctfDocument
DB.DynamicDocument = NanoctfDynamicDocument
