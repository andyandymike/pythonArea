#!/usr/bin/python
import sys
import csv
import re

seps = '.,!?:;"()<>[]#$=-/'

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if data[0] == '\"id\"':
        continue
    author_id = data[3]
    added_at = data[8]
    reg = re.compile(r'\d\d\d\d-\d\d-\d\d\s(\d\d):\d\d:\d\d.+')
    match = reg.match(added_at)
    if match:
        hour = match.group(1)
        print('%s\t%s' % (author_id, hour))
