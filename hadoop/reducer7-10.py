#!/usr/bin/python
import sys
from datetime import datetime

moSales = 0.0
tuSales = 0.0
weSales = 0.0
thSales = 0.0
frSales = 0.0
saSales = 0.0
suSales = 0.0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisdate, thisValue = data_mapped
    weekday = datetime.strptime(thisdate, "%Y-%m-%d").weekday()
    if weekday == 0:
        moSales += float(thisValue)
    elif weekday == 1:
        tuSales += float(thisValue)
    elif weekday == 2:
        weSales += float(thisValue)
    elif weekday == 3:
        thSales += float(thisValue)
    elif weekday == 4:
        frSales += float(thisValue)
    elif weekday == 5:
        saSales += float(thisValue)
    elif weekday == 6:
        suSales += float(thisValue)

print('sales for Mo: %f' % moSales)
print('sales for Tu: %f' % tuSales)
print('sales for We: %f' % weSales)
print('sales for Th: %f' % thSales)
print('sales for Fr: %f' % frSales)
print('sales for Sa: %f' % saSales)
print('sales for Su: %f' % suSales)