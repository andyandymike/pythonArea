#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    reg = re.compile(r'(\d+\.\d+.\d+.\d+)\s(.+)\s(.+)\s(\[.+\])\s(\".+\")\s(\d\d\d)\s(\d+|-)')
    match = reg.match(line)
    if match is None or len(match.groups()) != 7:
        continue
    request = match.group(5)
    status = match.group(6)
    print("%s\t%s" % (request, status))
