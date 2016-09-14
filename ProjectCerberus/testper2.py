__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testperjob.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testperjob.atl')


atllines = ReadFromFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testperjobori.atl')

i = 1
j = 100
for k in range(1, 100 + 1):
    tablename = 'hana.ANDY1.TESTPER' + str(i)
    sessionname = 'testper' + str(i)
    df1name = 'testper' + str(i) + '_1'
    df2name = 'testper' + str(i) + '_2'
    filename = 'testper' + str(i) + '.txt'

    guid1 = '60773dad-7c50-4fa1-9cb9-1945dfabf056'
    guid1new = '60773dad-7c50-4fa1-9cb9-1945dfabf' + str(j)
    guid2 = '5c292dcc-7f7d-413f-9266-064a9aae70e0'
    guid2new = '5c292dcc-7f7d-413f-9266-064a9aae7' + str(j)
    guid3 = 'fd151411-58ca-43ac-ba19-ad47f50a255b'
    guid3new = 'fd151411-58ca-43ac-ba19-ad47f50a2' + str(j)
    guid4 = 'c6d01507-b069-416a-af16-05fe6072acac'
    guid4new = 'c6d01507-b069-416a-af16-05fe6072a' + str(j)
    guid5 = '93b98cb1-099a-4e0c-8934-22f748c9e11a'
    guid5new = '93b98cb1-099a-4e0c-8934-22f748c9e' + str(j)
    guid6 = '09358427-9cac-4ef4-b265-a9ada28c8627'
    guid6new = '09358427-9cac-4ef4-b265-a9ada28c8' + str(j)
    guid7 = '3ea243a1-9e63-4042-bef5-3ddf6b447282'
    guid7new = '3ea243a1-9e63-4042-bef5-3ddf6b447' + str(j)
    guid8 = 'c6d01507-b069-416a-af16-05fe6072acac'
    guid8new = 'c6d01507-b069-416a-af16-05fe6072a' + str(j)
    guid9 = '33f11eb9-18d0-42e0-8dbd-5eaa4e276aa9'
    guid9new = '33f11eb9-18d0-42e0-8dbd-5eaa4e276' + str(j)
    guid10 = '2bd134c1-cdc0-4810-9341-433a48efcb8e'
    guid10new = '2bd134c1-cdc0-4810-9341-433a48efc' + str(j)
    guid11 = '1e43f84f-a867-4415-9796-dbc212b9f7b5'
    guid11new = '1e43f84f-a867-4415-9796-dbc212b9f' + str(j)

    i = i + 1
    j = j + 1

    for atlline in atllines:
        atlline = PurifyLine(atlline)
        atlline = atlline.replace('hana.ANDY1.TESTPER1', tablename)
        atlline = atlline.replace('sessionname', sessionname)
        atlline = atlline.replace('testper1_1', df1name)
        atlline = atlline.replace('testper1_2', df2name)
        atlline = atlline.replace('testper1.txt', filename)
        atlline = atlline.replace(guid1, guid1new)
        atlline = atlline.replace(guid11,guid11new)
        atlline = atlline.replace(guid2,guid2new)
        atlline = atlline.replace(guid3,guid3new)
        atlline = atlline.replace(guid4,guid4new)
        atlline = atlline.replace(guid5,guid5new)
        atlline = atlline.replace(guid6,guid6new)
        atlline = atlline.replace(guid7,guid7new)
        atlline = atlline.replace(guid8,guid8new)
        atlline = atlline.replace(guid9,guid9new)
        atlline = atlline.replace(guid10,guid10new)
        WriteToFile('C:\\Users\\i067382\\Documents\\DS\\bug\\DHR DS jobs hung due to AL_VERSION tabl\\testperjob.atl',atlline)