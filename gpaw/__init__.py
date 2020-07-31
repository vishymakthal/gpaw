# -*- coding: utf-8 -*-

"""
gpaw

Google Suite Python API Wrapper
"""

from .client import Client

def NewClient(credentials, scopes):
    """Login to Google API using OAuth2 credentials.

    :returns: :class:`gpaw.Client` instance.
    """
    client = Client(creds=credentials,scopes=scopes)
    client._authorize()
    return client