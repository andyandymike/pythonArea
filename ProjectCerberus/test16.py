__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\ct51dfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\ct51dfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\ct51df.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase051_1_wf' + str(i) + '.out'
    dfname = 'testcase051_1_df' + str(i)
    wfname = 'testcase051_1_wf' + str(i)
    dstgt = 'hana_partition02'
    guid1 = '6c97dc9e-205b-422b-b1c9-871c5a084333'
    guid1new = '6c97dc9e-205b-422b-b1c9-871c5a084' + str(j)
    guid2 = '332201c3-02ef-4182-8894-2d491ab95100'
    guid2new = '332201c3-02ef-4182-8894-2d491ab95' + str(j)
    guid3 = '448dccc6-1ba9-4385-bebd-609f59fa0100'
    guid3new = '448dccc6-1ba9-4385-bebd-609f59fa0' + str(j)
    guid4 = 'c7bb850a-4fe4-4766-b665-fbbc1478a100'
    guid4new = 'c7bb850a-4fe4-4766-b665-fbbc1478a' + str(j)

    guid5 = '09f7e57d-f60b-4abf-bf40-2cb18accdc87'
    guid5new = '09f7e57d-f60b-4abf-bf40-2cb18accd' + str(j)
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
        dfline = dfline.replace('testcase051_1_wf1',wfname)
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
        dfline = dfline.replace('testcase051_1_df1',dfname)
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
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\ct51dfs.atl',dfline)
