#!/usr/bin/python

import hexa      # This is the code being tested 
import unittest

class Samples(unittest.TestCase):
    pair = ( (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'),
             (6,'6'), (7,'7'), (8,'8'), (9,'9'), (10,'A'),
             (11,'B'), (12,'C'), (13,'D'), (14,'E'), (15,'F'),
             (16,'10'), (30,'1E'), (127,'7F'), (255,'FF'), (500,'1F4'),
             (1024,'400'), (5100,'13EC'), (65535,'FFFF'), (65536,'10000') )

    def testToHexa(self):
        for d, h in self.pair:
            res =  hexa.toHexa(d);
            self.assertEqual(h, res)

class BadSamples(unittest.TestCase):
    def testToHexaNegative(self):
        ''' toHex should fail when the input < 0'''
        self.assertRaises(hexa.OutOfRangeError, hexa.toHexa, -1)

    def testToHexaNonInteger(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(hexa.NotIntegerError, hexa.toHexa, 'C')

if __name__ == '__main__':
    unittest.main()
