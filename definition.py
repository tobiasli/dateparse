# -*- coding: utf-8 -*-
weekdays = OrderedDict([
            ('mandag',0),
            ('tirsdag',1),
            ('onsdag',2),
            ('torsdag',3),
            ('fredag',4),
            ('lørdag',5),
            ('søndag',6),
            ('man',0),
            ('tir',1),
            ('ons',2),
            ('tor',3),
            ('fre',4),
            ('lør',5),
            ('søn',6),
            ('monday',0),
            ('tuesday',1),
            ('wednesday',2),
            ('thursday',3),
            ('friday',4),
            ('saturday',5),
            ('sunday',6),
            ('mon',0),
            ('tue',1),
            ('wed',2),
            ('th',3),
            ('fri',4),
            ('sat',5),
            ('sun',6),
            ])

#Month variations with month number:
months = OrderedDict([
                ('januar', 1),
                ('februar', 2),
                ('mars', 3),
                ('april', 4),
                ('mai', 5),
                ('juni', 6),
                ('juli', 7),
                ('august', 8),
                ('september', 9),
                ('oktober', 10),
                ('november', 11),
                ('desember', 12),
                ('january', 1),
                ('february', 2),
                ('march', 3),
                ('may', 5),
                ('june', 6),
                ('july', 7),
                ('october', 10),
                ('december', 12),
                ('jan', 1),
                ('feb', 2),
                ('mar', 3),
                ('apr', 4),
                ('jun', 6),
                ('jul', 7),
                ('aug', 8),
                ('sep', 9),
                ('okt', 10),
                ('nov', 11),
                ('des', 12),
                ('oct', 10),
                ('dec', 12)
                ])

#Number of valid days in each month:
days = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
        }

#Relative position in year. Numbers are the months corresponding to the
#start of the relative position (i.e. Q1 = 1 not 3)
relativeYears = {
            'sommer(?:en)?':6,
            'høst(?:en)?':9,
            'vinter(?:en)?':12,
            'vår(?:en)?':3,
            'første kvartal':1,
            '1. kvartal':1,
            'Q1':1,
            'andre kvartal':4,
            '2. kvartal':4,
            'Q2':4,
            'tredje kvartal':7,
            '3. kvartal':7,
            'Q3':7,
            'fjerde kvartal':10,
            '4. kvartal':10,
            'Q4':10,
            'første halvdel':1,
            'tidlig':1,
            'starten av':1,
            'andre halvdel':6,
            'midten av':6,
            'sent':10,
            }

#Identification of typical century variations:
centuries = [
             '(\\d{2}00)[-\s]tallet',
             '(\\d{2}).? århundre'
            ]
#Identification of various relative positions in centuries, with the
#corresponding year:
relativeCenturies = {
                'første halvdel av(?: det)?':0,
                'første kvartal':0,
                'andre kvartal':25,
                'tredje kvartal':50,
                'fjerde kvartal':75,
                'tidlig (?:i|på)(?: det)?':0,
                'starten av(?: det)?':0,
                'andre halvdel av(?: det)?':50,
                'midten av(?: det)?':50,
                'sent på(?: det)?':90,
                'slutten av(?: det)?':90,
                'begynnelsen av(?: det)?':0,
                }

day = '%(day)s'
month = '%(month)s'
year = '%(year)s'
time = '%(time)s'

weekday = '%(weekday)s'
relativeYear = '%(relativeYear)s'
century = '%(century)s'
relativeCentury = '%(relativeCentury)s'


#The order of what to look for. Higher complexity should come first for
#tests to not overlap. I.e, if [year] is placed first, it will trump
#everything.
combinations = [
             [day,month,year,time],
             [year,month,day,time],
             [time,day,month,year],
             [time,year,month,day],
             [day,month,year],
             [year,month,day],
             [day,month],
             [month,day],
             [weekday,time],
             [time,weekday],
             [weekday],
             [month,year],
             [year,month],
             [relativeCentury,century],
             [century,relativeCentury],
             [relativeYear,year],
             [year,relativeYear],
             [century],
             [year],
             ]

referenceDate = None
string = ''