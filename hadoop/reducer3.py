#!/usr/bin/python
import sys

num = 0
sales = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisKey, thisCost = data_mapped
    num += 1
    sales += float(thisCost)
print('Number of sales: %s' % num)
print('Total value of sales: %s' % sales)
