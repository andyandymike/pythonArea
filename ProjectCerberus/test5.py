__author__ = 'I067382'

import PorjectFunc
from PorjectFunc import *
from os import *
from shutil import *

goldlogs = listdir('Z:\\landy\\tmp\\partition_pre')
workfiles = listdir('Z:\\landy\\tmp\\partition_unix-aix')

workoutfolder = 'C:\\Users\\i067382\\Desktop\\New folder\\work\\'
goldlogoutfolder = 'C:\\Users\\i067382\\Desktop\\New folder\\goldlog\\'

goldlogfolder = 'Z:\\landy\\tmp\\partition_pre\\'
workfilefolder = 'Z:\\landy\\tmp\\partition_unix-aix\\'

for workfile in workfiles:
    workfilecontent = ReadFromFile(workfilefolder + workfile)
    goldlogcontent = ReadFromFile(goldlogfolder + workfile)
    same = True
    print('now working on ' + workfilefolder + workfile)
    for workfileline in workfilecontent:
        if workfileline not in goldlogcontent:
            same = False
    for goldlogline in goldlogcontent:
        if goldlogline not in workfilecontent:
            same = False
    if same is False:
        copy(workfilefolder + workfile, workoutfolder + workfile)
        copy(goldlogfolder + workfile, goldlogoutfolder + workfile)