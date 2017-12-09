# Date-parser
A small and basic date parser for different date formats, parses to datetime eligble format with the kind help of the dateutil library.

#### Installation
`pip3 install date-parser`

#### Usage

```
from date_parser.parser import DateParser
dp = DateParser()
```
Natural language
```
dp.parse_date('September 24th 1929')
>> datetime.datetime(1929, 9, 24, 0, 0)
```
Natural language - shortened month
```
dp.parse_date('Jan 14th 1999')
>> datetime.datetime(1999, 1, 14, 0, 0, 0)
```
Hyphens
```
dp.parse_date('01-01-2017')
>> datetime.datetime(2017, 1, 1, 0, 0)
```
Dots

```
dp.parse_date('19.11.1984')
>> datetime.datetime(1984, 11, 19, 0, 0, 0)
```
Forward slash
```
dp.parse_date('30/09/1542)
>> datetime.datetime(1542, 9, 30, 0, 0, 0)

```
Another natural language example
```
print(dp.parse_date('On 2012, I believe it was May 19th, Chelsea won the Champions League.'))
>> 2012-05-19 00:00:00

```

