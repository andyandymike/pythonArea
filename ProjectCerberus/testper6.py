__author__ = 'I067382'

import subprocess

for i in range (1, 100 + 1):
    jobname = 'testper' + str(i)
    ps = subprocess.Popen(jobname + '.bat', shell=True)