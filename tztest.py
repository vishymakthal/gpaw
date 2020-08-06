import datetime
from dateutil.tz import tzlocal

t = datetime.datetime.now(tzlocal()).isoformat('T')  + 'Z'
print(t[:26]+'Z')
t1 = datetime.datetime.utcnow().isoformat('T')  + 'Z'
print(t1)