#!/usr/bin/env python

import datetime as d

time = "11:00:16 IST 2015"

class CheckVariableScope(object):
    __name = "Niraj"
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
   
    def printAbsoluteDate(self):
        return "Absolute time is : + %s/%s/%s %s " %(self.year, self.month, self.day, d.time)

    def printName(self):
        print name
  

def printAbsoluteDate():
    return "Date is %s" %(d.time)

a = CheckVariableScope(1993, "May", 5)
#timeIs = a.printAbsoluteDate()
#print timeIs

a.printName()

#defVal = printAbsoluteDate()
#print defVal
