__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\ct45dfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\ct45dfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\ct45df.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase045_1_wf' + str(i) + '.out'
    dfname = 'testcase045_1_df' + str(i)
    wfname = 'testcase045_1_wf' + str(i)
    dstgt = 'hana_partition02'
    guid1 = '046a9d80-e90b-4bb1-9ca0-496148643a3e'
    guid1new = '046a9d80-e90b-4bb1-9ca0-496148643' + str(j)
    guid2 = '7d8375dd-878f-40ed-9e99-357f55cd9100'
    guid2new = '7d8375dd-878f-40ed-9e99-357f55cd9' + str(j)
    guid3 = '199db901-26c6-4b4a-8c5c-1d74dbaf7100'
    guid3new = '199db901-26c6-4b4a-8c5c-1d74dbaf7' + str(j)
    guid4 = '75ebff96-787e-42f6-b979-ef95e1df4100'
    guid4new = '75ebff96-787e-42f6-b979-ef95e1df4' + str(j)

    guid5 = '299d5a5c-40c5-499f-b419-bf2a2bca1100'
    guid5new = '299d5a5c-40c5-499f-b419-bf2a2bca1' + str(j)
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
        dfline = dfline.replace('testcase045_1_wf1',wfname)
        dfline = dfline.replace('out.out',outname)
        dfline = dfline.replace('RANGE_INT_NP_1',table)
        #dfline = dfline.replace('RANGE_INT_NP_2',table.replace('1', '2'))
        oldstring = table + '.ID = NO_PARTITION_TABLE_1.ID'
        if table.upper().find('_INT') != -1:
            dfline = dfline.replace(oldstring, table + '.INTCOL = NO_PARTITION_TABLE_1.INTCOL')
        if table.upper().find('_TINYINT') != -1:
            dfline = dfline.replace(oldstring, table + '.TINYINTCOL = NO_PARTITION_TABLE_1.TINYINTCOL')
        if table.upper().find('_SMALLINT') != -1:
            dfline = dfline.replace(oldstring, table + '.SMALLINTCOL = NO_PARTITION_TABLE_1.SMALLINTCOL')
        if table.upper().find('_BIGINT') != -1:
            dfline = dfline.replace(oldstring, table + '.BIGINTCOL = NO_PARTITION_TABLE_1.BIGINTCOL')
        if table.upper().find('_DATE') != -1:
            dfline = dfline.replace(oldstring, table + '.DATECOL = NO_PARTITION_TABLE_1.DATECOL')
        if table.upper().find('_SECONDDATE') != -1:
            dfline = dfline.replace(oldstring, table + '.SECONDDATECOL = NO_PARTITION_TABLE_1.SECONDDATECOL')
        if table.upper().find('_TIMESTAMP') != -1:
            dfline = dfline.replace(oldstring, table + '.TIMESTAMPCOL = NO_PARTITION_TABLE_1.TIMESTAMPCOL')
        if table.upper().find('_VARHCAR') != -1:
            dfline = dfline.replace(oldstring, table + '.VARCHARCOL = NO_PARTITION_TABLE_1.VARCHARCOL')
        if table.upper().find('_NVARHCAR') != -1:
            dfline = dfline.replace(oldstring, table + '.NVARCHARCOL = NO_PARTITION_TABLE_1.NVARCHARCOL')
        if table.upper().find('_VARCHAR') != -1:
            dfline = dfline.replace(oldstring, table + '.VARCHARCOL = NO_PARTITION_TABLE_1.VARCHARCOL')
        if table.upper().find('_NVARCHAR') != -1:
            dfline = dfline.replace(oldstring, table + '.NVARCHARCOL = NO_PARTITION_TABLE_1.NVARCHARCOL')
        if table.upper().find('_DECIMAL') != -1:
            dfline = dfline.replace(oldstring, table + '.DECIMALCOL = NO_PARTITION_TABLE_1.DECIMALCOL')
        if table.upper().find('_SMALLDECIMAL') != -1:
            dfline = dfline.replace(oldstring, table + '.SMALLDECIMALCOL = NO_PARTITION_TABLE_1.SMALLDECIMALCOL')
        if table.upper().find('_REAL') != -1:
            dfline = dfline.replace(oldstring, table + '.REALCOL = NO_PARTITION_TABLE_1.REALCOL')
        if table.upper().find('_DOUBLE') != -1:
            dfline = dfline.replace(oldstring, table + '.DOUBLECOL = NO_PARTITION_TABLE_1.DOUBLECOL')
        if table.upper().find('_ALPHANUM') != -1:
            dfline = dfline.replace(oldstring, table + '.ALPHANUMCOL = NO_PARTITION_TABLE_1.ALPHANUMCOL')
        if table.upper().find('_TIME') != -1:
            dfline = dfline.replace(oldstring, table + '.TIMECOL = NO_PARTITION_TABLE_1.TIMECOL')
        dfline = dfline.replace('testcase045_1_df1',dfname)
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
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\ct45dfs.atl',dfline)
