#!/usr/bin/python
import sys
import csv

seps = '.,!?:;"()<>[]#$=-/'

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if data[0] == '\"id\"':
        continue
    id = data[0]
    body = data[4].strip()[1:-1].strip()
    for sep in seps:
        body = body.replace(sep, ' ')
    words = body.split()
    for index, word in enumerate(words):
        print('%s\t%s\t%s' % (word.lower(), id, index + 1))
