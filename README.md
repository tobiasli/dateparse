# dateparse
[![Stories in Ready](https://badge.waffle.io/tobiasli/dateparse.svg?label=ready&title=backlog)](http://waffle.io/tobiasli/dateparse)<br/>
[![Build Status](https://travis-ci.org/tobiasli/dateparse.svg?branch=master)](https://travis-ci.org/tobiasli/dateparse)<br/>
[![Coverage Status](https://coveralls.io/repos/tobiasli/dateparse/badge.svg?branch=master&service=github)](https://coveralls.io/github/tobiasli/dateparse?branch=master)

Dateparser handling Norwegian dates.

```python
import dateparse
dateparse.parse('5. januar 2015')
>>> datetime.datetime(2015, 1, 5, 0, 0)

dateparse.parse('monday 16:25')
>>> datetime.datetime(2015, 11, 16, 16, 25)   # The first monday after today.

dateparse.parse(1/12/2014 kl 12)
>>> datetime.datetime(2014, 12, 11, 12, 00)
```

<b>Notice:</b> The module is written for flexibility, not speed. Parsing single dates works fine, parsing hundreds will seem pretty slow.
