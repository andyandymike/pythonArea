__author__ = 'I067382'

import os

path = os.path.abspath('.')
file = open(path + '\\PorjectFunc.py', 'r')
file2 = open(path + '\\PorjectFunc_mo.py', 'a')
for line in file:
    file2.write(line)
    if line.find('print(\'Error: ') != -1:
        file2.write(line.replace('print(\'Error: ', 'logger.error(\''))
    if line.find('print(\'Warning: ') != -1:
        file2.write(line.replace('print(\'Warning: ', 'logger.warning(\''))
    if line.find('print') != -1 and line.find('print(\'Error: ') == -1 and line.find('print(\'Warning: ') == -1:
        file2.write(line.replace('print', 'logger.info'))