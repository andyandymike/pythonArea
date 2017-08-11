#!/usr/bin/python
import sys

oldword = None
oldid = 0

for line in sys.stdin:
    date = line.strip().split('\t')
    word, id = date

    if oldword is None:
        oldword = word
        oldid = id
    if oldword == word:
        if oldid == id:
            pass
        if oldid != id:
            print('%s : id : %s' % (oldword, id))
            oldid = id
    if oldword != word:
        print('%s : id : %s' % (oldword, id))
        oldword = word
        oldid = id

if oldword is not None:
    print('%s : id : %s' % (oldword, id))
