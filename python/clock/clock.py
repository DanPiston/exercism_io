class Clock(object):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.fix()

    def __eq__(self, other):
        return (self.hours == other.hours and
                self.minutes == other.minutes)

    def __str__(self):
        return (self.format_hours() + ":" + 
                self.format_minutes())

    def add(self, additional_mins):
        self.minutes += additional_mins
        self.fix()
        return self

    def fix(self):
        self.fix_minutes()
        self.fix_hours()

    def fix_hours(self):
        self.hours == self.hours % 24

    def fix_minutes(self):
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60

    def format_hours(self):
        return str(self.hours).zfill(2)
    
    def format_minutes(self):
        return str(self.minutes).zfill(2)

