#!/usr/bin/python

fo = open("foo.txt", "wb")

print "name of the file : ", fo.name
print "File opening mode : ", fo.mode
print "Closed or not :", fo.closed
print "Softspace flag :", fo.softspace

fo.close()

print "Closed or not ?", fo.closed

fo = open("foo.txt", "wb")

fo.write("Python is a great language!!!Yeah its really cool :)")

print "file closed or not ?" , fo.closed

fo.write("\n Add next line to foo \n")
