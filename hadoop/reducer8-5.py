#!/usr/bin/python
import sys

oldid = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 3:
        continue
    id, node_type, body = data_mapped
    if node_type == '1':
        ql = len(body)
    if oldid and oldid != id:
        if an == 0:
            print('%s\t%s\t%s' % (oldid, ql, 0))
        else:
            aal = al/an
            print('%s\t%s\t%s' % (oldid, ql, aal))
    if node_type == '2':
        al += len(body)
        an += 1
    oldid = id

if oldid != None:
    if an == 0:
        print('%s\t%s\t%s' % (oldid, ql, 0))
    else:
        aal = al / an
        print('%s\t%s\t%s' % (oldid, ql, aal))