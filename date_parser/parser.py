# pylint: disable=import-error

import re
import dateutil.parser
from datetime import datetime
from date_parser.settings import Constants


class DateFromString:
    """
    Checks for different date formats in given string using regex for year and day,
    and a dictionary for months.
    Appends parsed data to list 'date'.
    If 2 dates are present within a string, will use the first one by order of appearence.
    """
    _CONSTANTS = Constants()

    def __init__(self):
        self._date = []
        self._year = re.compile(r'\d{4}')  # Regex to match year digits
        self._day = re.compile(r'\b\d{1,2}\b')  # Regex to match day digits surrounded by whitespace
        self._months = self._CONSTANTS.months  # A dictionary of key(month number) and value (month 3 chars)
        self._separators = ('/', '-', '.')

    def _get_year(self, date_string):
        """
        Matches 4 digit strings and appends first one to self.date
        """
        year_from_string = re.findall(self._year, date_string)
        try:
            self._date.append(year_from_string[0])
        except IndexError:
            pass

    def _get_day(self, date_string):
        """
        Uses regex to find any 1 or 2 digit surrounded by whitespace.
        If an empty list is returned, changes regex to match 1 or 2 digits
        without whitespace lookahead. Appends to self.date.
        """
        day_from_string = re.findall(self._day, date_string)
        if not day_from_string:
            self._day = re.compile(r'\b\d{1,2}\D{2}')
        # If self.day matches None, change regex to match day digit with followed by 2 chars
        # e.g: (1st, 2nd, 14th, 29th)
            day_from_string = re.findall(self._day, date_string)
        try:
            if len(day_from_string[0]) == 1:
                # Add 0 before day digit if it's a single digit
                self._date.append('0'.join(day_from_string[0]))
            else:
                self._date.append(day_from_string[0])

        except IndexError:
            pass

    def _get_month(self, date_string):
        """
        Split passed param and iterate over it's elements, if element is in MONTHS.values()
        and the length of self.date list < 1, append it's corresponding key to self.date
        Appends to self.date.
        """
        for month in date_string.lower().split():
            for month_key, month_value in self._CONSTANTS.months.items():
                if month_value in month and not len(self._date) > 1:
                    self._date.append(month_key)


class DateParser(DateFromString):
    def __init__(self):
        super().__init__()
        self._pattern_list = [
            self._CONSTANTS.forward_slash_regex, self._CONSTANTS.dot_regex, self._CONSTANTS.hyphen_regex]
    """
    Inherits from DateFromString, tries to parse date from passed string using
    dateutil module / super class' methods.
    """

    def _parse_by_separator(self, date_string):
        """
        Tries to parse each element of date_string split by separator
        using dateutil if separator occurrence > 2 in date_string.
        :return: Datetime object
        """
        for pattern in self._pattern_list:
            compiled_pattern = re.compile(pattern)
            pattern_date = re.findall(compiled_pattern, date_string)
            try:
                timestamp = dateutil.parser.parse(pattern_date[0])
                if timestamp:
                    return timestamp
            except (ValueError, IndexError):
                pass

    def parse_date(self, date_string):
        """
        Tries to parse passed param date_string using dateutil module.
        If fails and date_string contains more than one occurrence of elements from
        self.separators, calls _parse_by_separator function.
        Else, calls calls super class' methods _get_year, _get_month, _get_day.
        :return: datetime.date object of parsed date else None
        """
        date_string = date_string.replace('\n', ' ').replace('\r', '')
        try:
            date = dateutil.parser.parse(date_string)
            return date
        except ValueError:
            pass

        for separator in self._separators:
            if date_string.count(separator) > 1:
                try:
                    date = self._parse_by_separator(date_string)
                    if date:
                        return date
                except ValueError:
                    continue

        self._get_year(date_string)
        self._get_month(date_string)
        self._get_day(date_string)
        try:
            if self._date and len(self._date[2]) > 2:
                parsed_date = dateutil.parser.parse(' '.join(self._date))
            else:
                parsed_date = datetime(int(self._date[0]), int(self._date[1]), int(self._date[2]))
        except IndexError:
            self._date = []
            return 'Could not parse date from {}'.format(date_string)
        self._date = []
        return parsed_date
