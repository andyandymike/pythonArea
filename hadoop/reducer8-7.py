#!/usr/bin/python
import sys

oldtagname = None
num = 0
list = []
for i in range(10):
    list.append(('', 0))


def inserttop10(node):
    sorted(list, lambda x, y: cmp(x[1], y[1]))
    for i in range(10):
        if list[i][1] < node[1]:
            list.insert(i, node)
            list.pop()
            return


for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    tagname, id = data_mapped
    if oldtagname and oldtagname != tagname:
        inserttop10((oldtagname, num))
        num = 0
    num += 1
    oldtagname = tagname

if oldtagname != None:
    inserttop10((oldtagname, num))

for i in range(10):
    print(list[i])
