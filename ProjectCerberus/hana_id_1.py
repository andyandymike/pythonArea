__author__ = 'I067382'

from PorjectFunc import *


FileStatus = os.path.isfile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase')
if FileStatus is True:
    os.remove('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase')

jobs = ReadFromFile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\jobs.txt')

for job in jobs:
    job = PurifyLine(job)
    WriteToFile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase','!testcase ' + job + ' ' + job + '.atl')
    WriteToFile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase','!sh eim_launcher.sh ' + job)
    WriteToFile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase','!expect no *Failed*')
    WriteToFile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase','!endtestcase')
    WriteToFile('C:\\Users\\i067382\\Documents\\DS\\HANA identity coulmn\\testcase',' ')
