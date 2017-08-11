#!/usr/bin/python
import sys

num = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    request, status = data_mapped
    if request.find('/assets/js/the-associates.js') != -1 and (int(status) == 200 or int(status) == 304):
        num += 1

print('hit number: %s' % num)
