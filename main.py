# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
Method dateParse.parse(string) returns a datetime-object for any reference to a
time that lies within string. String can detect complex dates in any string.
Examples:
    string = 'en gang på 1600-tallet'       => 1600-01-01 00:00:00
    string = 'midten av det 14. århundre'   => 1350-01-01 00:00:00
    string = 'den 14. mai 1927, kl 19:22'   => 1927-05-14 19:22:00
    string = '14.05.2012 kl 1306'           => 2012-05-14 13:06:00
    string = 'fjerde kvartal 2002'          => 2002-10-01 00:00:00


The method assumes that 2-digit years are in current century if the two digits
are lower than the current 2-digit year, while higher numbers are assumed to
be in the previous century. Examples:
    Current year = 2014
    string = 'midten av 12'                 => 2012-06-01 00:00:00
    string = '17. desember 22'              => 1922-12-17 00:00:00

(the method uses current year, and is not hardcoded to 2014)

Added functionality to parse weekdays as input. Method will interpret weekdays
and find the first upcoming dates (including today) that match the weekday name.

Written by:
    Tobias Litherland
    tobiaslland@gmail.com

History:
    07.04.2015  TL  Objectified script. Streamline logic within parser.
                    Reduced parsing time to 1/280 on simpe dates. Added history.
    01.05.2014  TL  Started groundwork.

Future improvements:
    - Token lookback to make sure the number seperators for time is consistent.
    - Fix handling of relative centuries.
    - PEP8 conformity
    - Speed

'''

import re
from collections import OrderedDict
import datetime
import time as timer

import definition

class dateParse(object):

    def replace_dict(string,dictionary):
        dictionary = {"condition1": "", "condition2": "text"} # define desired replacements here

        # use these three lines to do the replacement
        pattern = re.compile("|".join(dictionary.keys()))
        string = pattern.sub(lambda m: str(dictionary[re.escape(m.group(0))]), string)

        return string


    def parse2(self,input_string, reference_date = None, debugging = False):


    def parse(self,stringIn,debugMode = False,referenceDate = None):
        '''
        (stringIn = string, debugMode = boolean/False)
        Takes any string and checks if it can find any valid dates within. Variable
        "combinations" controlls the variants that are looked for, and in what order
        they are prioritized.

        All dates and months are checked for accepted values and string is
        rechecked if values are outside acceptable bounds.

        All identifiable formats are listed below, and lists may be appended at
        will. All text identifications are regular expressions.

        '''

        string = stringIn
        match = False

        if not string:
            return []

        if not referenceDate:
            self.referenceDate = datetime.date.today()
        elif isinstance(referenceDate,str):
            self.referenceDate = self.parse(referenceDate)
        else:
            self.referenceDate = referenceDate

        self.string = string

        date = []

        #Check for simple, pure number dates:
        dayFormat = r'(?P<day>\d{2})'
        monthFormat = r'(?P<month>\d{2})'
        yearFormat = r'(?P<year>\d{4}|\d{2})'
        simpleCombos = [[dayFormat,monthFormat,yearFormat],[yearFormat,monthFormat,dayFormat]]
        for combo in simpleCombos:
            pattern = '\D{1,2}?'.join(combo)
            r = re.compile(pattern)
            date = [found for found in r.finditer(string)]

            [match,date] = self.checkDate(date)
            if match:
               break

        #Complex date search:
        if not match:
            for combo in self.combinations:
                #Switch between months and relatives for second order unit according to which combination is in use.
                patternPart = {}

                if [True for c in combo if 'time' in c]:
                    patternPart['time'] = r'(?:(?:(?:kl)|(?:klokka)|(?:klokken))\D{1,2})?(?P<hour>\d{1,4})(?:\D(?P<minute>\d{2}))?(?:\D(?P<second>\d{2}))?'

                if [True for c in combo if 'relativeYear' in c]:
                     loopThrough = self.relativeYears
                     for Str,Num in loopThrough.items():
                        patternPart['relativeYear'] = r'(?P<month>(?i)%s)' % Str
                        patternPart['year'] = r'(?P<year>\d{4}|\d{2})'
                        [match,date] = self.checkPattern(patternPart,combo,Num)
                        if match: break

                elif [True for c in combo if 'relativeCentury' in c or 'century' in c]:
                     loopThrough = self.relativeCenturies
                     for Str,Num in loopThrough.items():
                        patternPart['century'] = r'(?P<century>(?i)%s)' % '|(?i)'.join(self.centuries)
                        patternPart['relativeCentury'] = r'(?P<relativeCentury>(?i)%s)' % '|(?i)'.join([Str])
                        [match,date] = self.checkPattern(patternPart,combo,Num,centuryCheck = True)
                        if match: break

                elif [True for c in combo if 'weekday' in c]:
                     loopThrough = self.weekdays
                     for Str,Num in loopThrough.items():
                        patternPart['weekday'] = r'(?P<weekday>(?i)%s)' % Str
                        [match,date] = self.checkPattern(patternPart,combo,Num)
                        if match: break

                else:
                    loopThrough = self.months
                    for Str,Num in loopThrough.items():
                        patternPart['day'] = r'(?P<day>\d{1,2})'
                        patternPart['month'] = r'(?P<month>(?i)%s)' % '|(?i)'.join([Str] + [r'(?:^|(?<=[^:\d]))0?' + str(Num) + r'(?:(?=[^:\d])|$)'])
                        patternPart['year'] = r'(?P<year>\d{4}|\d{2})'
                        [match,date] = self.checkPattern(patternPart,combo,Num)
                        if match: break
                if match:
                   break

        if debugMode:
           return [stringIn,combo,pattern,datetime.datetime(**date)]
        else:
            if match:
                return datetime.datetime(**date)
            else:
                return []

    def checkPattern(self,patternPart,combo,Num = 0,centuryCheck = False):
        #Run a pattern through the regular expression and return output.
        pattern = '(?:^|(?<=\D))' + '(?=[^:\d])[^:\d]{1,4}?(?<=[^:\d])'.join(combo) % patternPart  + '(?:(?=\D)|$)'

        r = re.compile(pattern)
        date = [found for found in r.finditer(self.string)]

        #Check integrity of match:
        [match,date] = self.checkDate(date,Num,centuryCheck)

        return [match,date]

    def checkDate(self,date,Num = 0,centuryCheck = False):
           #Takes an input date dictionary and check and massages the content until
           #until is fails or creates a passable date.
           match = True
           if not date:
               match = False
               return [match,date]
           elif not isinstance(date,dict):
                date = date[0].groupdict()
                for part in date:
                    if not part:
                       match = False
                       return[match,date]

           #Get first upcoming weekday
           if 'weekday' in date:
                if re.findall('^\d+$',date['weekday']):
                    dayOfTheWeek = int(date['weekday'])
                else:
                    dayOfTheWeek = self.weekdays[date['weekday']]
                delta = datetime.timedelta(days=1)
                i=0
                candidate = self.referenceDate+delta*i
                while not candidate.weekday() == dayOfTheWeek:
                    i+=1
                    candidate = self.referenceDate+delta*i
                date['day'] = str(candidate.day)
                date['month'] = str(candidate.month)
                date['year'] = str(candidate.year)

           #Check if days are found:
           if not 'day' in date:
              date['day'] = 1
           elif not date['day']:
                date['day'] = 1
           else:
                date['day'] = int(date['day'])

           #Get month number:
           if not 'month' in date:
              date['month'] = 1
           elif not date['month']:
                date['month'] = 1
           elif not re.findall(r'\d+',date['month']):
                date['month'] = Num
           else:
                date['month'] = int(date['month'])

           if date['month'] > 12:
                match = False
                return[match,date]

           #Check if days are valid amount:
           try: days[date['month']]
           except:
                  pass
           if date['day'] > self.days[date['month']]: #Days higher than monthly maximum.
                  match = False
                  return [match,date]

            #If only month/day is found, find first upcoming date matching the day/month combo.
           if not 'year' in date:
                today = datetime.datetime.today()
                currentYear = today.year
                if today.month > date['month']:
                    currentYear += 1
                elif today.month == date['month']:
                    if today.day > date['day']:
                        currentYear += 1
                date['year'] = str(currentYear) #Convert to string to not have to hamper code further down.

           if 'relativeCentury' in date:
              if date['relativeCentury']:
                 date['relativeCentury'] = Num
              else: date['relativeCentury'] = 0
           else: date['relativeCentury'] = 0

           if 'century' in date:
                 excerpt = re.findall('(?:' + '|'.join(self.centuries) + ')',date['century'])
                 if re.findall('\\d{2}.? århundre',date['century']):
                    #The first "århundre" starts with year 0, so we subtract to get the actual year:
                    correctCentury = -100
                 else:
                      correctCentury = 0
                 for d in excerpt[0]: #There should only be one hit here, we just don't know which.
                     if d:
                         date['year'] = d

           #Check two-number years and centuries;
           if len(date['year']) == 2 and centuryCheck:
              date['year'] = int(date['year'])*100 + date['relativeCentury'] + correctCentury

           elif len(date['year']) == 4 and centuryCheck:
                date['year'] = int(date['year']) + date['relativeCentury'] + correctCentury

           elif len(date['year']) == 4:
                date['year'] = int(date['year'])

           elif len((date['year'])) == 2:
              if int(date['year']) > int(str(datetime.datetime.now().year)[-2:]): #More than current two-number year.
                 date['year'] = int(date['year']) + 1900 #Assumed last century.
              else:
                   date['year'] = int(date['year']) + 2000 #Assumed this century.

           if 'hour'in date:
             if len(date['hour']) == 4:
                date['minute'] = date['hour'][2:4]
                date['hour'] = date['hour'][0:2]
             date['hour'] = int(date['hour'])
             if date['hour'] > 24 and date['hour'] < 0: match = False

             if 'minute' in date:
                if not date['minute']:
                    date['minute'] = 0
                date['minute'] = int(date['minute'])
                if date['minute'] > 60 and date['minute'] < 0: match = False

                if 'second' in date:
                  if not date['second']:
                    date['second'] = 0
                  date['second'] = int(date['second'])
                  if date['second'] > 60 and date['second'] < 0: match = False


           for k in list(date.keys()):
            if not k in ['year','month','day','hour','minute','second']:
                del date[k]

           return [match,date]

parser = dateParse()

def parse(string):
    return parser.parse(string)


if __name__ == '__main__':
    strings = ['14. mai 2012','14.05.2012 kl 1306','mandag 14:53','saturday']

    for string in strings:
        start= timer.clock()
        print(parse(string))
        print('\tTime spent: %0.6f' % (timer.clock()-start))

