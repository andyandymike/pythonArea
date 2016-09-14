__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

#FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\t221wfs.atl')
#if FileStatus is True:
#    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\t221wfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\t531wf.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase053_1_wf' + str(i) + '.out'
    dfname = 'testcase053_1_df' + str(i)
    wfname = 'testcase053_1_wf' + str(i)
    dstgt = 'hana_partition01'
    guid1 = 'dc35b9bd-3d55-444c-912e-576656f8c362'
    guid1new = 'dc35b9bd-3d55-444c-912e-576656f8c' + str(j)
    guid2 = 'fcc101dc-657f-49ea-89ac-4f38cecae214'
    guid2new = 'fcc101dc-657f-49ea-89ac-4f38cecae' + str(j)
    guid3 = '099609b3-68d6-4e8b-b98a-ddbb61766214'
    guid3new = '099609b3-68d6-4e8b-b98a-ddbb61766' + str(j)
    guid4 = 'facd480c-c9fb-4750-9fcc-1a2c58cb8d12'
    guid4new = 'facd480c-c9fb-4750-9fcc-1a2c58cb8' + str(j)

    guid5 = '800092f6-00f8-42dc-9f16-122907826e4b'
    guid5new = '800092f6-00f8-42dc-9f16-122907826' + str(j)
    guid6 = '1e0c3e5d-5f71-45fb-be08-f1488f10cace'
    guid6new = '1e0c3e5d-5f71-45fb-be08-f1488f10c' + str(j)
    guid7 = '88b419fd-dda1-4638-a708-959512d6feb8'
    guid7new = '88b419fd-dda1-4638-a708-959512d6f' + str(j)
    guid8 = 'ad8f3039-4a43-496e-a373-f124f60e9221'
    guid8new = 'ad8f3039-4a43-496e-a373-f124f60e9' + str(j)
    guid9 = 'b9e5e851-6546-41d2-81a0-7cddfc12a071'
    guid9new ='b9e5e851-6546-41d2-81a0-7cddfc12a' + str(j)
    guid10 = '9ae285a2-eab6-4ea3-8ede-02f0186f9873'
    guid10new = '9ae285a2-eab6-4ea3-8ede-02f0186f9' + str(j)
    i = i + 1
    j = j + 1
    for dfline in df:
        dfline = dfline.replace('testcase053_1_wf1',wfname)
        dfline = dfline.replace('out.out',outname)
        dfline = dfline.replace('RANGE_INT_NP_1',table)
        #dfline = dfline.replace('HASH_BIGINT_NP_1',table)
        dfline = dfline.replace('testcase053_1_df1',dfname)
        #dfline = dfline.replace('hana_partition02',dstgt)
        dfline = dfline.replace(guid1,guid1new)
        dfline = dfline.replace(guid2,guid2new)
        dfline = dfline.replace(guid3,guid3new)
        dfline = dfline.replace(guid4,guid4new)
        dfline = dfline.replace(guid5,guid5new)
        dfline = dfline.replace(guid6,guid6new)
        dfline = dfline.replace(guid7,guid7new)
        dfline = dfline.replace(guid8,guid8new)
        dfline = dfline.replace(guid9,guid9new)
        dfline = dfline.replace(guid10,guid10new)
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\t531wfs.atl',dfline)
