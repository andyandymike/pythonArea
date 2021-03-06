__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *

FileStatus = os.path.isfile('C:\\Users\\i067382\\Desktop\\New folder\\ct47dfs.atl')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Desktop\\New folder\\ct47dfs.atl')

df = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\ct47df.atl')

tables = ReadFromFile('C:\\Users\\i067382\\Desktop\\New folder\\tableonly.txt')
i = 1;
j = 100;
for table in tables:
    table = PurifyLine(table)
    outname = 'testcase047_1_wf' + str(i) + '.out'
    dfname = 'testcase047_1_df' + str(i)
    wfname = 'testcase047_1_wf' + str(i)
    dstgt = 'hana_partition02'
    guid1 = '3bbdc1d6-99c5-4134-8e4f-d80731341544'
    guid1new = '3bbdc1d6-99c5-4134-8e4f-d80731341' + str(j)
    guid2 = 'a6707549-5cf7-4553-9fb3-b24bce65d100'
    guid2new = 'a6707549-5cf7-4553-9fb3-b24bce65d' + str(j)
    guid3 = '40c35486-34c9-4768-b830-e9ecb912e100'
    guid3new = '40c35486-34c9-4768-b830-e9ecb912e' + str(j)
    guid4 = 'c2220ce1-5020-4375-8390-edf402417100'
    guid4new = 'c2220ce1-5020-4375-8390-edf402417' + str(j)

    guid5 = 'db21cf41-d6f0-4ecd-9ef2-d94f0eff07b7'
    guid5new = 'db21cf41-d6f0-4ecd-9ef2-d94f0eff0' + str(j)
    guid6 = '138e94f5-e737-4355-9d96-90642cffeb72'
    guid6new = '138e94f5-e737-4355-9d96-90642cffe' + str(j)
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
        dfline = dfline.replace('testcase047_1_wf1',wfname)
        dfline = dfline.replace('out.out',outname)
        dfline = dfline.replace('RANGE_INT_NP_1',table)
        dfline = dfline.replace('RANGE_INT_NP_2',table.replace('1', '2'))
        dfline = dfline.replace('RANGE_INT_NP_3',table.replace('1', '3'))
        oldstring1 = table + '.ID = ' + table.replace('1', '2') + '.ID'
        oldstring2 = table + '.ID = ' + table.replace('1', '3') + '.ID'
        if table.upper().find('_INT') != -1:
            dfline = dfline.replace(oldstring1, table + '.INTCOL = ' + table.replace('1', '2') + '.INTCOL')
            dfline = dfline.replace(oldstring2, table + '.INTCOL = ' + table.replace('1', '3') + '.INTCOL')
        if table.upper().find('_TINYINT') != -1:
            dfline = dfline.replace(oldstring1, table + '.TINYINTCOL = ' + table.replace('1', '2') + '.TINYINTCOL')
            dfline = dfline.replace(oldstring2, table + '.TINYINTCOL = ' + table.replace('1', '3') + '.TINYINTCOL')
        if table.upper().find('_SMALLINT') != -1:
            dfline = dfline.replace(oldstring1, table + '.SMALLINTCOL = ' + table.replace('1', '2') + '.SMALLINTCOL')
            dfline = dfline.replace(oldstring2, table + '.SMALLINTCOL = ' + table.replace('1', '3') + '.SMALLINTCOL')
        if table.upper().find('_BIGINT') != -1:
            dfline = dfline.replace(oldstring1, table + '.BIGINTCOL = ' + table.replace('1', '2') + '.BIGINTCOL')
            dfline = dfline.replace(oldstring2, table + '.BIGINTCOL = ' + table.replace('1', '3') + '.BIGINTCOL')
        if table.upper().find('_DATE') != -1:
            dfline = dfline.replace(oldstring1, table + '.DATECOL = ' + table.replace('1', '2') + '.DATECOL')
            dfline = dfline.replace(oldstring2, table + '.DATECOL = ' + table.replace('1', '3') + '.DATECOL')
        if table.upper().find('_SECONDDATE') != -1:
            dfline = dfline.replace(oldstring1, table + '.SECONDDATECOL = ' + table.replace('1', '2') + '.SECONDDATECOL')
            dfline = dfline.replace(oldstring2, table + '.SECONDDATECOL = ' + table.replace('1', '3') + '.SECONDDATECOL')
        if table.upper().find('_TIMESTAMP') != -1:
            dfline = dfline.replace(oldstring1, table + '.TIMESTAMPCOL = ' + table.replace('1', '2') + '.TIMESTAMPCOL')
            dfline = dfline.replace(oldstring2, table + '.TIMESTAMPCOL = ' + table.replace('1', '3') + '.TIMESTAMPCOL')
        if table.upper().find('_VARHCAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.VARCHARCOL = ' + table.replace('1', '2') + '.VARCHARCOL')
            dfline = dfline.replace(oldstring2, table + '.VARCHARCOL = ' + table.replace('1', '3') + '.VARCHARCOL')
        if table.upper().find('_NVARHCAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.NVARCHARCOL = ' + table.replace('1', '2') + '.NVARCHARCOL')
            dfline = dfline.replace(oldstring2, table + '.NVARCHARCOL = ' + table.replace('1', '3') + '.NVARCHARCOL')
        if table.upper().find('_VARCHAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.VARCHARCOL = ' + table.replace('1', '2') + '.VARCHARCOL')
            dfline = dfline.replace(oldstring2, table + '.VARCHARCOL = ' + table.replace('1', '3') + '.VARCHARCOL')
        if table.upper().find('_NVARCHAR') != -1:
            dfline = dfline.replace(oldstring1, table + '.NVARCHARCOL = ' + table.replace('1', '2') + '.NVARCHARCOL')
            dfline = dfline.replace(oldstring2, table + '.NVARCHARCOL = ' + table.replace('1', '3') + '.NVARCHARCOL')
        if table.upper().find('_DECIMAL') != -1:
            dfline = dfline.replace(oldstring1, table + '.DECIMALCOL = ' + table.replace('1', '2') + '.DECIMALCOL')
            dfline = dfline.replace(oldstring2, table + '.DECIMALCOL = ' + table.replace('1', '3') + '.DECIMALCOL')
        if table.upper().find('_SMALLDECIMAL') != -1:
            dfline = dfline.replace(oldstring1, table + '.SMALLDECIMALCOL = ' + table.replace('1', '2') + '.SMALLDECIMALCOL')
            dfline = dfline.replace(oldstring2, table + '.SMALLDECIMALCOL = ' + table.replace('1', '3') + '.SMALLDECIMALCOL')
        if table.upper().find('_REAL') != -1:
            dfline = dfline.replace(oldstring1, table + '.REALCOL = ' + table.replace('1', '2') + '.REALCOL')
            dfline = dfline.replace(oldstring2, table + '.REALCOL = ' + table.replace('1', '3') + '.REALCOL')
        if table.upper().find('_DOUBLE') != -1:
            dfline = dfline.replace(oldstring1, table + '.DOUBLECOL = ' + table.replace('1', '2') + '.DOUBLECOL')
            dfline = dfline.replace(oldstring2, table + '.DOUBLECOL = ' + table.replace('1', '3') + '.DOUBLECOL')
        if table.upper().find('_ALPHANUM') != -1:
            dfline = dfline.replace(oldstring1, table + '.ALPHANUMCOL = ' + table.replace('1', '2') + '.ALPHANUMCOL')
            dfline = dfline.replace(oldstring2, table + '.ALPHANUMCOL = ' + table.replace('1', '3') + '.ALPHANUMCOL')
        if table.upper().find('_TIME') != -1:
            dfline = dfline.replace(oldstring1, table + '.TIMECOL = ' + table.replace('1', '2') + '.TIMECOL')
            dfline = dfline.replace(oldstring2, table + '.TIMECOL = ' + table.replace('1', '3') + '.TIMECOL')
        dfline = dfline.replace('testcase047_1_df1',dfname)
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
        WriteToFile('C:\\Users\\i067382\\Desktop\\New folder\\ct47dfs.atl',dfline)
