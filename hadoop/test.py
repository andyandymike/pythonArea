#!/usr/bin/python
import sys
import re

line = '10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 10469'
reg = re.compile(r'(\d+\.\d+.\d+.\d+)\s(.+)\s(.+)\s(\[.+\])\s(\".+\")\s(\d\d\d)\s(\d+|-)')
match = reg.match(line)
if match is None or len(match.groups()) != 7:
    print('1 no match')
request = match.group(5)
print(request)
reg_filepath = re.compile(r'\"\w+\s(.+?)\s.+\"')
match = reg_filepath.match(request)
if match is None:
    print('2 no match')
print(match.group(1))
filepath = match.groups(1)
filepath = filepath[0].replace('http://www.the-associates.co.uk', '')
reg_suffix = re.compile(r'.+?\.\w+')
match = reg_suffix.match(filepath)
if match is None:
    print('no match file')
print("%s" % filepath)

num = 0
oldpath = None

if oldpath is None:
    oldpath = filepath
if filepath == oldpath:
    num += 1
if filepath != oldpath:
    print('%s\tcount:\t%s' % (oldpath, num))
    oldpath = filepath
    num = 0

if oldpath is not None:
    print('%s\tcount:\t%s' % (oldpath, num))
