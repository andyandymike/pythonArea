__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\ddl.txt')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\ddl.txt')


ddllines = ReadFromFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\ddlori.txt')

for ddlline in ddllines:
    print(ddlline)
    ddlline = PurifyLine(ddlline)
    for i in range(1, 100 + 1):
        insert = ddlline.replace('testper1', 'testper' + str(i))
        print(insert)
        WriteToFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\ddl.txt',insert)