#!/usr/bin/python
import sys

oldid = None
mosthour = '00'
hourcount = {}
for i in range(10):
    hourcount['0' + str(i)] = 0
for i in range(10, 24):
    hourcount[str(i)] = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisid, thishour = data_mapped
    if oldid and oldid != thisid:
        for i in range(10):
            if hourcount['0' + str(i)] > hourcount[mosthour]:
                mosthour = '0' + str(i)
        for i in range(10, 24):
            if hourcount[str(i)] > hourcount[mosthour]:
                mosthour = str(i)
        print('%s\t%s' % (thisid, mosthour))
        oldKey = thisid
        mosthour = '00'
        hourcount = {}
        for i in range(10):
            hourcount['0' + str(i)] = 0
        for i in range(10, 24):
            hourcount[str(i)] = 0

    oldid = thisid
    hourcount[thishour] += 1