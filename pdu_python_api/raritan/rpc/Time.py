

import time, calendar
from datetime import datetime

#
# Decodes UNIX timestamp (UTC secs since epoch) to python datetime and vice versa.
#
class Time(datetime):
    def __new__(cls, *x):
        return datetime.__new__(cls, *x)

    @staticmethod
    def decode(json):
        assert isinstance(json, int)
        return Time.utcfromtimestamp(json)

    def encode(self):
        timestamp = calendar.timegm(self.utctimetuple()) 
        return timestamp

    def __str__(self):
        return self.isoformat(' ') + " (UTC)"
