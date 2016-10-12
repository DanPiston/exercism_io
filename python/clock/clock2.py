class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.total()

    def add(self, minutes):
        self.minute += minutes
        return self.total()

    def __eq__(self, otherclock):
        return str(self) == str(otherclock)

    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    def total(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self
