__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\table.txt')
print(len(tables))
for table in tables:
    if table.upper().find('CREATE') != -1:
        table = table.upper().replace('CREATE','')
        table = table.upper().replace('COLUMN','')
        table = table.upper().replace('TABLE','')
        table = table.upper().replace('(','')
        table = PurifyLine(table.upper(),' ')
        if table.find('PARTITION_TARGET_1') != -1:
            continue
        #if table.find('HASH_BIGINT_NP_1') != -1:
        #    continue
        #if table.find('HASH_BIGINT_P_1') != -1:
        #    continue
        #if table.find('HASH_DATE_NP_1') != -1:
        #    continue
        #if table.find('HASH_DATE_P_1') != -1:
        #    continue
        #if table.find('HASH_DECIMAL_NP_1') != -1:
        #    continue
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt',table.upper())
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt','HASHHASH_BIGINT_NP_1')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt','HASHHASH_BIGINT_P_1')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt','HASHHASH_DATE_NP_1')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt','HASHHASH_DATE_P_1')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt','HASHHASH_DECIMAL_NP_1')

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\dfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\dfs.atl')
WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\dfs.atl','#__AW_Repository_Version \'14.2.6.0000\';')
WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\dfs.atl','#__AW_Product_Version \'14.2.6.943\';')
WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\dfs.atl','#__AW_ATL_Locale \'zho_cn.utf-8\';')
df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\df.txt')
tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    dfname = 'testcase021_1_df' + str(i)
    guid1 = '677f92a9-b72e-40bb-9c78-0f98d303b4d3'
    guid1new = '677f92a9-b72e-40bb-9c78-0f98d303b' + str(j)
    guid2 = '4dd4cd34-57a0-40ff-a389-06fadef87fa8'
    guid2new = '4dd4cd34-57a0-40ff-a389-06fadef87' + str(j)
    i = i + 1
    j = j + 1
    for dfline in df:
        dfline = dfline.replace('testcase021_5',dfname)
        dfline = dfline.replace('HASH_DECIMAL_NP_1',table)
        dfline = dfline.replace(guid1,guid1new)
        dfline = dfline.replace(guid2,guid2new)
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\dfs.atl',dfline)


FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\wfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\wfs.atl')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\wfs.atl','#__AW_Repository_Version \'14.2.6.0000\';')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\wfs.atl','#__AW_Product_Version \'14.2.6.943\';')
#WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\wfs.atl','#__AW_ATL_Locale \'zho_cn.utf-8\';')
wf = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\wft.atl')
tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    wfname = 'testcase021_1_wf' + str(i)
    wfoutname = 'testcase021_1_wf' + str(i)
    dfname = 'testcase021_1_df' + str(i)
    guid1 = '677f92a9-b72e-40bb-9c78-0f98d303b4d2'
    guid1new = '677f92a9-b72e-40bb-9c78-0f98d303b' + str(j)
    guid2 = 'd5cfa225-a01f-4d1b-8f32-ba5f7a0b77ed'
    guid2new = 'd5cfa225-a01f-4d1b-8f32-ba5f7a0b7' + str(j)
    guid3 = 'd9602726-0411-45c9-ac3d-0ce700b6e642'
    guid3new = 'd9602726-0411-45c9-ac3d-0ce700b6e' + str(j)
    #guid4 = 'dc35b9bd-3d55-444c-912e-576656f8c362'
    #guid4new = 'dc35b9bd-3d55-444c-912e-576656f8c' + str(j)
    guid5 = 'a25581c0-e5aa-449f-9a65-686302d2eba5'
    guid5new = 'a25581c0-e5aa-449f-9a65-686302d2e' + str(j)
    guid6 = '4dd4cd34-57a0-40ff-a389-06fadef87fa7'
    guid6new = '4dd4cd34-57a0-40ff-a389-06fadef87' + str(j)
    guid7 = 'fcc101dc-657f-49ea-89ac-4f38cecae04d'
    guid7new = 'fcc101dc-657f-49ea-89ac-4f38cecae' + str(j)
    guid8 = '099609b3-68d6-4e8b-b98a-ddbb617660c6'
    guid8new ='099609b3-68d6-4e8b-b98a-ddbb61766' + str(j)
    i = i + 1
    j = j + 1
    for wdline in wf:
        wdline = wdline.replace('test',wfname)
        wdline = wdline.replace('HASH_BIGINT_NP_1',table)
        wdline = wdline.replace('dfn',dfname)
        wdline = wdline.replace(guid1,guid1new)
        wdline = wdline.replace(guid2,guid2new)
        wdline = wdline.replace(guid3,guid3new)
        #wdline = wdline.replace(guid4,guid4new)
        wdline = wdline.replace(guid5,guid5new)
        wdline = wdline.replace(guid6,guid6new)
        wdline = wdline.replace(guid7,guid7new)
        wdline = wdline.replace(guid8,guid8new)
        wdline = wdline.replace('outname',wfoutname)
        wdline = wdline.replace('outdf','testcase021_file_1')
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\wfs.atl',wdline)

