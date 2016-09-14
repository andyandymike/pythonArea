__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *
import subprocess

i = 1
jobname = 'testper' + str(i)
ps = subprocess.Popen('al_engine -NHANA -SHANA -UANDY1 -PPassword1 -s' + jobname, shell=True)
