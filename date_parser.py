# pylint: disable=import-error

import re
from datetime import datetime
import dateutil.parser
from .settings import CONSTANTS as CONSTS


class DateFromString:
    """
    Checks for different date formats in given string using regex for year and day,
    and a dictionary for months.
    Appends parsed data to list 'date'.
    If 2 dates are present within a string, will use the first one by order of appearence.
    """
    def __init__(self, date_string):
        self.date_string = date_string.replace('\n', ' ').replace('\r', '')
        self.date = []
        self.year = re.compile(r'\d{4}')  # Regex to match year digits
        self.day = re.compile(r'\b\d{1,2}\b')  # Regex to match day digits surrounded by whitespace
        self.months = CONSTS.months  # A dictionary of key(month number) and value (month 3 chars)
        self.separators = ('/', '-', '.')

    def _get_year(self):
        """
        Matches 4 digit strings and appends first one to self.date
        """
        year_from_string = re.findall(self.year, self.date_string)
        try:
            self.date.append(year_from_string[0])
        except IndexError:
            pass

    def _get_day(self):
        """
        Uses regex to find any 1 or 2 digit surrounded by whitespace.
        If an empty list is returned, changes regex to match 1 or 2 digits
        without whitespace lookahead. Appends to self.date.
        """
        day_from_string = re.findall(self.day, self.date_string)
        if not day_from_string:
            self.day = re.compile(r'\b\d{1,2}\D{2}')
        # If self.day matches None, change regex to match day digit with followed by 2 chars
        # e.g: (1st, 2nd, 14th, 29th)
            day_from_string = re.findall(self.day, self.date_string)
        try:
            if len(day_from_string[0]) == 1:
                # Add 0 before day digit if it's a single digit
                self.date.append('0'.join(day_from_string[0]))
        except IndexError:
            pass

        else:
            try:
                self.date.append(day_from_string[0])
            except IndexError:
                pass

    def _get_month(self):
        """
        Split passed param and iterate over it's elements, if element is in MONTHS.values()
        and the length of self.date list < 1, append it's corresponding key to self.date
        Appends to self.date.
        """
        for month in self.date_string.lower().split():
            for month_key, month_value in CONSTS.months.items():
                if month_value in month and not len(self.date) > 1:
                    self.date.append(month_key)


class DateParser(DateFromString):
    """
    Inherits from DateFromString, tries to parse date from passed string using
    dateutil module / super class' methods.
    """
    def _parse_by_separator(self):
        """
        Tries to parse each element of date_string split by separator
        using dateutil if separator occurrence > 2 in date_string.
        :return: Datetime object
        """
        # Using pattern list because I couldn't use string formatting with regex strings
        pattern_list = [CONSTS.forward_slash_regex, CONSTS.dot_regex, CONSTS.hyphen_regex]

        for pattern in pattern_list:
            compiled_pattern = re.compile(pattern)
            pattern_date = re.findall(compiled_pattern, self.date_string)
            try:
                timestamp = dateutil.parser.parse(pattern_date[0])
                if timestamp:
                    return timestamp
                else:
                    pass
            except (ValueError, IndexError):
                pass

    def parse_date(self):
        """
        Tries to parse passed param date_string using dateutil module.
        If fails and date_string contains more than one occurrence of elements from
        self.separators, calls _parse_by_separator function.
        Else, calls calls super class' methods _get_year, _get_month, _get_day.
        :return: datetime.date object of parsed date else None
        """
        try:
            timestamp = dateutil.parser.parse(self.date_string)
            return timestamp
        except ValueError:
            pass

        for separator in self.separators:
            if self.date_string.count(separator) > 1:
                try:
                    timestamp = DateParser._parse_by_separator(self)
                    if timestamp:
                        return timestamp
                    else:
                        continue
                except ValueError:
                    continue

        DateFromString._get_year(self)
        DateFromString._get_month(self)
        DateFromString._get_day(self)
        try:
            if self.date and len(self.date[2]) > 2:
                return dateutil.parser.parse(' '.join(self.date))
            else:
                return datetime(int(self.date[0]), int(self.date[1]), int(self.date[2]))
        except IndexError:
            print('No date found')
            return None
