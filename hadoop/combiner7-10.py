#!/usr/bin/python
import sys

oldDate = None
totalCost = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisDate, thisCost = data_mapped
    if oldDate and oldDate != thisDate:
        print('%s\t%s' % (oldDate, totalCost))
        oldDate = thisDate
        totalCost = 0
    oldDate = thisDate
    totalCost += float(thisCost)
if oldDate != None:
    print('%s\t%s' % (oldDate, totalCost))
