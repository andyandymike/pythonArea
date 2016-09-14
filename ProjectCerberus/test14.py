__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\ct49dfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\ct49dfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\ct49df.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase049_1_wf' + str(i) + '.out'
    dfname = 'testcase049_1_df' + str(i)
    wfname = 'testcase049_1_wf' + str(i)
    dstgt = 'hana_partition02'
    guid1 = '41ceab64-59bc-4467-9af4-44f9b120256d'
    guid1new = '41ceab64-59bc-4467-9af4-44f9b1202' + str(j)
    guid2 = 'fefffaa4-628e-40bd-8a20-af27dbf9b100'
    guid2new = 'fefffaa4-628e-40bd-8a20-af27dbf9b' + str(j)
    guid3 = '199db901-26c6-4b4a-8c5c-1d74dbaf7100'
    guid3new = '903a6f77-0515-458f-abf0-4cacddc3a100' + str(j)
    guid4 = 'ebe3d9ce-3e96-484b-8a8b-41387282e100'
    guid4new = 'ebe3d9ce-3e96-484b-8a8b-41387282e' + str(j)

    guid5 = 'a6d77fab-9293-40d9-b344-66a98c2374d4'
    guid5new = 'a6d77fab-9293-40d9-b344-66a98c237' + str(j)
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
        dfline = dfline.replace('testcase049_1_wf1',wfname)
        dfline = dfline.replace('out.out',outname)
        dfline = dfline.replace('RANGE_INT_NP_1',table)
        dfline = dfline.replace('RANGE_INT_NP_2',table.replace('1', '2'))
        oldstring = table + '.ID = ' + table.replace('1', '2') + '.ID'
        if table.upper().find('_INT') != -1:
            dfline = dfline.replace(oldstring, table + '.INTCOL = ' + table.replace('1', '2') + '.INTCOL')
        if table.upper().find('_TINYINT') != -1:
            dfline = dfline.replace(oldstring, table + '.TINYINTCOL = ' + table.replace('1', '2') + '.TINYINTCOL')
        if table.upper().find('_SMALLINT') != -1:
            dfline = dfline.replace(oldstring, table + '.SMALLINTCOL = ' + table.replace('1', '2') + '.SMALLINTCOL')
        if table.upper().find('_BIGINT') != -1:
            dfline = dfline.replace(oldstring, table + '.BIGINTCOL = ' + table.replace('1', '2') + '.BIGINTCOL')
        if table.upper().find('_DATE') != -1:
            dfline = dfline.replace(oldstring, table + '.DATECOL = ' + table.replace('1', '2') + '.DATECOL')
        if table.upper().find('_SECONDDATE') != -1:
            dfline = dfline.replace(oldstring, table + '.SECONDDATECOL = ' + table.replace('1', '2') + '.SECONDDATECOL')
        if table.upper().find('_TIMESTAMP') != -1:
            dfline = dfline.replace(oldstring, table + '.TIMESTAMPCOL = ' + table.replace('1', '2') + '.TIMESTAMPCOL')
        if table.upper().find('_VARHCAR') != -1:
            dfline = dfline.replace(oldstring, table + '.VARCHARCOL = ' + table.replace('1', '2') + '.VARCHARCOL')
        if table.upper().find('_NVARHCAR') != -1:
            dfline = dfline.replace(oldstring, table + '.NVARCHARCOL = ' + table.replace('1', '2') + '.NVARCHARCOL')
        if table.upper().find('_VARCHAR') != -1:
            dfline = dfline.replace(oldstring, table + '.VARCHARCOL = ' + table.replace('1', '2') + '.VARCHARCOL')
        if table.upper().find('_NVARCHAR') != -1:
            dfline = dfline.replace(oldstring, table + '.NVARCHARCOL = ' + table.replace('1', '2') + '.NVARCHARCOL')
        if table.upper().find('_DECIMAL') != -1:
            dfline = dfline.replace(oldstring, table + '.DECIMALCOL = ' + table.replace('1', '2') + '.DECIMALCOL')
        if table.upper().find('_SMALLDECIMAL') != -1:
            dfline = dfline.replace(oldstring, table + '.SMALLDECIMALCOL = ' + table.replace('1', '2') + '.SMALLDECIMALCOL')
        if table.upper().find('_REAL') != -1:
            dfline = dfline.replace(oldstring, table + '.REALCOL = ' + table.replace('1', '2') + '.REALCOL')
        if table.upper().find('_DOUBLE') != -1:
            dfline = dfline.replace(oldstring, table + '.DOUBLECOL = ' + table.replace('1', '2') + '.DOUBLECOL')
        if table.upper().find('_ALPHANUM') != -1:
            dfline = dfline.replace(oldstring, table + '.ALPHANUMCOL = ' + table.replace('1', '2') + '.ALPHANUMCOL')
        if table.upper().find('_TIME') != -1:
            dfline = dfline.replace(oldstring, table + '.TIMECOL = ' + table.replace('1', '2') + '.TIMECOL')
        dfline = dfline.replace('testcase049_1_df1',dfname)
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
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\ct49dfs.atl',dfline)
