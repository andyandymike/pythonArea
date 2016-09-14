__author__ = 'I067382'

import testperfunc
from testperfunc import *

batlines = ReadFromFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testper1.bat')
txtlines = ReadFromFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testper1.txt')

for batline in batlines:
    print(batline)
    batline = PurifyLine(batline)
    for i in range(1, 100 + 1):
        FileStatus = os.path.isfile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testbat\\testper' + str(i) + '.bat')
        if FileStatus is True:
            os.remove('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testbat\\testper' + str(i) + '.bat')

        insert = batline.replace('testper1', 'testper' + str(i))
        print(insert)
        WriteToFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testbat\\testper' + str(i) + '.bat',insert)

for txtline in txtlines:
    print(txtline)
    txtline = PurifyLine(txtline)
    for i in range(1, 100 + 1):
        FileStatus = os.path.isfile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testbat\\testper' + str(i) + '.txt')
        if FileStatus is True:
            os.remove('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testbat\\testper' + str(i) + '.txt')

        insert = txtline.replace('testper1', 'testper' + str(i))
        print(insert)
        WriteToFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testbat\\testper' + str(i) + '.txt',insert)