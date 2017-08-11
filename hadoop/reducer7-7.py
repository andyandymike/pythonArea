#!/usr/bin/python
import sys

num = 0
oldword = None

for line in sys.stdin:
    date = line.strip().split('\t')
    word, id, index = date

    if oldword is None:
        oldword = word
    if oldword == word:
        num += 1
    if oldword != word:
        print('%s : count : %s' % (oldword, num))
        oldword = word
        num += 1

if oldword is not None:
    print('%s : count : %s' % (oldword, num))