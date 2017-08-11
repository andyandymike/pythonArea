#!/usr/bin/python
import sys

valuesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
        print('%s\t%s' % (oldKey, valuesTotal))
        oldKey = thisKey
        valuesTotal = 0
    oldKey = thisKey
    valuesTotal += float(thisValue)
if oldKey != None:
    print('%s\t%s' % (oldKey, valuesTotal))
