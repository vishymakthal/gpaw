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

from .services import GoogleSheets
from .services import GoogleTasks
from .services import GoogleCalendar

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
        self.auth = None
        self.svc = {}
        self.creds = creds
        self.scopes = scopes
        self.token = token

    def _authorize(self):
        """
        Authorizes the client using the user's provided credentials file and scopes.
        """
        if os.path.exists(self.token):
            with open(self.token, 'rb') as token:
                self.auth = pickle.load(token)
        
        if not self.auth or not self.auth.valid:
            if self.auth and self.auth.expired and self.auth.refresh_token:
                self.auth.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.creds, self.scopes)
                self.auth = flow.run_local_server()
            with open(self.token, 'wb') as token:
                pickle.dump(self.auth, token)

    
    def Sheets(self):
        """Returns a Google Sheets instance. Creates a new one if not present already.
        
        :returns: a :class:`~gpaw.services.Sheets` instance.
        """
        if self.svc.get(sheets_key, None):
            return self.svc[sheets_key]

        return GoogleSheets(self.auth)

    def Tasks(self):
        """Returns a Google Tasks instance. Creates a new one if not present already.
        
        :returns: a :class:`~gpaw.services.Tasks` instance.
        """
        if self.svc.get(tasks_key, None):
            return self.svc[tasks_key]

        return GoogleTasks(self.auth)

    def Calendar(self):
        """Returns a Google Calendar instance. Creates a new one if not present already.
        
        :returns: a :class:`~gpaw.services.Calendar` instance.
        """
        if self.svc.get(cal_key, None):
            return self.svc[cal_key]

        return GoogleCalendar(self.auth)

