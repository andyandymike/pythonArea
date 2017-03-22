import os


target = 'C:\\Users\\i067382\\Documents\\DS\\cassandra\\temp.txt'
if os.path.isfile(target):
    os.remove(target)
targetFile = open('C:\\Users\\i067382\\Documents\\DS\\cassandra\\temp.txt', 'a', encoding='utf-8')

for i in range(1, 37):
    if i < 10:
        targetFile.write('!testcase tcase'+str(i)+' odbc00'+str(i)+'.atl\n')
        targetFile.write('!sh eim_launcher.sh odbc00' + str(i) + '\n')
    else:
        targetFile.write('!testcase tcase' + str(i) + ' odbc0' + str(i) + '.atl\n')
        targetFile.write('!sh eim_launcher.sh odbc0' + str(i) + '\n')
    targetFile.write('!expect no *Failed*\n')
    if i < 10:
        targetFile.write('!sh adiff ${runtest}/goldlog/odbc00'+str(i)+'.out ${runtest}/work/odbc00'+str(i)+'.out\n')
    else:
        targetFile.write('!sh adiff ${runtest}/goldlog/odbc0' + str(i) + '.out ${runtest}/work/odbc0' + str(i) + '.out\n')
    targetFile.write('!endtestcase\n')
    targetFile.write('\n')