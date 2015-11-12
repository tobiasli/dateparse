#-------------------------------------------------------------------------------
# Name:        GroceryShopping_Test_Suite
# Purpose:      Test the components of the groceries class.
#
# Author:      Tobias
#
# Created:     01.05.2015
# Copyright:   (c) Tobias 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import datetime
import sys
import os

sys.path = [os.path.split(os.path.dirname(__file__))[0] + os.path.sep] + sys.path

TEST_CASES = [
        ('14. mai 2012',datetime.datetime(2012,5,14,0,0,0)),
        ('14.05.2012 kl 1306',datetime.datetime(2012,5,14,13,6,0)),
        ('midten av 1600-tallet',datetime.datetime(1650,1,1,0,0,0)),
        ('starten av det 19. århundre',datetime.datetime(1800,1,1,0,0,0))
        ]

class TestDateparseModule(unittest.TestCase):

    def test_parse_method(self):
        import main
        for candidate, response in TEST_CASES:
            self.assertTrue(main.parse(candidate),response)

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDateparseModule)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run()