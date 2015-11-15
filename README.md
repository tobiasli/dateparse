# dateparse
[![Stories in Ready](https://badge.waffle.io/tobiasli/dateparse.svg?label=ready&title=backlog)](http://waffle.io/tobiasli/dateparse)<br/>
[![Build Status](https://travis-ci.org/tobiasli/dateparse.svg?branch=master)](https://travis-ci.org/tobiasli/dateparse)

Dateparser handling Norwegian dates.

```python
import dateparse
dateparse.parse('første januar 2015')
>>> datetime.datetime(2015, 1, 1, 0, 0)
```
