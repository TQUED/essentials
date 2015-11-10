#!/usr/bin/python

while True:
    try:
        x = int(input("Please input a number"))
        print x
        break
    except:
        print("Ooops!! VALUE ERROR exception caught")
