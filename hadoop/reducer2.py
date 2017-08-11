#!/usr/bin/python
import sys

highest = 0.0
oldStore = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisStore, thisCost = data_mapped
    if oldStore and oldStore != thisStore:
        print('%s\t%s' % (oldStore, highest))
        oldStore = thisStore
        highest = 0.0
    oldStore = thisStore
    if float(thisCost) > highest:
        highest = float(thisCost)
if oldStore != None:
    print('%s\t%s' % (oldStore, highest))
