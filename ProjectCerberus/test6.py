__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *
from os import *
from shutil import *

#FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\missoutput-pre.txt')
#if FileStatus is True:
#    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\missoutput-pre.txt')

outputs = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\alloutputs.txt')
checkoutputs = listdir('C:\\Users\\i067382\\Documents\\DS\\Hana partition\\partition-sd')


for output in outputs:
    if output not in checkoutputs:
        print(output)
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\missoutput-std.txt',output)