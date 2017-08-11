#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if data[0] == '\"id\"' or len(data) != 19:
        continue
    id = data[0]
    author_id = data[3]
    node_type = data[5]
    parent_id = data[6]
    if node_type == 'question':
        print('%s\t%s' % (id, author_id))
    else:
        print('%s\t%s' % (parent_id, author_id))
