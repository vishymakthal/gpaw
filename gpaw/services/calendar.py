from googleapiclient.discovery import build

from gpaw.services.gsuite import GoogleSuite

class GoogleCalendar(GoogleSuite):
    """The service object responsible for providing an interface with Google Calendar.

    :param auth: An OAuth credential object generated by the oauth2client library, gets passed to the super's constructor.

    """
    def __init__(self, auth):
        GoogleSuite.__init__(self, auth)
        self._c = build('calendar', 'v3', credentials=self.auth).events()

    def create(self, event_desc):
        """Creates an event based on the description.
        
        :param event_desc (str): Description of event to add. e.g. "Lakers vs Raptors at 8:30pm on 8/1" 
        :param columns (bool): flag to specify that columns are being written.

        :returns List[List]: 2D array representing cells read.
        """
        
        self._c.quickAdd(
            calendarId='primary',
            text=event_desc).execute()