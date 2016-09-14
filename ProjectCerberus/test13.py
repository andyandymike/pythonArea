__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\ct48dfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\ct48dfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\ct48df.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase048_1_wf' + str(i) + '.out'
    dfname = 'testcase048_1_df' + str(i)
    wfname = 'testcase048_1_wf' + str(i)
    dstgt = 'hana_partition02'
    guid1 = '30c2a4aa-225f-42dc-b143-34e46ff935bc'
    guid1new = '30c2a4aa-225f-42dc-b143-34e46ff93' + str(j)
    guid2 = '6a61211b-bc71-491f-a0a8-3f32abd18100'
    guid2new = '6a61211b-bc71-491f-a0a8-3f32abd18' + str(j)
    guid3 = '6acac8b6-9ac0-4ef5-a9ac-35f7e2815100'
    guid3new = '6acac8b6-9ac0-4ef5-a9ac-35f7e2815' + str(j)
    guid4 = 'a44ec6fc-eaec-443c-9c72-f8ce86c60100'
    guid4new = 'a44ec6fc-eaec-443c-9c72-f8ce86c60' + str(j)

    guid5 = '394bbb92-79bd-4721-ad9a-fc812143b100'
    guid5new = '394bbb92-79bd-4721-ad9a-fc812143b' + str(j)
    guid6 = '81bee613-4c6a-4216-9135-d550b26217e6'
    guid6new = '81bee613-4c6a-4216-9135-d550b2621' + str(j)
    guid7 = '2ab307bd-7caf-434d-a3b3-57dfcb752178'
    guid7new = '2ab307bd-7caf-434d-a3b3-57dfcb752' + str(j)
    guid8 = 'eddbcc81-7900-4899-b01c-746671119548'
    guid8new = 'eddbcc81-7900-4899-b01c-746671119' + str(j)
    guid9 = '6daee4d6-f28c-4c43-8d34-1a823822db96'
    guid9new ='6daee4d6-f28c-4c43-8d34-1a823822d' + str(j)
    guid10 = 'b4ed387e-45bd-4e3c-8b42-f485beb38e99'
    guid10new = 'b4ed387e-45bd-4e3c-8b42-f485beb38' + str(j)
    i = i + 1
    j = j + 1
    for dfline in df:
        dfline = dfline.replace('testcase048_1_wf1',wfname)
        dfline = dfline.replace('out.out',outname)
        dfline = dfline.replace('RANGE_INT_NP_1',table)
        #dfline = dfline.replace('RANGE_INT_NP_2',table.replace('1', '2'))
        oldstring = table + '.ID = MORE_PARTINUM_TABLE_1.ID'
        if table.upper().find('_INT') != -1:
            dfline = dfline.replace(oldstring, table + '.INTCOL = MORE_PARTINUM_TABLE_1.INTCOL')
        if table.upper().find('_TINYINT') != -1:
            dfline = dfline.replace(oldstring, table + '.TINYINTCOL = MORE_PARTINUM_TABLE_1.TINYINTCOL')
        if table.upper().find('_SMALLINT') != -1:
            dfline = dfline.replace(oldstring, table + '.SMALLINTCOL = MORE_PARTINUM_TABLE_1.SMALLINTCOL')
        if table.upper().find('_BIGINT') != -1:
            dfline = dfline.replace(oldstring, table + '.BIGINTCOL = MORE_PARTINUM_TABLE_1.BIGINTCOL')
        if table.upper().find('_DATE') != -1:
            dfline = dfline.replace(oldstring, table + '.DATECOL = MORE_PARTINUM_TABLE_1.DATECOL')
        if table.upper().find('_SECONDDATE') != -1:
            dfline = dfline.replace(oldstring, table + '.SECONDDATECOL = MORE_PARTINUM_TABLE_1.SECONDDATECOL')
        if table.upper().find('_TIMESTAMP') != -1:
            dfline = dfline.replace(oldstring, table + '.TIMESTAMPCOL = MORE_PARTINUM_TABLE_1.TIMESTAMPCOL')
        if table.upper().find('_VARHCAR') != -1:
            dfline = dfline.replace(oldstring, table + '.VARCHARCOL = MORE_PARTINUM_TABLE_1.VARCHARCOL')
        if table.upper().find('_NVARHCAR') != -1:
            dfline = dfline.replace(oldstring, table + '.NVARCHARCOL = MORE_PARTINUM_TABLE_1.NVARCHARCOL')
        if table.upper().find('_VARCHAR') != -1:
            dfline = dfline.replace(oldstring, table + '.VARCHARCOL = MORE_PARTINUM_TABLE_1.VARCHARCOL')
        if table.upper().find('_NVARCHAR') != -1:
            dfline = dfline.replace(oldstring, table + '.NVARCHARCOL = MORE_PARTINUM_TABLE_1.NVARCHARCOL')
        if table.upper().find('_DECIMAL') != -1:
            dfline = dfline.replace(oldstring, table + '.DECIMALCOL = MORE_PARTINUM_TABLE_1.DECIMALCOL')
        if table.upper().find('_SMALLDECIMAL') != -1:
            dfline = dfline.replace(oldstring, table + '.SMALLDECIMALCOL = MORE_PARTINUM_TABLE_1.SMALLDECIMALCOL')
        if table.upper().find('_REAL') != -1:
            dfline = dfline.replace(oldstring, table + '.REALCOL = MORE_PARTINUM_TABLE_1.REALCOL')
        if table.upper().find('_DOUBLE') != -1:
            dfline = dfline.replace(oldstring, table + '.DOUBLECOL = MORE_PARTINUM_TABLE_1.DOUBLECOL')
        if table.upper().find('_ALPHANUM') != -1:
            dfline = dfline.replace(oldstring, table + '.ALPHANUMCOL = MORE_PARTINUM_TABLE_1.ALPHANUMCOL')
        if table.upper().find('_TIME') != -1:
            dfline = dfline.replace(oldstring, table + '.TIMECOL = MORE_PARTINUM_TABLE_1.TIMECOL')
        dfline = dfline.replace('testcase048_1_df1',dfname)
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
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\ct48dfs.atl',dfline)
