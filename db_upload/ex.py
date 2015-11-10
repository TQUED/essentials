#!/usr/bin/python

class TestResultsModel(object):
    def __init__(self, tid, release, version, component, status, category, description):
        self.tid         = tid
        self.release     = release
        self.version     = version
        self.component   = component
        self.status      = status
        self.category    = category
        self.description = description

    # Returns the testresults as dictionary of items
    def asDict(self):
        testresults = {
           'tid'         : self.tid,
           'release'     : self.release,
           'version'     : self.version,
           'component'   : self.component,
           'status'      : self.status,
           'category'    : self.category,
           'description' : self.description
        }
        return testresults



def process(testresultFile):
    '''Returns testresults models as a list'''
    l = []
    with open(testresultFile, 'r') as f:
        for line in f:
            tid, rel, ver, comp, status, category, description = line.strip('\n').split(",")
            l.append(TestResultsModel(tid, rel, ver, comp, status, category, description).asDict())
    return l
a = process('data')
print a
