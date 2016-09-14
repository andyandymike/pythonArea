__author__ = 'I067382'

import subprocess

for i in range (1, 100 + 1):
    jobname = 'testper' + str(i)
    ps = subprocess.Popen('al_engine -NHANA -SHANA -UANDY1 -PPassword1 -s' + jobname, shell=True)
