__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *
from os import *
from shutil import *

outputs = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\alloutputs.txt')

for output in outputs:
    line = '!sh adiff ${runtest}/goldlog/' + output + ' $DS_WORK/' + output
    WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\adiff.txt',line)