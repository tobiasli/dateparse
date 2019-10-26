# -------------------------------------------------------------------------------
# Name:        GroceryShopping_Test_Suite
# Purpose:      Test the components of the groceries class.
#
# Author:      Tobias
#
# Created:     01.05.2015
# Copyright:   (c) Tobias 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import pytest
import datetime
from dateparse import dateparse

TEST_CASES = [
    ('14.05.2012 kl 13:06:26.23', datetime.datetime(2012, 5, 14, 13, 6, 26, 230000)),
    ('14.05.2012 kl 1306', datetime.datetime(2012, 5, 14, 13, 6, 0)),
    ('14.05.2012 kl 13:06', datetime.datetime(2012, 5, 14, 13, 6, 0)),
    ('14.05.2012 kl 13:06:26', datetime.datetime(2012, 5, 14, 13, 6, 26)),
    ('14. mai 2012', datetime.datetime(2012, 5, 14, 0, 0, 0)),
    ('mai 2012', datetime.datetime(2012, 5, 1, 0, 0, 0)),

]


def test_pattern_builder_simple():
    seq = ['year', 'month']
    pat = dateparse.pattern_builder(seq)
    assert pat == '(:?(?<=\\W)|^)(?P<year>\\d{4}|\\d{2})[\\.\\-\\W\\\\/](?P<month>\\d{1,2}|\\w{3,9})(:?(?=\\W)|$)'


def test_verify_and_get_datevec():
    assert dateparse.DateParser.verify_and_get_datevec(
        {'year': '1988', 'month': 'nov', 'day': '22', 'hour': '14', 'minute': '50', 'second': '12.1234576'})
    assert not dateparse.DateParser.verify_and_get_datevec(
        {'year': '1988', 'month': 'gnome', 'day': '22', 'hour': '14', 'minute': '50', 'second': '12.1234576'})
    assert not dateparse.DateParser.verify_and_get_datevec(
        {'year': '1988', 'month': 'nov', 'day': '33', 'hour': '14', 'minute': '50', 'second': '12.1234576'})
    assert not dateparse.DateParser.verify_and_get_datevec(
        {'year': '1988', 'month': 'nov', 'day': '22', 'hour': '26', 'minute': '50', 'second': '12.1234576'})
    assert not dateparse.DateParser.verify_and_get_datevec(
        {'year': '1988', 'month': 'nov', 'day': '22', 'hour': '14', 'minute': '70', 'second': '12.1234576'})


@pytest.mark.parametrize(('candidate', 'expected'), TEST_CASES)
def test_parse(candidate, expected):
    parser = dateparse.DateParser()
    assert parser.parse(candidate)[0] == expected