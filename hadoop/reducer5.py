#!/usr/bin/python
import sys

num = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    ip, status = data_mapped
    if ip == '10.99.99.186' and (int(status) == 200 or int(status) == 304):
        num += 1

print('hit number: %s' % num)
