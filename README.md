# Date-parser
A small and basic date parser for different date formats, parses to datetime eligble format with the kind help of the dateutil library.

# Description
Originally developed for my RSS project, I needed a date parser because each blog / site had different date formats, so I wrote this in order to be able to sort by date, and for continuity's sake.

# Examples
These examples contain the string scraped from a date tag in an arbitrarty URL and the date returned after the call to DateParser(date).parse_date() function with that string.


Date tag:  "09 October 2016"
Parsed date:  2016-10-09 00:00:00

Date tag: "Mar 29, 2017 · 3 minute read"
Parsed date:  2017-03-29 00:00:00

Date tag: "Jan 1, 2017 · 2 minute read"
Parsed date: "2017-01-01 00:00:00

Date tag: Posted by `Author` on
May 14, 2017."
Parsed date:  2017-05-14 00:00:00

If 2 dates are present within a string, uses the first one by order of appearence:

Date tag: "Post updated by `Author` on 
March 01, 2017. Originally posted 
on February 27, 2017."
Parsed date:  2017-03-01 00:00:00

Date tag: "different day format 17th july 2017"
Parsed Date: 2017-07-17 00:00:00

Date tag: "This is a 27/05/1920 date string"
Parsed Date: 1920-05-27 00:00:00

Date tag: "This is another string containing a date09.12.1990with no white space"
Parsed Date: 1990-09-12 00:00:00

# Note
DateParser utilizes dateutil library. If passed a date string the like the last example above, DateParser isolates the date only part and tries to let dateutil parse it. 
dateutil defaults to DD/MM/YYYY or YYYY/MM/DD so the middle digits will always be considered month, UNLESS middle digits > 12, which they will then be considered as days.
