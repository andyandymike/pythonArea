#!/usr/bin/python
import sys

oldid = None
studentset = set()

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisid, thisaid = data_mapped
    if oldid and oldid != thisid:
        print('%s\t%s' % (oldid, studentset))
        studentset = set()
        oldid = thisid
    studentset.add(thisaid)
    oldid = thisid

if oldid != None:
    print('%s\t%s' % (oldid, studentset))