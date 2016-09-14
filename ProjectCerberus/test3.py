__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

#FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\t221wfs.atl')
#if FileStatus is True:
#    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\t221wfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\t411wf.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase041_1_wf' + str(i) + '.out'
    dfname = 'testcase041_1_df' + str(i)
    wfname = 'testcase041_1_wf' + str(i)
    dstgt = 'hana_partition01'
    guid1 = 'dc35b9bd-3d55-444c-912e-576656f8c362'
    guid1new = 'dc35b9bd-3d55-444c-912e-576656f8c' + str(j)
    guid2 = 'fcc101dc-657f-49ea-89ac-4f38cecae214'
    guid2new = 'fcc101dc-657f-49ea-89ac-4f38cecae' + str(j)
    guid3 = '099609b3-68d6-4e8b-b98a-ddbb61766214'
    guid3new = '099609b3-68d6-4e8b-b98a-ddbb61766' + str(j)
    guid4 = 'd222fb3e-5951-406c-a7bc-d13c0cf1122a'
    guid4new = 'd222fb3e-5951-406c-a7bc-d13c0cf11' + str(j)

    guid5 = 'aa3b92b3-c546-4380-91f8-425774ed89e8'
    guid5new = 'aa3b92b3-c546-4380-91f8-425774ed8' + str(j)
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
        dfline = dfline.replace('testcase041_1_wf1',wfname)
        dfline = dfline.replace('out.out',outname)
        dfline = dfline.replace('RANGE_INT_NP_1',table)
        oldstring1 = table + '.INTCOL is not null'
        oldstring2 = table + '.INTCOL IS NOT  NULL'
        if table.upper().find('_INT') != -1:
            dfline = dfline.replace(oldstring1, table + '.INTCOL is not null')
            define = dfline.replace(oldstring2, table + '.INTCOL IS NOT  NULL')
        if table.upper().find('_TINYINT') != -1:
            dfline = dfline.replace(oldstring1, table + '.TINYINTCOL is not null')
            define = dfline.replace(oldstring2, table + '.TINYINTCOL IS NOT  NULL')
        if table.upper().find('_SMALLINT') != -1:
            dfline = dfline.replace(oldstring1, table + '.SMALLINTCOL is not null')
            define = dfline.replace(oldstring2, table + '.SMALLINTCOL IS NOT  NULL')
        if table.upper().find('_BIGINT') != -1:
            dfline = dfline.replace(oldstring1, table + '.BIGINTCOL is not null')
            define = dfline.replace(oldstring2, table + '.BIGINTCOL IS NOT  NULL')
        if table.upper().find('_DATE') != -1:
            dfline = dfline.replace(oldstring1, table + '.DATECOL is not null')
            define = dfline.replace(oldstring2, table + '.DATECOL IS NOT  NULL')
        if table.upper().find('_SECONDDATE') != -1:
            dfline = dfline.replace(oldstring1, table + '.SECONDDATECOL is not null')
            define = dfline.replace(oldstring2, table + '.SECONDDATECOL IS NOT  NULL')
        if table.upper().find('_TIMESTAMP') != -1:
            dfline = dfline.replace(oldstring1, table + '.TIMESTAMPCOL is not null')
            define = dfline.replace(oldstring2, table + '.TIMESTAMPCOL IS NOT  NULL')
        if table.upper().find('_VARHCAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.VARCHARCOL is not null')
            define = dfline.replace(oldstring2, table + '.VARCHARCOL IS NOT  NULL')
        if table.upper().find('_NVARHCAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.NVARCHARCOL is not null')
            define = dfline.replace(oldstring2, table + '.NVARCHARCOL IS NOT  NULL')
        if table.upper().find('_VARCHAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.VARCHARCOL is not null')
            define = dfline.replace(oldstring2, table + '.VARCHARCOL IS NOT  NULL')
        if table.upper().find('_NVARCHAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.NVARCHARCOL is not null')
            define = dfline.replace(oldstring2, table + '.NVARCHARCOL IS NOT  NULL')
        if table.upper().find('_DECIMAL') != -1:
            dfline = dfline.replace(oldstring1, table + '.DECIMALCOL is not null')
            define = dfline.replace(oldstring2, table + '.DECIMALCOL IS NOT  NULL')
        if table.upper().find('_SMALLDECIMAL') != -1:
            dfline = dfline.replace(oldstring1, table + '.SMALLDECIMALCOL is not null')
            define = dfline.replace(oldstring2, table + '.SMALLDECIMALCOL IS NOT  NULL')
        if table.upper().find('_REAL') != -1:
            dfline = dfline.replace(oldstring1, table + '.REALCOL is not null')
            define = dfline.replace(oldstring2, table + '.REALCOL IS NOT  NULL')
        if table.upper().find('_DOUBLE') != -1:
            dfline = dfline.replace(oldstring1, table + '.DOUBLECOL is not null')
            define = dfline.replace(oldstring2, table + '.DOUBLECOL IS NOT  NULL')
        if table.upper().find('_ALPHANUM') != -1:
            dfline = dfline.replace(oldstring1, table + '.ALPHANUMCOL is not null')
            define = dfline.replace(oldstring2, table + '.ALPHANUMCOL IS NOT  NULL')
        if table.upper().find('_TIME') != -1:
            dfline = dfline.replace(oldstring1, table + '.TIMECOL is not null')
            define = dfline.replace(oldstring2, table + '.TIMECOL IS NOT  NULL')
        dfline = dfline.replace('testcase041_1_df1',dfname)
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
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\t411wfs.atl',dfline)
