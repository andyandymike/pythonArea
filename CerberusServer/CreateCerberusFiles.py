__author__ = 'I067382'

import os
import json
import logging
import time

rootPath = os.path.abspath('.')
inputFolder = '\\CerberusInput'
outputFolder = '\\CerberusOutput'
setupFolder='\\Cerberus'


#Create log folder and log file
folderStatus = os.path.isdir(rootPath + '\\log')
if folderStatus is False:
    os.mkdir(rootPath + '\\log')
logSuffix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
logFileName = 'LogCreateCerberusFiles' + logSuffix + '.log'
logFileLoc = rootPath + '\\log\\' + logFileName
#Create instance of logging
logger = logging.getLogger('Log')
logger.setLevel(logging.DEBUG)
#File handler
fh = logging.FileHandler(logFileLoc)
fh.setLevel(logging.DEBUG)
#Formatter
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmt)
#Add formatter to handler
logger.addHandler(fh)


def WriteToFile(outputFile, outputLine, deleteBeforeWrite = False):
    if deleteBeforeWrite is True:
        fileStatus = os.path.isfile(outputFile)
        if fileStatus is True:
            os.remove(outputFile)
    file = open(outputFile, 'a')
    try:
        file.write(outputLine + '\n')
    finally:
        file.close()


def PurifyLine(line, extraPurifyCode = ''):
    if not line:
        return line
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    line = line.replace('\t', '')
    line = line.lstrip()
    line = line.rstrip()
    if extraPurifyCode != '':
        line = line.replace(extraPurifyCode, '')
    return line


def GenerateNodeName(nodeName, replaceCodeListFile, extraReplaceCode = ''):
    replaceCodeListFile = open(replaceCodeListFile, 'r')
    try:
        replaceCode = replaceCodeListFile.readline()
        while replaceCode:
            replaceCode = PurifyLine(replaceCode)
            replaceCode = PurifyLine(replaceCode, ' ')
            nodeName = nodeName.replace(replaceCode, '_')
            replaceCode = replaceCodeListFile.readline()
    finally:
        replaceCodeListFile.close()
    if extraReplaceCode != '':
        nodeName = nodeName.replace(extraReplaceCode, '_')
    return nodeName.upper()


def CreateInstallInfoFileFromJson(inputFile, outputPath, setupPath):
    inputFile = open(inputFile, 'r')
    templateFile = open(setupPath + '\\installinfo.json', 'r')
    try:
        inputFileJsonObject = json.loads(inputFile.read())
        templateFileJsonObject = json.loads(templateFile.read())
        for responseParameter in inputFileJsonObject['responseparameter']:
            outputFolder = outputPath + '\\' + responseParameter['machinename']
            if not os.path.isdir(outputFolder):
                os.mkdir(outputFolder)
            outputFile = outputFolder + '\\installinfo.ini'
            WriteToFile(outputFile, '@machinename@:=' + responseParameter['machinename'].upper(), True)
            WriteToFile(outputFile, '@userdomain@:=' + responseParameter['userdomain'])
            WriteToFile(outputFile, '@user@:=' + responseParameter['user'])
            WriteToFile(outputFile, '@machinepassword@:=' + responseParameter['machinepassword'])

            nodeName = GenerateNodeName(responseParameter['machinename'].upper(), setupPath + '\\NodeNameReplaceCode.ini')
            WriteToFile(outputFile, '@nodename@:=' + nodeName)

            if responseParameter.has_key('cmspassword'):
                WriteToFile(outputFile, '@cmspassword@:=' + responseParameter['cmspassword'])
            else:
                WriteToFile(outputFile, '@cmspassword@:=' + templateFileJsonObject['cmspassword'])
            if responseParameter.has_key('cmsport'):
                WriteToFile(outputFile, '@cmsport@:=' + responseParameter['cmsport'])
            else:
                WriteToFile(outputFile, '@cmsport@:=' + templateFileJsonObject['cmsport'])
            if responseParameter.has_key('dsproductkey'):
                WriteToFile(outputFile, '@dsproductkey@:=' + responseParameter['dsproductkey'])
            else:
                WriteToFile(outputFile, '@dsproductkey@:=' + templateFileJsonObject['dsproductkey'])
            if responseParameter.has_key('boeproductkey'):
                WriteToFile(outputFile, '@boeproductkey@:=' + responseParameter['boeproductkey'])
            else:
                WriteToFile(outputFile, '@boeproductkey@:=' + templateFileJsonObject['boeproductkey'])
            if responseParameter.has_key('cmsusername'):
                WriteToFile(outputFile, '@cmsusername@:=' + responseParameter['cmsusername'])
            else:
                WriteToFile(outputFile, '@cmsusername@:=' + templateFileJsonObject['cmsusername'])
            if responseParameter.has_key('clusterkey'):
                WriteToFile(outputFile, '@clusterkey@:=' + responseParameter['clusterkey'])
            else:
                WriteToFile(outputFile, '@clusterkey@:=' + templateFileJsonObject['clusterkey'])
            if responseParameter.has_key('lcmpassword'):
                WriteToFile(outputFile, '@lcmpassword@:=' + responseParameter['lcmpassword'])
            else:
                WriteToFile(outputFile, '@lcmpassword@:=' + templateFileJsonObject['lcmpassword'])
            if responseParameter.has_key('lcmport'):
                WriteToFile(outputFile, '@lcmport@:=' + responseParameter['lcmport'])
            else:
                WriteToFile(outputFile, '@lcmport@:=' + templateFileJsonObject['lcmport'])
            if responseParameter.has_key('siaport'):
                WriteToFile(outputFile, '@siaport@:=' + responseParameter['siaport'])
            else:
                WriteToFile(outputFile, '@siaport@:=' + templateFileJsonObject['siaport'])
            if responseParameter.has_key('sqlanywhereadminpassword'):
                WriteToFile(outputFile, '@sqlanywhereadminpassword@:=' + responseParameter['sqlanywhereadminpassword'])
            else:
                WriteToFile(outputFile, '@sqlanywhereadminpassword@:=' + templateFileJsonObject['sqlanywhereadminpassword'])
            if responseParameter.has_key('sqlanywhereport'):
                WriteToFile(outputFile, '@sqlanywhereport@:=' + responseParameter['sqlanywhereport'])
            else:
                WriteToFile(outputFile, '@sqlanywhereport@:=' + templateFileJsonObject['sqlanywhereport'])
            if responseParameter.has_key('tomcatconnectionport'):
                WriteToFile(outputFile, '@tomcatconnectionport@:=' + responseParameter['tomcatconnectionport'])
            else:
                WriteToFile(outputFile, '@tomcatconnectionport@:=' + templateFileJsonObject['tomcatconnectionport'])
            if responseParameter.has_key('tomcatredirectport'):
                WriteToFile(outputFile, '@tomcatredirectport@:=' + responseParameter['tomcatredirectport'])
            else:
                WriteToFile(outputFile, '@tomcatredirectport@:=' + templateFileJsonObject['tomcatredirectport'])
            if responseParameter.has_key('tomcatshutdownport'):
                WriteToFile(outputFile, '@tomcatshutdownport@:=' + responseParameter['tomcatshutdownport'])
            else:
                WriteToFile(outputFile, '@tomcatshutdownport@:=' + templateFileJsonObject['tomcatshutdownport'])
            if responseParameter.has_key('wacsport'):
                WriteToFile(outputFile, '@wacsport@:=' + responseParameter['wacsport'])
            else:
                WriteToFile(outputFile, '@wacsport@:=' + templateFileJsonObject['wacsport'])
    except Exception,e:
        logger.error('Catched Error: ' + str(Exception) + ' : ' + str(e))
    finally:
        inputFile.close()
        templateFile.close()


def CreateSetupFileFromJson(inputFile, outputPath):
    inputFile = open(inputFile, 'r')
    templateFile = open(setupPath + '\\Setup.json', 'r')
    try:
        inputFileJsonObject = json.loads(inputFile.read())
        templateFileJsonObject = json.loads(templateFile.read())
        for cerberusSetup in inputFileJsonObject['cerberussetup']:
            outputFolder = outputPath + '\\' + cerberusSetup['machinename']
            if not os.path.isdir(outputFolder):
                os.mkdir(outputFolder)
            outputFile = outputFolder + '\\Setup.ini'
            if os.path.isfile(outputFile):
                os.remove(outputFile)
            if cerberusSetup.has_key('dsinstallforceinstall'):
                WriteToFile(outputFile, 'DSInstallForceInstall=' + cerberusSetup['dsinstallforceinstall'])
            else:
                WriteToFile(outputFile, 'DSInstallForceInstall=' + templateFileJsonObject['dsinstallforceinstall'])
            if cerberusSetup.has_key('minibipinstallforceinstall'):
                WriteToFile(outputFile, 'MiniBIPInstallForceInstall=' + cerberusSetup['minibipinstallforceinstall'])
            else:
                WriteToFile(outputFile, 'MiniBIPInstallForceInstall=' + templateFileJsonObject['MiniBIPInstallForceInstall'])
            if cerberusSetup.has_key('fullboeinstallforceinstall'):
                WriteToFile(outputFile, 'FullBOEInstallForceInstall=' + cerberusSetup['fullboeinstallforceinstall'])
            else:
                WriteToFile(outputFile, 'FullBOEInstallForceInstall=' + templateFileJsonObject['FullBOEInstallForceInstall'])
            if cerberusSetup.has_key('boeinstallforceinstall'):
                WriteToFile(outputFile, 'BOEInstallForceInstall=' + cerberusSetup['boeinstallforceinstall'])
            else:
                WriteToFile(outputFile, 'BOEInstallForceInstall=' + templateFileJsonObject['BOEInstallForceInstall'])
            if cerberusSetup.has_key('minibippatchforcepatch'):
                WriteToFile(outputFile, 'MiniBIPPatchForcePatch=' + cerberusSetup['minibippatchforcepatch'])
            else:
                WriteToFile(outputFile, 'MiniBIPPatchForcePatch=' + templateFileJsonObject['MiniBIPPatchForcePatch'])
            if cerberusSetup.has_key('fullboepatchforcepatch'):
                WriteToFile(outputFile, 'FullBOEPatchForcePatch=' + cerberusSetup['fullboepatchforcepatch'])
            else:
                WriteToFile(outputFile, 'FullBOEPatchForcePatch=' + templateFileJsonObject['FullBOEPatchForcePatch'])
            if cerberusSetup.has_key('boepatchforcepatch'):
                WriteToFile(outputFile, 'BOEPatchForcePatch=' + cerberusSetup['boepatchforcepatch'])
            else:
                WriteToFile(outputFile, 'BOEPatchForcePatch=' + templateFileJsonObject['BOEPatchForcePatch'])
            if cerberusSetup.has_key('dsupgradeforceinstall'):
                WriteToFile(outputFile, 'DSUpgradeForceInstall=' + cerberusSetup['dsupgradeforceinstall'])
            else:
                WriteToFile(outputFile, 'DSUpgradeForceInstall=' + templateFileJsonObject['DSUpgradeForceInstall'])
            if cerberusSetup.has_key('dsupgradeforceupgrade'):
                WriteToFile(outputFile, 'DSUpgradeForceUpgrade=' + cerberusSetup['dsupgradeforceupgrade'])
            else:
                WriteToFile(outputFile, 'DSUpgradeForceUpgrade=' + templateFileJsonObject['DSUpgradeForceUpgrade'])
            if cerberusSetup.has_key('installfullboe'):
                WriteToFile(outputFile, 'InstallFullBOE=' + cerberusSetup['installfullboe'])
            else:
                WriteToFile(outputFile, 'InstallFullBOE=' + templateFileJsonObject['InstallFullBOE'])
            if cerberusSetup.has_key('installminibip'):
                WriteToFile(outputFile, 'InstallMiniBIP=' + cerberusSetup['installminibip'])
            else:
                WriteToFile(outputFile, 'InstallMiniBIP=' + templateFileJsonObject['InstallMiniBIP'])
            if cerberusSetup.has_key('patchfullboe'):
                WriteToFile(outputFile, 'PatchFullBOE=' + cerberusSetup['patchfullboe'])
            else:
                WriteToFile(outputFile, 'PatchFullBOE=' + templateFileJsonObject['PatchFullBOE'])
            if cerberusSetup.has_key('patchminibip'):
                WriteToFile(outputFile, 'PatchMINIBIP=' + cerberusSetup['patchminibip'])
            else:
                WriteToFile(outputFile, 'PatchMINIBIP=' + templateFileJsonObject['PatchMINIBIP'])
            if cerberusSetup.has_key('removefullboepackage'):
                WriteToFile(outputFile, 'RemoveFullBOEPackage=' + cerberusSetup['removefullboepackage'])
            else:
                WriteToFile(outputFile, 'RemoveFullBOEPackage=' + templateFileJsonObject['RemoveFullBOEPackage'])
            if cerberusSetup.has_key('removefullboepatch'):
                WriteToFile(outputFile, 'RemoveFullBOEPatch=' + cerberusSetup['removefullboepatch'])
            else:
                WriteToFile(outputFile, 'RemoveFullBOEPatch=' + templateFileJsonObject['RemoveFullBOEPatch'])
            if cerberusSetup.has_key('removeminibippackage'):
                WriteToFile(outputFile, 'RemoveMINIBIPPackage=' + cerberusSetup['removeminibippackage'])
            else:
                WriteToFile(outputFile, 'RemoveMINIBIPPackage=' + templateFileJsonObject['RemoveMINIBIPPackage'])
            if cerberusSetup.has_key('removeminibippatch'):
                WriteToFile(outputFile, 'RemoveMINIBIPPatch=' + cerberusSetup['removeminibippatch'])
            else:
                WriteToFile(outputFile, 'RemoveMINIBIPPatch=' + templateFileJsonObject['RemoveMINIBIPPatch'])
            if cerberusSetup.has_key('installds'):
                WriteToFile(outputFile, 'InstallDS=' + cerberusSetup['installds'])
            else:
                WriteToFile(outputFile, 'InstallDS=' + templateFileJsonObject['InstallDS'])
            if cerberusSetup.has_key('skipinstallds'):
                WriteToFile(outputFile, 'SkipInstallDS=' + cerberusSetup['skipinstallds'])
            else:
                WriteToFile(outputFile, 'SkipInstallDS=' + templateFileJsonObject['SkipInstallDS'])
            if cerberusSetup.has_key('upgradeds'):
                WriteToFile(outputFile, 'UpgradeDS=' + cerberusSetup['upgradeds'])
            else:
                WriteToFile(outputFile, 'UpgradeDS=' + templateFileJsonObject['UpgradeDS'])
            if cerberusSetup.has_key('removeds'):
                WriteToFile(outputFile, 'RemoveDS=' + cerberusSetup['removeds'])
            else:
                WriteToFile(outputFile, 'RemoveDS=' + templateFileJsonObject['RemoveDS'])
            if cerberusSetup.has_key('boeregsubkey'):
                WriteToFile(outputFile, 'BOEregsubkey=' + cerberusSetup['boeregsubkey'])
            else:
                WriteToFile(outputFile, 'BOEregsubkey=' + templateFileJsonObject['BOEregsubkey'])
            if cerberusSetup.has_key('dsregsubkey'):
                WriteToFile(outputFile, 'DSregsubkey=' + cerberusSetup['dsregsubkey'])
            else:
                WriteToFile(outputFile, 'DSregsubkey=' + templateFileJsonObject['DSregsubkey'])
    except Exception,e:
        logger.error('Catched Error: ' + str(Exception) + ' : ' + str(e))
    finally:
        inputFile.close()
        templateFile.close()


def CreateInstallStepsFileFromJson(inputFile, outputPath):
    inputFile = open(inputFile, 'r')
    try:
        inputFileJsonObject = json.loads(inputFile.read())
        for installSteps in inputFileJsonObject['installationsteps']:
            outputFolder = outputPath + '\\' + installSteps['machinename']
            if not os.path.isdir(outputFolder):
                os.mkdir(outputFolder)
            outputFile = outputFolder + '\\InstallSteps.ini'
            if os.path.isfile(outputFile):
                os.remove(outputFile)
            for i in range(1, len(installSteps)):
                if len(installSteps['step' + str(i)]) == 1:
                    WriteToFile(outputFile, installSteps['step' + str(i)][0])
                if len(installSteps['step' + str(i)]) == 2:
                    WriteToFile(outputFile, installSteps['step' + str(i)][0] + ', ' + installSteps['step' + str(i)][1])
                if len(installSteps['step' + str(i)]) > 2:
                    raise Exception('step' + str(i) + ' for ' + installSteps['machinename'] + ' cannot have three fields!')
    except Exception,e:
        logger.error('Catched Error: ' + str(Exception) + ' : ' + str(e))
    finally:
        inputFile.close()





inputPath = rootPath + inputFolder
outputPath = rootPath + outputFolder
setupPath = rootPath + setupFolder
for inputFileName in os.listdir(inputPath):
    if inputFileName.find('.json') >= 0:
        inputFile = inputPath + '\\' + inputFileName
        CreateInstallInfoFileFromJson(inputFile, outputPath, setupPath)
        CreateSetupFileFromJson(inputFile, outputPath)
        CreateInstallStepsFileFromJson(inputFile, outputPath)