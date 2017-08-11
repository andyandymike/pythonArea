#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if data[0] == '\"id\"' or len(data) != 19:
        continue
    id = data[0]
    tagnames = data[2]
    node_type = data[5]
    if node_type == 'question':
        for tagname in tagnames.strip().split(" "):
            print('%s\t%s' % (tagname, id))
