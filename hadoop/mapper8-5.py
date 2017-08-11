#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if data[0] == '\"id\"' or len(data) != 19:
        continue
    id = data[0]
    body = data[4]
    node_type = data[5]
    parent_id = data[6]
    if node_type == 'answer':
        id = parent_id
        node_type = '2'
    if node_type == 'question':
        node_type = '1'
    if node_type == '1' or node_type == '2':
        print('%s\t%s\t%s' % (id, node_type, body))
