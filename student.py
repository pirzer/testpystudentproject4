from datetime import date, timedelta


class Student:
    """ A Student class as a basis for method testing """
    def __init__(self, first_name, last_name):
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{first_name} {self._last_name}"
