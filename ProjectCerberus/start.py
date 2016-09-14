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
LogFileName = 'LogStart' + LogSuffix + '.log'
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
    print('Cerberus is broken!')
    logger.error('Cerberus is broken!')
    quit()

#According to new design, installed BOE path no longer needed
#BOEInstallPath = ''
#FileStatus = os.path.isfile(ProjectPath + '\\machineinfo\\InputBOEPath.ini')
#if FileStatus is True:
#    BOEInstallPath = ReadFromFile(ProjectPath + '\\machineinfo\\InputBOEPath.ini', 1)
#    InstalledBOEVersion = CheckBOEVerison(ProjectPath, BOEInstallPath)
#    if InstalledBOEVersion == '-1':
#        InstalledBOEVersion = CheckBOEVerison(ProjectPath)
#else:
#    InstalledBOEVersion = CheckBOEVerison(ProjectPath)

#Print machine deployment status
PrintMachineInstallationStatus(ProjectPath)
print('')

#Get all steps from setup file
AllSteps = GetSteps(ProjectPath)
if AllSteps is False:
    print('Error: Error happened when get all installation steps, Cerberus will exit')
    logger.error('Error happened when get all installation steps, Cerberus will exit')
    quit()
#Delete duplicate steps
AllSteps = SimplifySteps(AllSteps)
if AllSteps is False:
    print('Error: Error happened when get simplified all installation steps, Cerberus will exit')
    logger.error('Error happened when get simplified all installation steps, Cerberus will exit')
    quit()
print('')

AllStepCount = 0
while AllStepCount < len(AllSteps):
    #Get installed DS version
    InstalledDSVersion = CheckDSVersion(ProjectPath, 1)
    if InstalledDSVersion is False:
        print('Error: Error happened when get installed DS version, Cerberus will exit')
        logger('Error happened when get installed DS version, Cerberus will exit')
        quit()
    #Get installed BOE version
    InstalledBOEVersion = CheckBOEVerison(ProjectPath, 1)
    if InstalledBOEVersion is False:
        print('Error: Error happened when get installed BOE version, Cerberus will exit')
        logger('Error happened when get installed BOE version, Cerberus will exit')
        quit()
    #Get installed BOE type
    InstalledBOEType = CheckBOEType(ProjectPath, 1)
    if InstalledBOEType is False:
        print('Error: Error happened when get install BOE type, Cerberus will exit')
        logger.error('Error happened when get install BOE type, Cerberus will exit')
        quit()
    print('Now Cerberus is processing your Step: ' + AllSteps[AllStepCount][0])
    logger.info('Now Cerberus is processing your Step: ' + AllSteps[AllStepCount][0])
    #Interprete step to correct steps
    CorrectStep = GetCorrectStep(ProjectPath, AllSteps[AllStepCount], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
    if CorrectStep is False:
        print('Error: Error happened when getting correct step, Cerberus will exit')
        logger.error('Error happened when getting correct step, Cerberus will exit')
        quit()
    StepCount = 0
    print('According to your setup and machine env, Step: ' + AllSteps[AllStepCount][0] + ' is interpreted to:')
    logger.info('According to your setup and machine env, Step: ' + AllSteps[AllStepCount][0] + ' is interpreted to:')
    print(CorrectStep)
    logger.info(CorrectStep)
    while StepCount < len(CorrectStep):
        StepName = CorrectStep[StepCount][0]
        print('Now Cerberus is processing interpreted Correct Step: ' + StepName)
        logger.info('Now Cerberus is processing interpreted Correct Step: ' + StepName)
        #Generate response file for correct step
        ResponseFile = GetResponseFile(ProjectPath, StepName)
        if ResponseFile is False:
            print('Error: Error happened when get response file, Cerberus will exit')
            logger.error('Error happened when get response file, Cerberus will exit')
            quit()
        #Execute correct step
        if ExecuteStep(ProjectPath, CorrectStep[StepCount], ResponseFile) is False:
            print('Error: Error happened when execute Step: ' + CorrectStep[StepCount] + ', Cerberus will exit')
            logger.error('Error happened when execute Step: ' + CorrectStep[StepCount] + ', Cerberus will exit')
            quit()
        #Check step success or not
        if CheckStepStatus(ProjectPath, CorrectStep[StepCount]) is False:
            print('Error: Step: ' + StepName + ' doesn\'t successfully executed, Cerberus will exit')
            logger.error('Step: ' + StepName + ' doesn\'t successfully executed, Cerberus will exit')
            quit()
        StepCount = StepCount + 1
    print('')
    AllStepCount = AllStepCount + 1

#Print machine deployment status
PrintMachineInstallationStatus(ProjectPath)
print('Cerberus has finished your installation steps. Have a nice day!')
logger.info('Cerberus has finished your installation steps. Have a nice day!')

print('Press any key to exit')
print(ord(msvcrt.getch()))