#!/usr/bin/python

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed = []

for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
 
#    print transposed_matrix

    transposed.append(transposed_row)

transposed

print transposed

c = zip(*matrix)

print c
