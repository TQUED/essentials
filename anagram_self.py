#!/usr/bin/python

def anagram(s1, s2):

    list1 = list(s1)
    list2 = list(s2)
    
    list1.sort()
    list2.sort()
   
    pos = 0
    isOk = True
    
    while pos < len(list1) and isOk:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            isOk = False
    return isOk

a = anagram('abcd','dcba')
print a
