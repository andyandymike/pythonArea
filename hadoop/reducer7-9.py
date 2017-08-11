#!/usr/bin/python
import sys
from datetime import datetime

valuesTotal = 0
num = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisdate, thisValue = data_mapped
    weekday = datetime.strptime(thisdate, "%Y-%m-%d").weekday()
    if weekday == 6:
        valuesTotal += float(thisValue)
        num += 1

if num != 0:
    print('sunday average sales: %f' % (valuesTotal/num))
