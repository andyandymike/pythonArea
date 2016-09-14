__author__ = 'I067382'

import os
import shutil

projectPath = os.path.abspath('.')
remotePath = projectPath + '\\remote'
installinfoPath = projectPath + '\\installinfo'
setupPath = projectPath + '\\setup\\Cerberus'

if not os.path.isdir(remotePath):
    print('Error: No remote folder in Cerberus folder, will not start remote deployment!')
    quit()

for remoteFileName in os.listdir(remotePath):
    if remoteFileName == 'installinfo.ini':
        if not os.path.isdir(installinfoPath):
            os.mkdir(installinfoPath)
            shutil.copy(remotePath + '\\' + remoteFileName, installinfoPath)
        else:
            if os.path.isfile(installinfoPath + '\\' + remoteFileName):
                os.remove(installinfoPath + '\\' + remoteFileName)
                shutil.copy(remotePath + '\\' + remoteFileName, installinfoPath)
            else:
                shutil.copy(remotePath + '\\' + remoteFileName, installinfoPath)

    if remoteFileName == 'Setup.ini':
        if not os.path.isdir(setupPath):
            print('Error: No setup folder in Cerberus folder, resummon again!')
            quit()
        else:
            if os.path.isfile(setupPath + '\\' + remoteFileName):
                os.remove(setupPath + '\\' + remoteFileName)
                shutil.copy(remotePath + '\\' + remoteFileName, setupPath)
            else:
                print('Warning: No setup.ini file in your \\setup\\Cerberus folder!')
                shutil.copy(remotePath + '\\' + remoteFileName, setupPath)

    if remoteFileName == 'InstallSteps.ini':
        if os.path.isfile(projectPath + '\\' + remoteFileName):
            os.remove(projectPath + '\\' + remoteFileName)
            shutil.copy(remotePath + '\\' + remoteFileName, projectPath)
        else:
            shutil.copy(remotePath + '\\' + remoteFileName, projectPath)

startFile = projectPath + '\\start.py'
command = startFile
os.system(command)