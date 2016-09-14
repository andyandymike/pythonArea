__author__ = 'i067382'

import os
import PorjectFunc
import logging
import msvcrt
from PorjectFunc import *

ProjectPath = os.path.abspath('.')

#Create log folder and log file
FolderStatus = os.path.isdir(ProjectPath + '\\log')
if FolderStatus is False:
    os.mkdir(ProjectPath + '\\log')
LogSuffix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
LogFileName = 'LogInit' + LogSuffix + '.log'
LogFileLoc = ProjectPath + '\\log\\' + LogFileName

#Create instance of logging
logger = logging.getLogger('Log')
logger.setLevel(logging.DEBUG)
#File handler
fh = logging.FileHandler(LogFileLoc)
fh.setLevel(logging.DEBUG)
#Formatter
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmt)
#Add formatter to handler
logger.addHandler(fh)

#Check whether Project is usable
ProjectEnvStatus = CheckEnv(ProjectPath)
if ProjectEnvStatus is False:
    print('Bring another Cerberus summon scroll!')
    logger.error('Bring another Cerberus summon scroll!')
    quit()
InitEnv(ProjectPath)

#No need to detect DS verion while init env
#InstalledDSVersion = CheckDSVersion(ProjectPath)

#According to new design, installed BOE path no longer needed
#BOEDefaultPathList = open(ProjectPath + '\\setup\\boedefaultpath.ini')
#try:
#    BOEDefaultPath = BOEDefaultPathList.readline()
#    BOEDefaultPath = PurifyLine(BOEDefaultPath)
#finally:
#    BOEDefaultPathList.close()
#print('Default installed BOE path is: ' + BOEDefaultPath)
#NeedInput = input('Do you want to input another installed BOE path now? [Y/N]')
#while NeedInput.upper() != 'N' and NeedInput.upper() != 'No' and NeedInput.upper() != 'Y' and NeedInput.upper() != 'YES':
#    NeedInput = input('Do you want to input another installed BOE path now? [Y/N]')
#if NeedInput.upper() == 'Y' or NeedInput.upper() == 'YES':
#    BOEInstallPath = AskForInput('Please input installed BOE path')
#    InstalledBOEVersion = CheckBOEVerison(ProjectPath, BOEInstallPath)
#    if InstalledBOEVersion != '-1':
#        WriteToFile(ProjectPath + '\\machineinfo\\InputBOEPath.ini', BOEInstallPath)
#else:
#    InstalledBOEVersion = CheckBOEVerison(ProjectPath)

#Generate InstallSteps.ini
GenerateInstallStepsFile(ProjectPath)

#Collect machine information
MachineName = AskForInput('Please input your machine name')
WriteToFile(ProjectPath + '\\machineinfo\\machineinfo.ini', '@MachineName@:=' + MachineName)

MachineDomain = AskForInput('Please input your full machine name with domain suffix')
WriteToFile(ProjectPath + '\\machineinfo\\machineinfo.ini', '@MachineDomain@:=' + MachineDomain)

MachineUser = AskForInput('Please input your user name')
WriteToFile(ProjectPath + '\\machineinfo\\machineinfo.ini', '@MachineUser@:=' + MachineUser)

MachinePassword = AskForInput('Please input your password')
WriteToFile(ProjectPath + '\\machineinfo\\machineinfo.ini', '@MachinePassword@:=' + MachinePassword)

#Generate node name for response file
NodeName = MachineName
NodeName = GenerateNodeName(NodeName, ProjectPath + '\\setup\\Cerberus\\NodeNameReplaceCode.ini')
WriteToFile(ProjectPath + '\\machineinfo\\machineinfo.ini', '@NodeName@:=' + NodeName)

#Write parameter to response parameter file
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@nodename@:=' + NodeName)
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@machinename@:=' + MachineName.upper())
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@userdomain@:=' + MachineDomain)
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@user@:=' + MachineUser)
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@machinepassword@:=' + MachinePassword)

WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@cmspassword@:=Bobobo')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@cmsport@:=6400')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@dsproductkey@:=')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@boeproductkey@:=')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@cmsusername@:=Administrator')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@clusterkey@:=Bobobo')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@sqlanywhereadminpassword@:=Password1')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@lcmpassword@:=Bobobo')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@lcmport@:=3690')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@siaport@:=6410')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@sqlanywhereadminpassword@:=Password1')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@sqlanywhereport@:=2638')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@tomcatconnectionport@:=8080')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@tomcatredirectport@:=8443')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@tomcatshutdownport@:=8005')
WriteToFile(ProjectPath + '\\installinfo\\installinfo.ini', '@wacsport@:=6405')

print('Modify '+ ProjectPath + '\\installinfo\\installinfo.ini' + ' to specify the installation parameters')
logger.info('Modify '+ ProjectPath + '\\installinfo\\installinfo.ini' + ' to specify the installation parameters')
print('Modify '+ ProjectPath + '\\InstallSteps.ini' + ' to specify the installation steps')
logger.info('Modify '+ ProjectPath + '\\InstallSteps.ini' + ' to specify the installation steps')
print('Launch '+ ProjectPath + '\\start.py' + ' to execute the installation steps')
logger.info('Launch '+ ProjectPath + '\\start.py' + ' to execute the installation steps')

print('Press any key to exit')
print(ord(msvcrt.getch()))
