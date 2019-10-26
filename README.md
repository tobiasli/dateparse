# dateparse
[![Stories in Ready](https://badge.waffle.io/tobiasli/dateparse.svg?label=ready&title=backlog)](http://waffle.io/tobiasli/dateparse)<br/>
[![Build Status](https://travis-ci.org/tobiasli/dateparse.svg?branch=master)](https://travis-ci.org/tobiasli/dateparse)<br/>
[![Coverage Status](https://coveralls.io/repos/tobiasli/dateparse/badge.svg?branch=master&service=github)](https://coveralls.io/github/tobiasli/dateparse?branch=master)

Dateparser for creating datetime objects from arbitrarily formated date strings. Primary support for Norwegian date formats.

New version is a complete refactor, with reduced complexity and functionality.

```python
import datetime
from dateparse import DateParser
parser = DateParser()
dt = parser.parse('5. januar 2015')
print(dt == [datetime.datetime(2015, 1, 5, 0, 0)])

dt = parser.parse('1/12/2014 kl 12, 11.12.2015 kl 14')
print(dt == [datetime.datetime(2014, 12, 1, 12, 00), datetime.datetime(2015, 12, 11, 14, 00)])
```
