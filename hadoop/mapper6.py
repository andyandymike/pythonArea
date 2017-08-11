#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    reg = re.compile(r'(\d+\.\d+.\d+.\d+)\s(.+)\s(.+)\s(\[.+\])\s(\".+\")\s(\d\d\d)\s(\d+|-)')
    match = reg.match(line)
    if match is None or len(match.groups()) != 7:
        continue
    request = match.group(5)
    reg_filepath = re.compile(r'\"\w+\s(.+?)\s.+\"')
    match = reg_filepath.match(request)
    if match is None:
        continue
    filepath = match.groups(1)[0].replace('http://www.the-associates.co.uk', '')
    reg_suffix = re.compile(r'.+?\.\w+')
    match = reg_suffix.match(filepath)
    if match is None:
        continue
    print("%s" % filepath)
