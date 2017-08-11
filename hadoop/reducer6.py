#!/usr/bin/python
import sys

num = 0
oldpath = None
mostnum = 0
mostfilepath = None

for line in sys.stdin:
    if oldpath is None:
        oldpath = line
    if line == oldpath:
        num += 1
    if line != oldpath:
        if num > mostnum:
            mostnum = num
            mostfilepath = oldpath
        oldpath = line
        num = 0

if oldpath is not None:
    if num > mostnum:
        mostnum = num
        mostfilepath = oldpath

print('%s : count : %s' % (mostfilepath, mostnum))
