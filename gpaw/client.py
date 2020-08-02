# -*- coding: utf-8 -*-

"""
gpaw.client

This module contains the Client class that is responsible for authorizing user credentials and instantiating service clients.
"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

from .services.sheets import GoogleSheets
from .services.tasks import GoogleTasks
from .services.calendar import GoogleCalendar

# Service Keys
sheets_key = 'sheets'
tasks_key = 'tasks'
cal_key = 'cal'


class Client(object):
    """The client that communicates with the Google APIs.

    :param creds (str): The path to the credentials.json file.
    :param scopes (list): List of string specifying the scope of services the token is authorized for.

    """

    def __init__(self, creds, scopes, token='token.pickle'):
        self._auth = None
        self._svc = {}
        self._creds = creds
        self._scopes = scopes
        self._token = token

    def _authorize(self):
        """
        Authorizes the client using the user's provided credentials file and scopes.
        """
        if os.path.exists(self._token):
            with open(self._token, 'rb') as token:
                self._auth = pickle.load(token)
        
        if not self._auth or not self._auth.valid:
            if self._auth and self._auth.expired and self._auth.refresh_token:
                self._auth.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self._creds, self._scopes)
                self._auth = flow.run_local_server()
            with open(self._token, 'wb') as token:
                pickle.dump(self._auth, token)

    
    def sheets(self):
        """Returns a Google Sheets instance. Creates a new one if not present already.
        
        :returns: a :class:`~gpaw.services.Sheets` instance.
        """
        if self._svc.get(sheets_key, None):
            return self._svc[sheets_key]

        self._svc[sheets_key] = GoogleSheets(self._auth)
        return self._svc[sheets_key] 

    def tasks(self):
        """Returns a Google Tasks instance. Creates a new one if not present already.
        
        :returns: a :class:`~gpaw.services.Tasks` instance.
        """
        if self._svc.get(tasks_key, None):
            return self._svc[tasks_key]

        self._svc[tasks_key] = GoogleTasks(self._auth)
        return self._svc[tasks_key] 

    def calendar(self):
        """Returns a Google Calendar instance. Creates a new one if not present already.
        
        :returns: a :class:`~gpaw.services.Calendar` instance.
        """
        if self._svc.get(cal_key, None):
            return self._svc[cal_key]

        self._svc[cal_key] = GoogleCalendar(self._auth)
        return self._svc[cal_key] 

