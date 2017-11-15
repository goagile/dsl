from datetime import date, time


class Calendar(object):

    def __init__(self):
        self.events = []

    def add(self, name):
        event = Event(name)
        self.events.append(event)
        return event


class Event:
    def __init__(self, name, date_=None, start=None, end=None, place=None):
        self._name = name
        self._date = date_
        self._start = start
        self._end = end
        self._place = place

    def __eq__(self, other):
        objs, fields = [(self, other)], ('_date', '_start', '_end', '_place')
        return all(
            all(getattr(s, name) == getattr(o, name) for s, o in objs)
            for name in fields
        )

    def on(self, year, month, day):
        self._date = date(year, month, day)
        return self

    def start(self, time_str):
        self._start = self._parse_time(time_str)
        return self

    def end(self, time_str):
        self._end = self._parse_time(time_str)
        return self

    def at(self, place):
        self._place = place
        return self

    def _parse_time(self, time_str):
        hours, minutes = time_str.split(':')
        result = time(int(hours), int(minutes))
        return result
