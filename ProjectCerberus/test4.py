__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\testcase.txt')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\testcase.txt')

jobline = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\t.txt')

flag = False
for job in jobline:
    if job.find('!testcase') != -1:
        if job.find('ShudGiveNoError') != -1:
            flag = True
            WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\testcase.txt',job)
            continue
        else:
            flag = False
    if flag is True:
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\testcase.txt',job)