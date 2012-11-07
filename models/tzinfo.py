from datetime import time, tzinfo, timedelta

class GMT2(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=2)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self,dt):
        return "Europe/Istanbul"
