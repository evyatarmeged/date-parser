# Date-parser
Parse different date strings into datetime objects.

#### Installation
`pip3 install date-parser`

#### Usage

```
from date_parser.parser import DateParser
dp = DateParser()
```

```
dp.parse_date('September 24th 1929')
datetime.datetime(1929, 9, 24, 0, 0)
```

```
dp.parse_date('01-01-2017')
datetime.datetime(2017, 1, 1, 0, 0)
```
```
print(dp.parse_date('Jan 14th 1999'))
1999-01-14 00:00:00
```
```
print(dp.parse_date('NoWhiteSpaceDate19.11.1984'))
1984-11-19 00:00:00
```

