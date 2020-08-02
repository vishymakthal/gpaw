# -*- coding: utf-8 -*-

from googleapiclient.discovery import build

"""
gpaw.services

This module contains the service classes that are responsible for executing functionalities of GSuite services.
"""

# from .exceptions import NotAuthorized


class GoogleSuite(object):
    """Base class for all other Google Suite service classes.

    :param: auth: An OAuth credential object generated by the oauth2client library.

    """
    def __init__(self, auth):
        self.auth = auth

