__author__ = 'i067382'

import os
import time
import subprocess
import winreg
import re
import logging

logger = logging.getLogger('Log')

#Function: Check whether project is usable
def CheckEnv(ProjectPath):
    FolderStatus = os.path.isdir(ProjectPath)
    if FolderStatus is False:
        print('Error: Cerberus summon scroll is not there!')
        logger.error('Cerberus summon scroll is not there!')
        return False
    FolderStatus = os.path.isdir(ProjectPath + '\\setup')
    if FolderStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup')
        return False
    FolderStatus = os.path.isdir(ProjectPath + '\\setup\\ResponseFiles')
    if FolderStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\ResponseFiles')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\ResponseFiles')
        return False
    FolderStatus = os.path.isdir(ProjectPath + '\\setup\\Cerberus')
    if FolderStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\NodeNameReplaceCode.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\NodeNameReplaceCode.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\NodeNameReplaceCode.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\NodeNameReplaceCode.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\NodeNameReplaceCode.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\NodeNameReplaceCode.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\BOEProductCode.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\BOEProductCode.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\DSDisplayName.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\DSDisplayName.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    #According to new design, installed BOE path no longer needed
    #FileStatus = os.path.isfile(ProjectPath + '\\setup\\boedefaultpath.ini')
    #if FileStatus is False:
    #    print('Error: Cerberus summon scroll missing spell! spell Name: \\setup\\boedefaultpath.ini')
    #    logger.error('Cerberus summon scroll missing spell! spell Name: \\setup\\boedefaultpath.ini')
    #    return False
    print('Cerberus summon scroll is good to use')
    logger.info('Cerberus summon scroll is good to use')

#Function: Initial machine env
def InitEnv(ProjectPath):
    ProjectExists = False
    FolderStatus = os.path.isdir(ProjectPath + '\\machineinfo')
    if FolderStatus is False:
        os.mkdir(ProjectPath + '\\machineinfo')
    else:
        ProjectExists = True
    FolderStatus = os.path.isdir(ProjectPath + '\\installinfo')
    if FolderStatus is False:
        os.mkdir(ProjectPath + '\\installinfo')
    else:
        ProjectExists = True
    FileStatus = os.path.isfile(ProjectPath + '\\machineinfo\\machineinfo.ini')
    if FileStatus is True:
        RenameFile(ProjectPath + '\\machineinfo\\', 'machineinfo.ini')
        ProjectExists = True
    FileStatus = os.path.isfile(ProjectPath + '\\installinfo\\installinfo.ini')
    if FileStatus is True:
        RenameFile(ProjectPath + '\\installinfo\\', 'installinfo.ini')
        ProjectExists = True
    #According to new design, installed BOE path no longer needed
    #FileStatus = os.path.isfile(ProjectPath + '\\machineinfo\\InputBOEPath.ini')
    #if FileStatus is True:
    #    RenameFile(ProjectPath + '\\machineinfo\\', 'InputBOEPath.ini')
    #    ProjectExists = True
    FileStatus = os.path.isfile(ProjectPath + '\\InstallSteps.ini')
    if FileStatus is True:
        os.remove(ProjectPath + '\\InstallSteps.ini')
        ProjectExists = True
    if ProjectExists is True:
        print('Old Cerberus need to vanish, we will summon a new one')
        logger.info('Old Cerberus need to vanish, we will summon a new one')
    print('Cerberus summoned')
    logger.info('Cerberus summoned')

#Function: Print a input question and get input value
def AskForInput(AskPhrase, NeedConfirm = True, IsPassword = False):
    IsCorrect = 'N'
    if NeedConfirm is True:
         while IsCorrect.upper() != 'Y' and IsCorrect.upper() != 'YES':
            ConfirmChoice = False
            InputValue = input(AskPhrase + ': ')
            while ConfirmChoice  is False:
                IsCorrect = input('Is you input ' + InputValue + ' correct? [Y/N]: ')
                if IsCorrect.upper() == 'Y' or IsCorrect.upper() == 'YES' or IsCorrect.upper() == 'N' or IsCorrect.upper() == 'NO':
                    ConfirmChoice = True
    else:
        InputValue = input(AskPhrase + ': ')
    return InputValue

#Function: Write line to a file
def WriteToFile(FileLoc, InputLine, DeleteBeforeWrite = False):
    if DeleteBeforeWrite is True:
        FileStatus = os.path.isfile(FileLoc)
        if FileStatus is True:
            os.remove(FileLoc)
    File = open(FileLoc, 'a')
    try:
        File.write(InputLine + '\n')
    finally:
        File.close()

#Function: Generate node name parameter
def GenerateNodeName(NodeName, ReplaceCodeListLoc, ExtraReplaceCode = ''):
    ReplaceCodeList = open(ReplaceCodeListLoc, 'r')
    try:
        ReplaceCode = ReplaceCodeList.readline()
        while ReplaceCode:
            ReplaceCode = PurifyLine(ReplaceCode)
            ReplaceCode = PurifyLine(ReplaceCode, ' ')
            NodeName = NodeName.replace(ReplaceCode, '_')
            ReplaceCode = ReplaceCodeList.readline()
    finally:
        ReplaceCodeList.close()
    if ExtraReplaceCode != '':
        NodeName = NodeName.replace(ExtraReplaceCode, '_')
    return NodeName.upper()

#Function: Keep line string only and remove specific content from a line
def PurifyLine(Line, ExtraPurifyCode = ''):
    if not Line:
        return Line
    Line = Line.replace('\n', '')
    Line = Line.replace('\r', '')
    Line = Line.replace('\t', '')
    Line = Line.lstrip()
    Line = Line.rstrip()
    if ExtraPurifyCode != '':
        Line = Line.replace(ExtraPurifyCode, '')
    return Line

#Not used old function. According to new design, will not need installed BOE path
#def CheckInstalledBOEPath(ProjectPath):
#    FileStatus = os.path.isfile(ProjectPath + '\\machineinfo\\InputBOEPath.ini')
#    FoundinstalledBOEPath = True
#    if FileStatus is True:
#        InstalledBOEPath = ReadFromFile(ProjectPath + '\\machineinfo\\InputBOEPath.ini', 1)
#        InstalledBOEVersion = CheckBOEVerison(ProjectPath, InstalledBOEPath, 1)
#        if InstalledBOEVersion == '-1':
#           InstalledBOEVersion = CheckBOEVerison(ProjectPath, DoNotPrint=1)
#            if InstalledBOEVersion == '-1':
#                FoundinstalledBOEPath = False
#            else:
#                return ReadFromFile(ProjectPath + '\\setup\\boedefaultpath.ini')
#        else:
#            return InstalledBOEPath
#    else:
#        InstalledBOEVersion = CheckBOEVerison(ProjectPath, DoNotPrint=1)
#        if InstalledBOEVersion == '-1':
#            FoundinstalledBOEPath = False
#        else:
#            return ReadFromFile(ProjectPath + '\\setup\\boedefaultpath.ini')

#Not used old function. According to new design, will use Registry to get DS version
#def CheckDSVersion(ProjectPath, DoNotPrint=0):
#    Link_Dir = os.environ.get('LINK_DIR')
#    if not Link_Dir:
#        WriteToFile(ProjectPath + '\\machineinfo\\InstalledDSVersion.ini', '-1', True)
#        if DoNotPrint == 0:
#            print('Cerberus cannot detect your installed DS!')
#            logger.info('Cerberus cannot detect your installed DS!')
#        return -1
#    else:
#        if not os.path.isfile(Link_Dir + '\\bin\\al_engine.exe'):
#            WriteToFile(ProjectPath + '\\machineinfo\\InstalledDSVersion.ini', '-1', True)
#            if DoNotPrint == 0:
#                print('Cerberus cannot detect your installed DS!')
#                logger.info('Cerberus cannot detect your installed DS!')
#            return -1
#        else:
#            ps = subprocess.Popen('\"' + Link_Dir + '\\bin\\al_engine.exe' + '\"' + ' -v' + '>' + '\"' + ProjectPath + '\\machineinfo\\InstalledDSVersion.ini' + '\"', shell=True)
#            ps.wait()
#            InstalledDSVersionList = open(ProjectPath + '\\machineinfo\\InstalledDSVersion.ini', 'r')
#            try:
#                InstalledDSVersion = InstalledDSVersionList.readline()
#                InstalledDSVersion = PurifyLine(InstalledDSVersion)
#                InstalledDSVersion = ConvertVersionToNumber(InstalledDSVersion)
#                if InstalledDSVersion is False:
#                    if DoNotPrint == 0:
#                        print('Error: Cerberus cannot detect your installed DS version correctly')
#                        logger.error('Cerberus cannot detect your installed DS version correctly')
#                    return False
#            finally:
#                InstalledDSVersionList.close()
#            WriteToFile(ProjectPath + '\\machineinfo\\InstalledDSVersion.ini', InstalledDSVersion, True)
#            if DoNotPrint == 0:
#                print('Cerberus detected your installed DS. Version number: ' + InstalledDSVersion)
#                logger.info('Cerberus detected your installed DS. Version number: ' + InstalledDSVersion)
#            return InstalledDSVersion

#Function: Get installed DS version
def CheckDSVersion(ProjectPath, DoNotPrint=0):
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\Setup.ini')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
            logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
        return False
    subkey1 = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'DSregsubkey', '=')
    if subkey1 is False:
        if DoNotPrint == 0:
            print('Error: Cerberus cannot find DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Cerberus cannot find DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    DSDisplayName = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
    if DSDisplayName is False or len(DSDisplayName) == 0:
        if DoNotPrint == 0:
            print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
            logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
        return False

    try:
        key1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey1)
        key1count = winreg.QueryInfoKey(key1)[0]
        i = 0
        while i < key1count:
            subkey2 = subkey1 + winreg.EnumKey(key1, i)
            key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey2)
            valuecount = winreg.QueryInfoKey(key2)[1]
            j = 0
            FoundDSRegKey = False
            while j < valuecount:
                valuename = winreg.EnumValue(key2, j)[0]
                valuedata = winreg.EnumValue(key2, j)[1]
                if str(valuename) == 'DisplayName':
                    if valuedata.find(DSDisplayName[0]) != -1:
                        FoundDSRegKey = True
                if str(valuename) == 'DisplayVersion' and FoundDSRegKey is True:
                    InstalledDSVersion = ConvertVersionToNumber(valuedata)
                    if DoNotPrint == 0:
                        print('Cerberus detected your installed DS. Version number: ' + InstalledDSVersion)
                        logger.info('Cerberus detected your installed DS. Version number: ' + InstalledDSVersion)
                    return InstalledDSVersion
                j = j + 1
            i = i + 1
    except FileNotFoundError:
        if DoNotPrint == 0:
            print('Error: Wrong register key path: HKEY_LOCAL_MACHINE\\' + subkey1)
            logger.error('Wrong register key path: HKEY_LOCAL_MACHINE\\' + subkey1)
            print('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    except OSError:
        if DoNotPrint == 0:
            print('Error: OSError happened when try to get register key value')
            logger.error('OSError happened when try to get register key value')
            print('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    if DoNotPrint == 0:
        print('Cerberus cannot detect your installed DS!')
        logger.info('Cerberus cannot detect your installed DS!')
    return -1

#Function: Get installed DS uninstall string from Registry
def CheckDSUninstallString(ProjectPath, DoNotPrint=0):
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\Setup.ini')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
            logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
        return False
    subkey1 = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'DSregsubkey', '=')
    if subkey1 is False:
        if DoNotPrint == 0:
            print('Error: Cerberus cannot find DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Cerberus cannot find DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    DSDisplayName = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
    if DSDisplayName is False or len(DSDisplayName) == 0:
        if DoNotPrint == 0:
            print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
            logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\DSDisplayName.ini')
        return False

    try:
        key1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey1)
        key1count = winreg.QueryInfoKey(key1)[0]
        i = 0
        while i < key1count:
            subkey2 = subkey1 + winreg.EnumKey(key1, i)
            key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey2)
            valuecount = winreg.QueryInfoKey(key2)[1]
            j = 0
            FoundDSRegKey = False
            while j < valuecount:
                valuename = winreg.EnumValue(key2, j)[0]
                valuedata = winreg.EnumValue(key2, j)[1]
                if str(valuename) == 'DisplayName':
                    if valuedata.find(DSDisplayName[0]) != -1:
                        FoundDSRegKey = True
                if str(valuename) == 'UninstallString' and FoundDSRegKey is True:
                    return valuedata
                j = j + 1
            i = i + 1
    except FileNotFoundError:
        if DoNotPrint == 0:
            print('Error: Wrong register key path: HKEY_LOCAL_MACHINE\\' + subkey1)
            logger.error('Wrong register key path: HKEY_LOCAL_MACHINE\\' + subkey1)
            print('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    except OSError:
        if DoNotPrint == 0:
            print('Error: OSError happened when try to get register key value')
            logger.error('OSError happened when try to get register key value')
            print('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Check DSregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    if DoNotPrint == 0:
        print('Cerberus cannot detect your installed DS!')
        logger.info('Cerberus cannot detect your installed DS!')
    return ''

#Old version of get Installed BOE version. According to design, will use new function to get installed BOE version
#def CheckBOEVerison(ProjectPath, BOEInstallPath = '', DoNotPrint=0):
#    if BOEInstallPath == '':
#        BOEDefaultPathList = open(ProjectPath + '\\setup\\boedefaultpath.ini')
#        try:
#            BOEDefaultPath = BOEDefaultPathList.readline()
#            BOEDefaultPath = PurifyLine(BOEDefaultPath)
#        finally:
#            BOEDefaultPathList.close()
#        FileStatus = os.path.isfile(BOEDefaultPath + '\\win64_x64\\version\\version.txt')
#        if FileStatus is False:
#            WriteToFile(ProjectPath + '\\machineinfo\\InstalledBOEVersion.ini', '-1', True)
#            if DoNotPrint == 0:
#                print('Cerberus cannot detect your installed BOE!')
#                logger.info('Cerberus cannot detect your installed BOE!')
#            return -1
#        BOEInstallPath = BOEDefaultPath
#    else:
#        FolderStatus = os.path.isfile(BOEInstallPath + '\\win64_x64\\version\\version.txt')
#        if FolderStatus is False:
#            if DoNotPrint == 0:
#                print('Cerberus cannot detect your installed BOE! Check your installed BOE path!')
#                logger.info('Cerberus cannot detect your installed BOE! Check your installed BOE path!')
#            return -1
#
#    InstalledBOEVersionList = open(BOEInstallPath + '\\win64_x64\\version\\version.txt')
#    try:
#        InstalledBOEVersion = InstalledBOEVersionList.readline()
#        InstalledBOEVersion = PurifyLine(InstalledBOEVersion)
#        InstalledBOEVersion = ConvertVersionToNumber(InstalledBOEVersion)
#        if InstalledBOEVersion is False:
#            if DoNotPrint == 0:
#                print('Error: Cerberus cannot detect your installed BOE version correctly')
#                logger.error('Cerberus cannot detect your installed BOE version correctly')
#            return False
#    finally:
#        InstalledBOEVersionList.close()
#    WriteToFile(ProjectPath + '\\machineinfo\\InstalledBOEVersion.ini', InstalledBOEVersion, True)
#    if DoNotPrint == 0:
#        print('Cerberus detected your installed BOE. Version number: ' + InstalledBOEVersion)
#        logger.info('Cerberus detected your installed BOE. Version number: ' + InstalledBOEVersion)
#    return InstalledBOEVersion

#Function: Get install BOE version
def CheckBOEVerison(ProjectPath, DoNotPrint=0):
    InstalledBOEInfoList = CheckInstalledBOEList(ProjectPath)
    if InstalledBOEInfoList is False:
        if DoNotPrint == 0:
            print('Error: Error getting installed BOE list')
            logger.error('Error getting installed BOE list')
        return False
    if InstalledBOEInfoList == []:
        if DoNotPrint == 0:
            print('Cerberus cannot detect your installed BOE!')
            logger.info('Cerberus cannot detect your installed BOE!')
        return -1
    else:
        InstalledBOEVersion = InstalledBOEInfoList[len(InstalledBOEInfoList) - 1][1]
        if InstalledBOEVersion is False:
            if DoNotPrint == 0:
                print('Error: Cerberus cannot detect your installed BOE version correctly')
                logger.error('Cerberus cannot detect your installed BOE version correctly')
            return False
        else:
            if DoNotPrint == 0:
                print('Cerberus detected your installed BOE. Version number: ' + InstalledBOEVersion)
                logger.info('Cerberus detected your installed BOE. Version number: ' + InstalledBOEVersion)
            return InstalledBOEVersion

#Function: Get installed BOE type
def CheckBOEType(ProjectPath, DoNotPrint=0):
    InstalledBOEInfoList = CheckInstalledBOEList(ProjectPath, Reverse=True)
    if InstalledBOEInfoList is False:
        if DoNotPrint == 0:
            print('Error: Error getting installed BOE list')
            logger.error('Error getting installed BOE list')
        return False
    if InstalledBOEInfoList == []:
        if DoNotPrint == 0:
            print('Cerberus cannot detect your installed BOE!')
            logger.info('Cerberus cannot detect your installed BOE!')
        return -1
    else:
        InstalledBOEVersion = InstalledBOEInfoList[len(InstalledBOEInfoList) - 1][2]
        if InstalledBOEVersion is False:
            if DoNotPrint == 0:
                print('Error: Error getting BOE type string')
                logger.error('Error getting BOE type string')
            return False
        InstalledBOEType = ConvertVersionToType(InstalledBOEVersion)
        if InstalledBOEType is False:
            if DoNotPrint == 0:
                print('Error: Cerberus cannot detect your installed BOE type correctly')
                logger.error('Cerberus cannot detect your installed BOE type correctly')
            return False
        if DoNotPrint == 0:
            print('Cerberus detected your installed BOE type is ' + InstalledBOEType)
            logger.info('Cerberus detected your installed BOE type is ' + InstalledBOEType)
        return InstalledBOEType

#Function: Get BOE installation package version
def GetBOEVersion(BOEPackageLoc, DoNotPrint=0):
    FileStatus = os.path.isfile(BOEPackageLoc + '\\ProductId.txt')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus cannot detect your BOE package version! Check your BOE package!')
            logger.error('Cerberus cannot detect your BOE package version! Check your BOE package!')
        return False
    PackageBOEVersionList = open(BOEPackageLoc + '\\ProductId.txt')
    try:
        PackageBOEVersion = PackageBOEVersionList.readline()
        if PackageBOEVersion.find('minibip') == -1 and PackageBOEVersion.find('businessobjects') == -1:
            if DoNotPrint == 0:
                print('Error: Your BOE package may not be a correct BOE package! Check your BOE package!')
                logger.error('Your BOE package may not be a correct BOE package! Check your BOE package!')
            return False
        PackageBOEVersion = PurifyLine(PackageBOEVersion)
        PackageBOEVersion = ConvertVersionToNumber(PackageBOEVersion)
        if PackageBOEVersion is False:
            if DoNotPrint == 0:
                print('Error: Cerberus cannot detect your BOE package version correctly')
                logger.error('Cerberus cannot detect your BOE package version correctly')
            return False
        if DoNotPrint == 0:
            print('Your BOE package Version is ' + PackageBOEVersion + ' under ' + BOEPackageLoc)
            logger.info('Your BOE package Version is ' + PackageBOEVersion + ' under ' + BOEPackageLoc)
        return PackageBOEVersion
    finally:
        PackageBOEVersionList.close()

#Function: Get installed BOE list (all patch or package installed) from Registry
def CheckInstalledBOEList(ProjectPath, DoNotPrint=0, Reverse=False):
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\Setup.ini')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
            logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
        return False

    subkey1 = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'BOEregsubkey', '=')
    if subkey1 is False:
        if DoNotPrint == 0:
            print('Error: Cerberus cannot find BOEregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Cerberus cannot find BOEregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    BOEProduceCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
    if BOEProduceCodeList is False:
        if DoNotPrint == 0:
            print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
            logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
        return False

    InstalledBOEInfoList = []
    try:
        key1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey1)
        key1count = winreg.QueryInfoKey(key1)[0]
        i = 0
        while i < key1count:
            subkey2 = subkey1 + winreg.EnumKey(key1, i)
            key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey2)
            valuecount = winreg.QueryInfoKey(key2)[1]
            j = 0
            InstalledBOEInfo = ['','','']
            while j < valuecount:
                valuename = winreg.EnumValue(key2, j)[0]
                valuedata = winreg.EnumValue(key2, j)[1]
                if str(valuename) == 'DisplayName':
                    InstalledBOEInfo[0] = valuedata
                if str(valuename) == 'DisplayVersion':
                    valuedata = ConvertVersionToNumber(valuedata)
                    InstalledBOEInfo[1] = valuedata
                for BOEProduceCode in BOEProduceCodeList:
                    BOEProduceCode = PurifyLine(BOEProduceCode)
                    if str(valuedata).find(BOEProduceCode) != -1 and str(valuename) == 'UninstallString':
                        InstalledBOEInfo[2] = valuedata
                        InstalledBOEInfoList.append(InstalledBOEInfo)
                j = j + 1
            i = i + 1
    except FileNotFoundError:
        if DoNotPrint == 0:
            print('Error: Wrong register key path: HKEY_LOCAL_MACHINE\\' + subkey1)
            logger.error('Wrong register key path: HKEY_LOCAL_MACHINE\\' + subkey1)
            print('Check BOEregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Check BOEregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    except OSError:
        if DoNotPrint == 0:
            print('Error: OSError happened when try to get register key value')
            logger.error('OSError happened when try to get register key value')
            print('Check BOEregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
            logger.error('Check BOEregsubkey in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    InstalledBOEInfoList.sort(key=lambda x:x[1], reverse=Reverse)
    return InstalledBOEInfoList

#Function: Get BOE installation package type
def GetBOEPackageType(BOEPackageLoc, DoNotPrint=0):
    FileStatus = os.path.isfile(BOEPackageLoc + '\\ProductId.txt')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus cannot detect your BOE package type! Check your BOE package!')
            logger.error('Cerberus cannot detect your BOE package type! Check your BOE package!')
        return False
    PackageBOEVersionList = open(BOEPackageLoc + '\\ProductId.txt')
    try:
        PackageBOEType = PackageBOEVersionList.readline()
        if PackageBOEType.find('minibip') == -1 and PackageBOEType.find('businessobjects') == -1:
            if DoNotPrint == 0:
                print('Error: Your BOE package may not be a correct BOE package! Check your BOE package!')
                logger.error('Your BOE package may not be a correct BOE package! Check your BOE package!')
            return False
        PackageBOEType = PurifyLine(PackageBOEType)
        PackageBOEType = ConvertVersionToType(PackageBOEType)
        if PackageBOEType is False:
            if DoNotPrint == 0:
                print('Error: Cerberus cannot detect your BOE package type correctly')
                logger.error('Cerberus cannot detect your BOE package type correctly')
            return False
        if DoNotPrint == 0:
            print('Your BOE package Type is ' + PackageBOEType + ' under ' + BOEPackageLoc)
            logger.info('Your BOE package Type is ' + PackageBOEType + ' under ' + BOEPackageLoc)
        return PackageBOEType
    finally:
        PackageBOEVersionList.close()

#Function: Get DS installation package version
def GetDSVersion(DSPackageLoc, DoNotPrint=0):
    FileStatus = os.path.isfile(DSPackageLoc + '\\ProductId.txt')
    if FileStatus is False:
        if DoNotPrint == 0:
            print('Error: Cerberus cannot detect your DS package version! Check your DS package!')
            logger.error('Cerberus cannot detect your DS package version! Check your DS package!')
        return False
    PackageDSVersionList = open(DSPackageLoc + '\\ProductId.txt')
    try:
        PackageDSVersion = PackageDSVersionList.readline()
        if PackageDSVersion.find('dataservices') == -1:
            if DoNotPrint == 0:
                print('Error: Your DS package may not be a correct DS package! Check your DS package!')
                logger.error('Your DS package may not be a correct DS package! Check your DS package!')
            return False
        PackageDSVersion = PurifyLine(PackageDSVersion)
        PackageDSVersion = ConvertVersionToNumber(PackageDSVersion)
        if PackageDSVersion is False:
            if DoNotPrint == 0:
                print('Error: Cerberus cannot detect your DS package version correctly')
                logger.error('Cerberus cannot detect your DS package version correctly')
            return False
        if DoNotPrint == 0:
            print('Your DS package Version is ' + PackageDSVersion + ' under ' + DSPackageLoc)
            logger.info('Your DS package Version is ' + PackageDSVersion + ' under ' + DSPackageLoc)
        return PackageDSVersion
    finally:
        PackageDSVersionList.close()

#Not Used old function, replaced with ConvertVersionToNumber
#def ConvertStringToNumber(Version, WhichDotToKeep = 3):
#    OriVersion = Version
#    Version = list(filter(lambda ch: ch in '0123456789.-', Version))
#    VersionLen = len(Version)
#    DotCount = 0
#    for i in range(0, VersionLen):
#        if Version[i] == '.':
#            DotCount = DotCount + 1
#            if DotCount != WhichDotToKeep:
#                Version[i] = ''
#    Version = ''.join(Version)
#    try:
#        VersionTemp = float(Version)
#    except ValueError:
#        Version = Version.replace('-', '')
#        try:
#            VersionTemp = float(Version)
#        except ValueError:
#            print('Error: ' + OriVersion + ' cannot convert to number')
#            logger.error('' + OriVersion + ' cannot convert to number')
#            return False
#    return Version

#Function: Convert version string to a number
def ConvertVersionToNumber(Version, WhichDotToKeep = 3):
    OriVersion = Version
    Version = list(Version)
    VersionTemp = []
    DotCount = 0
    for bit in Version:
        if DotCount == 4:
            break
        if bit == '.':
            VersionTemp.append(bit)
            DotCount = DotCount + 1
        if bit.isdigit() is True:
            VersionTemp.append(bit)
    Version = VersionTemp
    VersionLen = len(Version)
    DotCount = 0
    for i in range(0, VersionLen):
        if Version[i] == '.':
            DotCount = DotCount + 1
            if DotCount != WhichDotToKeep:
                Version[i] = ''
    Version = ''.join(Version)
    try:
        VersionTemp = float(Version)
    except ValueError:
        print('Error: ' + OriVersion + ' cannot convert to number')
        logger.error(OriVersion + ' cannot convert to number')
        return False
    return Version

#Function: Convert version string to BOE type
def ConvertVersionToType(Version):
    if Version.find('minibip') != -1:
        if Version.find('patch') != -1:
            return 'MINIBIPPATCH'
        else:
            return 'MINIBIPPACKAGE'
    if Version.find('businessobjects64') != -1:
        if Version.find('patch') != -1:
            return 'FULLBOEPATCH'
        else:
            return 'FULLBOEPACKAGE'
    return False

#Function: Rename a file with time information suffix
def RenameFile(FilePath, FileName):
    time.sleep(1)
    FileStatus = os.path.isfile(FilePath + '\\' + FileName)
    if FileStatus is True:
        Filesuffix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        os.rename(FilePath + '\\' + FileName, FilePath + '\\' + FileName + Filesuffix)
    else:
        print('Error: Cerberus fail to find file: ' + FilePath + '\\' + FileName + ', cannot rename it')
        logger.error('Cerberus fail to find file: ' + FilePath + '\\' + FileName + ', cannot rename it')
        return False

#Function: Read content from a file. Support read specific number of lines, start read from specific line number, skip every specific number of lines
def ReadFromFile(FileLoc, LineLimit = 'ALL', StartLine = 1, SkipRead = 0):
    LineLimit = str(LineLimit)
    if LineLimit.upper() != 'ALL' and not LineLimit.isdigit():
        print('Error: LineCount must be number or ALL')
        logger.error('LineCount must be number or ALL')
        return False
    if StartLine < 1:
        print('Error: StartLine must larger than or equal to 1')
        logger.error('StartLine must larger than or equal to 1')
        return False
    if SkipRead < 0:
        print('Error: SkipRead must larger than or equal to 0')
        logger.error('SkipRead must larger than or equal to 0')
        return False
    FileStatus = os.path.isfile(FileLoc)
    if FileStatus is False:
        print('Error: Cerberus fail to find file: ' + FileLoc + ', cannot read it')
        logger.error('Cerberus fail to find file: ' + FileLoc + ', cannot read it')
        return False
    File = open(FileLoc, 'r')
    LineCount = 0
    LineContent = []
    SkipReadTemp = SkipRead
    try:
        if LineLimit.upper() == 'ALL':
            FileLine = File.readline()
            FileLine = PurifyLine(FileLine)
            while FileLine:
                if LineCount == StartLine - 1:
                    LineContent.append(FileLine)
                if LineCount > StartLine - 1 and SkipReadTemp == 0:
                    LineContent.append(FileLine)
                    SkipReadTemp = SkipRead
                    LineCount = LineCount + 1
                    FileLine = File.readline()
                    FileLine = PurifyLine(FileLine)
                    continue
                if LineCount > StartLine - 1 and SkipReadTemp >= 1:
                    SkipReadTemp = SkipReadTemp - 1
                LineCount = LineCount + 1
                FileLine = File.readline()
                FileLine = PurifyLine(FileLine)
            return LineContent
        else:
            LineLimit = int(LineLimit)
            if LineLimit < 0:
                print('Error: LineLimit must larger than or equal to 0')
                logger.error('LineLimit must larger than or equal to 0')
                return False
            FileLine = File.readline()
            FileLine = PurifyLine(FileLine)
            while FileLine and LineLimit > 0:
                if LineCount == StartLine - 1:
                    LineContent.append(FileLine)
                if LineCount > StartLine - 1 and SkipReadTemp == 0:
                    LineContent.append(FileLine)
                    SkipReadTemp = SkipRead
                    LineLimit = LineLimit - 1
                    LineCount = LineCount + 1
                    FileLine = File.readline()
                    FileLine = PurifyLine(FileLine)
                    continue
                if LineCount > StartLine - 1 and SkipReadTemp >= 1:
                    SkipReadTemp = SkipReadTemp - 1
                LineLimit = LineLimit - 1
                LineCount = LineCount + 1
                FileLine = File.readline()
                FileLine = PurifyLine(FileLine)
            return LineContent
    finally:
        File.close()

#Function: Generate InsallStep.ini
def GenerateInstallStepsFile(ProjectPath):
    WriteToFile(ProjectPath + '\\InstallSteps.ini', 'Define your Installation steps, use comma to seperate step and package location', True)

    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if SupportedStepsList is False:
        print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsString = ''
    for SupportedStep in SupportedStepsList:
        SupportedStepsString = SupportedStepsString + ', ' + SupportedStep
    SupportedStepsString = SupportedStepsString.replace(', ', '', 1)
    WriteToFile(ProjectPath + '\\InstallSteps.ini', 'Steps support: ' + SupportedStepsString)
    WriteToFile(ProjectPath + '\\InstallSteps.ini', 'InstallMiniBIP, Input Mini BIP package location')
    WriteToFile(ProjectPath + '\\InstallSteps.ini', 'InstallDS, Input DS package location')

#Function: Get Steps from InsallStep.ini
def GetSteps(ProjectPath):
    FileStatus = os.path.isfile(ProjectPath + '\\InstallSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus cannot find your steps file; ' + ProjectPath + '\\InstallSteps.ini')
        logger.error('Cerberus cannot find your steps file; ' + ProjectPath + '\\InstallSteps.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if SupportedStepsList is False:
        print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsString = ''
    for SupportedStep in SupportedStepsList:
        SupportedStepsString = SupportedStepsString + ', ' + SupportedStep
    SupportedStepsString = SupportedStepsString.replace(', ', '', 1)
    try:
        StepsList = open(ProjectPath + '\\InstallSteps.ini', 'r')
        LineNum = 0
        AllSteps = []
        for StepsLine in StepsList:
            LineNum = LineNum + 1
            StepsLine = PurifyLine(StepsLine)
            if StepsLine == 'Define your Installation steps, use comma to seperate step and package location':
                continue
            if StepsLine == 'Steps support: ' + SupportedStepsString:
                continue

            if StepsLine.upper().find('INSTALLMINIBIP') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input Mini BIP package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input Mini BIP package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'INSTALLMINIBIP':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input Mini BIP package location' or Step[1] == '':
                    print('Error: Please input Mini BIP package location at Line Number: ' + str(LineNum))
                    logger.error('Please input Mini BIP package location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your Mini BIP package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your Mini BIP package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        BOEPackageType = GetBOEPackageType(Step[1])
                        if BOEPackageType != 'MINIBIPPACKAGE' and BOEPackageType is not False:
                            print('Warning: Your Mini BIP package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not Mini BIP type, may cause problem later')
                            logger.warning('Your Mini BIP package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not Mini BIP type, may cause problem later')
                Step[0] = 'INSTALLMINIBIP'
                AllSteps.append(Step)

            if StepsLine.upper().find('INSTALLFULLBOE') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input full BOE package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input full BOE package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'INSTALLFULLBOE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input full BOE package location' or Step[1] == '':
                    print('Error: Please input full BOE package location at Line Number: ' + str(LineNum))
                    logger.error('Please input full BOE package location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your full BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your full BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        BOEPackageType = GetBOEPackageType(Step[1])
                        if BOEPackageType != 'FULLBOEPACKAGE' and BOEPackageType is not False:
                            print('Warning: Your full BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not full BOE type, may cause problem later')
                            logger.warning('Your full BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not full BOE type, may cause problem later')
                Step[0] = 'INSTALLFULLBOE'
                AllSteps.append(Step)

            if StepsLine.upper().find('INSTALLBOE') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input BOE package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input BOE package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'INSTALLBOE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input BOE package location' or Step[1] == '':
                    print('Error: Please input BOE package location at Line Number: ' + str(LineNum))
                    logger.error('Please input BOE package location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        BOEPackageType = GetBOEPackageType(Step[1])
                        if BOEPackageType != 'FULLBOEPACKAGE' and BOEPackageType != 'MINIBIPPACKAGE' and BOEPackageType is not False:
                            print('Warning: Your BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid BOE type, may cause problem later')
                            logger.warning('Your BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid BOE type, may cause problem later')
                Step[0] = 'INSTALLBOE'
                AllSteps.append(Step)

            if StepsLine.upper().find('PATCHFULLBOE') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input full BOE patch location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input full BOE patch location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'PATCHFULLBOE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input full BOE patch location' or Step[1] == '':
                    print('Error: Please input full BOE patch location at Line Number: ' + str(LineNum))
                    logger.error('Please input full BOE patch location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your full BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your full BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        BOEPackageType = GetBOEPackageType(Step[1])
                        if BOEPackageType != 'FULLBOEPATCH' and BOEPackageType is not False:
                            print('Warning: Your full BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not full BOE patch type, may cause problem later')
                            logger.warning('Your full BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not full BOE patch type, may cause problem later')
                Step[0] = 'PATCHFULLBOE'
                AllSteps.append(Step)

            if StepsLine.upper().find('PATCHMINIBIP') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input Mini BIP patch location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input Mini BIP patch location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'PATCHMINIBIP':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input Mini BIP patch location' or Step[1] == '':
                    print('Error: Please input Mini BIP patch location at Line Number: ' + str(LineNum))
                    logger.error('Please input Mini BIP patch location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your Mini BIP patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your Mini BIP patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        BOEPackageType = GetBOEPackageType(Step[1])
                        if BOEPackageType != 'MINIBIPPATCH' and BOEPackageType is not False:
                            print('Warning: Your Mini BIP patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not Mini BIP patch type, may cause problem later')
                            logger.warning('Your Mini BIP patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not Mini BIP patch type, may cause problem later')
                Step[0] = 'PATCHMINIBIP'
                AllSteps.append(Step)

            if StepsLine.upper().find('PATCHBOE') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input BOE patch location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input BOE patch location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'PATCHBOE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input BOE patch location' or Step[1] == '':
                    print('Error: Please input BOE patch location at Line Number: ' + str(LineNum))
                    logger.error('Please input BOE patch location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        BOEPackageType = GetBOEPackageType(Step[1])
                        if BOEPackageType != 'MINIBIPPATCH' and BOEPackageType != 'FULLBOEPATCH' and BOEPackageType is not False:
                            print('Warning: Your BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid BOE patch type, may cause problem later')
                            logger.warning('Your BOE patch location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid BOE patch type, may cause problem later')
                Step[0] = 'PATCHBOE'
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEFULLBOEPATCH') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input BOE patch produce code at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input BOE patch produce code at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'REMOVEFULLBOEPATCH':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                else:
                    BOEProductCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    if BOEProductCodeList is False:
                        print('Error: Error opening setup file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                        logger.error('Error opening setup file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                        return False
                    FoundBOEProduceCode = False
                    for BOEProductCode in BOEProductCodeList:
                        if BOEProductCode == Step[1]:
                            FoundBOEProduceCode = True
                    if FoundBOEProduceCode is False:
                        print('Warning: Cannot find your BOE product code: ' + Step[1] + ', may cause problem later')
                        logger.warning('Cannot find your BOE product code: ' + Step[1] + ', may cause problem later')
                Step[0] = 'REMOVEFULLBOEPATCH'
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEMINIBIPPATCH') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input BOE patch product code at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input BOE patch product code at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'REMOVEMINIBIPPATCH':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                else:
                    BOEProductCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    if BOEProductCodeList is False:
                        print('Error: Error opening setup file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                        logger.error('Error opening setup file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                        return False
                    FoundBOEProduceCode = False
                    for BOEProductCode in BOEProductCodeList:
                        if BOEProductCode == Step[1]:
                            FoundBOEProduceCode = True
                    if FoundBOEProduceCode is False:
                        print('Warning: Cannot find your BOE product code: ' + Step[1] + ', may cause problem later')
                        logger.warning('Cannot find your BOE product code: ' + Step[1] + ', may cause problem later')
                Step[0] = 'REMOVEMINIBIPPATCH'
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEBOEPATCH') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input BOE patch product code at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input BOE patch product code at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'REMOVEBOEPATCH':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                else:
                    BOEProductCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    if BOEProductCodeList is False:
                        print('Error: Error opening setup file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                        logger.error('Error opening setup file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                        return False
                    FoundBOEProduceCode = False
                    for BOEProductCode in BOEProductCodeList:
                        if BOEProductCode == Step[1]:
                            FoundBOEProduceCode = True
                    if FoundBOEProduceCode is False:
                        print('Warning: Cannot find your BOE product code: ' + Step[1] + ', may cause problem later')
                        logger.warning('Cannot find your BOE product code: ' + Step[1] + ', may cause problem later')
                Step[0] = 'REMOVEBOEPATCH'
                AllSteps.append(Step)

            if StepsLine.upper().find('INSTALLDS') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input DS package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input DS package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'INSTALLDS':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input DS package location' or Step[1] == '':
                    print('Error: Please input DS package location at Line Number: ' + str(LineNum))
                    logger.error('Please input DS package location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        DSPackageVersion = GetDSVersion(Step[1])
                        if DSPackageVersion is False:
                            print('Warning: Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid DS package, may cause problem later')
                            logger.warning('Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid DS package, may cause problem later')
                Step[0] = 'INSTALLDS'
                AllSteps.append(Step)

            if StepsLine.upper().find('SKIPINSTALLDS') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input DS package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input DS package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'SKIPINSTALLDS':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input DS package location' or Step[1] == '':
                    print('Error: Please input DS package location at Line Number: ' + str(LineNum))
                    logger.error('Please input DS package location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        DSPackageVersion = GetDSVersion(Step[1])
                        if DSPackageVersion is False:
                            print('Warning: Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid DS package, may cause problem later')
                            logger.warning('Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid DS package, may cause problem later')
                Step[0] = 'SKIPINSTALLDS'
                AllSteps.append(Step)

            if StepsLine.upper().find('UPGRADEDS') != -1:
                Step = StepsLine.split(',', 1)
                if len(Step) < 2:
                    print('Error: Please input DS package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    logger.error('Please input DS package location at Line Number: ' + str(LineNum) + ' and use comma to split')
                    return False
                Step[0] = PurifyLine(Step[0])
                Step[1] = PurifyLine(Step[1])
                if Step[0].upper() != 'UPGRADEDS':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                if Step[1] == 'Input DS package location' or Step[1] == '':
                    print('Error: Please input DS package location at Line Number: ' + str(LineNum))
                    logger.error('Please input DS package location at Line Number: ' + str(LineNum))
                    return False
                else:
                    FolderStatus = os.path.isdir(Step[1])
                    if FolderStatus is False:
                        print('Warning: Your BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                        logger.warning('Your BOE package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not reachable')
                    else:
                        DSPackageVersion = GetDSVersion(Step[1])
                        if DSPackageVersion is False:
                            print('Warning: Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid DS package, may cause problem later')
                            logger.warning('Your DS package location: ' + Step[1] + ' at Line Number: ' + str(LineNum) + ' is not a valid DS package, may cause problem later')
                Step[0] = 'UPGRADEDS'
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEMINIBIPPACKAGE') != -1:
                Step = PurifyLine(StepsLine)
                if Step.upper() != 'REMOVEMINIBIPPACKAGE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                Step = ['REMOVEMINIBIPPACKAGE', '']
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEFULLBOEPACKAGE') != -1:
                Step = PurifyLine(StepsLine)
                if Step.upper() != 'REMOVEFULLBOEPACKAGE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                Step = ['REMOVEFULLBOEPACKAGE', '']
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEBOE') != -1:
                Step = PurifyLine(StepsLine)
                if Step.upper() != 'REMOVEBOE':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                Step = ['REMOVEBOE', '']
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEALLBOEPATCH') != -1:
                Step = PurifyLine(StepsLine)
                if Step.upper() != 'REMOVEALLBOEPATCH':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                Step = ['REMOVEALLBOEPATCH', '']
                AllSteps.append(Step)

            if StepsLine.upper().find('REMOVEDS') != -1:
                Step = PurifyLine(StepsLine)
                if Step.upper() != 'REMOVEDS':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                Step = ['REMOVEDS', '']
                AllSteps.append(Step)

            if StepsLine.upper().find('CLEANUP') != -1:
                Step = PurifyLine(StepsLine)
                if Step.upper() != 'CLEANUP':
                    print('Error: Line format is wrong at Line Number: ' + str(LineNum))
                    logger.error('Line format is wrong at Line Number: ' + str(LineNum))
                    return False
                Step = ['CLEANUP', '']
                AllSteps.append(Step)

        return AllSteps
    finally:
        StepsList.close()

#Function: Substitute a specific file with parameter file to a output file
def SubParameter(ParamFile, SubFile, OutputFile, DeleteBeforeWrite = False):
    if DeleteBeforeWrite is True:
        FileStatus = os.path.isfile(OutputFile)
        if FileStatus is True:
            os.remove(OutputFile)
    FileStatus = os.path.isfile(ParamFile)
    if FileStatus is False:
        print('Error: Cerberus cannot find your parameter file: ' + ParamFile)
        logger.error('Cerberus cannot find your parameter file: ' + ParamFile)
        return False
    FileStatus = os.path.isfile(SubFile)
    if FileStatus is False:
        print('Error: Cerberus cannot find your substitute source file: ' + SubFile)
        logger.error('Cerberus cannot find your substitute source file: ' + SubFile)
        return False
    ParamFileList = open(ParamFile, 'r')
    SubFileList = open(SubFile, 'r')
    try:
        ParamFileLines = ParamFileList.readlines()
        SubFileLines = SubFileList.readlines()
        OutputFileLines = SubFileLines
        for ParamFileLine in ParamFileLines:
            ParamFileLine = PurifyLine(ParamFileLine)
            Param = ParamFileLine.split(':=')
            if len(Param) > 2:
                print('Error: Check parameter values, values cannot contain :=')
                logger.error('Check parameter values, values cannot contain :=')
                return False
            OutputFileLineCount = 0
            for OutputFileLine in OutputFileLines:
                OutputFileLine = PurifyLine(OutputFileLine)
                OutputFileLines[OutputFileLineCount] = OutputFileLine.replace(Param[0], Param[1])
                OutputFileLineCount = OutputFileLineCount + 1
        for OutputFileLine in OutputFileLines:
            WriteToFile(OutputFile, OutputFileLine)
    finally:
        ParamFileList.close()
        SubFileList.close()

#Function: Execute step
def ExecuteStep(ProjectPath, Step, ResponseFile):
    if len(Step) != 2:
        print(Step)
        logger.info(Step)
        print('Error: Your step do not meet the step format')
        logger.error('Your step do not meet the step format')
        return False
    if Step[0].upper() == 'SKIPSTEP':
        return True
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if SupportedStepsList is False:
        print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        return False
    FoundStep = False
    for SupportedStep in SupportedStepsList:
        if Step[0].upper() == SupportedStep.upper():
            FoundStep = True
    if FoundStep is False:
        print('Error: Cerberus current do not support your input step: ' + Step[0])
        logger.error('Cerberus current do not support your input step: ' + Step[0])
        return False
    FileStatus = os.path.isfile(ResponseFile)
    if FileStatus is False:
        print('Error: Cerberus cannot reach your response file: ' + ResponseFile)
        logger.error('Cerberus cannot reach your response file: ' + ResponseFile)
        return False

    FolderStatus = os.path.isdir(ProjectPath + '\\log\\')
    if FolderStatus is False:
        os.mkdir(ProjectPath + '\\Log\\')
    Log_Folder_Name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    Log_Folder = ProjectPath + '\\log\\' + Log_Folder_Name
    FolderStatus = os.path.isdir((Log_Folder))
    if FolderStatus is True:
        os.renames(Log_Folder, ProjectPath + '\\log\\' + Log_Folder_Name + '-bk')
    os.mkdir(Log_Folder)

    #According to new design, will use register to get ds unintall string
    #if Step[0].upper() == 'REMOVEDS':
    #    Link_Dir = os.environ.get('LINK_DIR')
    #    SAP_BO_Folder = Link_Dir.replace('\Data Services', '')
    #    SetupEngine_Folder = SAP_BO_Folder + '\\InstallData\\setup.engine\\'
    #    FileStatus = os.path.isfile(SetupEngine_Folder + 'SetupEngine.exe')
    #    if FileStatus is False:
    #        print('Error: Cerberus cannot uninstall DS. Cause no setupengine under ' + SetupEngine_Folder)
    #        logger.error('Cerberus cannot uninstall DS. Cause no setupengine under ' + SetupEngine_Folder)
    #        return False
    #    ps = subprocess.Popen('\"' + SetupEngine_Folder + 'SetupEngine.exe\" -engine \"' + SetupEngine_Folder +  '\\\" -bootstrapper \"' + SAP_BO_Folder + '\\\\\" -l \"' + Log_Folder + '\" \"-r\" \"' + ResponseFile + '\" \"-i\" \"product.dataservices64-4.0-core-32\"', shell=True)
    #    ps.wait()
    #    if ps.returncode > 0:
    #        print('Error: Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
    #        logger.error('Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
    #        return False
    #    else:
    #        return True

    if Step[0].upper() == 'REMOVEDS':
        DSUnintallString = CheckDSUninstallString(ProjectPath, 1)
        if DSUnintallString is False or DSUnintallString == '':
            print('Error: No DS uninstall string')
            logger.error('No DS uninstall string')
            return False
        ps = subprocess.Popen(DSUnintallString + ' \"-r\" ' + '\"' + ResponseFile + '\"', shell=True)
        ps.wait()
        if ps.returncode > 0:
            print('Error: Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
            logger.error('Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
            return False
        else:
            return True

    if Step[0].upper() == 'REMOVEMINIBIPPACKAGE' or Step[0].upper() == 'REMOVEFULLBOEPACKAGE' or Step[0].upper() == 'REMOVEMINIBIPPATCH' or Step[0].upper() == 'REMOVEFULLBOEPATCH':
        ps = subprocess.Popen(Step[1] + ' \"-r\" ' + '\"' + ResponseFile + '\"', shell=True)
        ps.wait()
        if ps.returncode > 0:
            print('Error: Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
            logger.error('Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
            return False
        else:
            return True

    if Step[1] != '':
        FolderStatus = os.path.isdir(Step[1])
        if FolderStatus is False:
            print('Error: Cerberus cannot reach your package location: ' + Step[1])
            logger.error('Cerberus cannot reach your package location: ' + Step[1])
            return False
        FileStatus = os.path.isfile(Step[1] + '\\setup.exe')
        if FileStatus is False:
            print('Error: Your package location: ' + Step[1] + ' do not contain setup.exe')
            logger.error('Your package location: ' + Step[1] + ' do not contain setup.exe')
            return False
        ps = subprocess.Popen('\"' + Step[1] + '\\setup.exe\" \"-r\" \"' + ResponseFile + '\"', shell=True)
        ps.wait()
        if ps.returncode > 0:
            print('Error: Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
            logger.error('Operation: '+ Step[0] + ' Failed. ' + 'Return code: ' + str(ps.returncode))
            return False
        else:
            return True

#Function: Get a variable's value from a parameter file. eg: value=3 in param.ini, input(param.ini, value, '='), output 3
def GetValueFromFile(File, VariableName, SpliteCode):
    VariableName = str(VariableName)
    SpliteCode = str(SpliteCode)
    if VariableName == '' or SpliteCode == '':
        print('Error: VariableName and SpliteCode cannot be blank')
        logger.error('VariableName and SpliteCode cannot be blank')
        return False
    Temp = VariableName.split(SpliteCode)
    if len(Temp) > 1:
        RandSuffix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        VariableName = VariableName.replace(SpliteCode, SpliteCode + RandSuffix)
    FileStatus = os.path.isfile(File)
    if FileStatus is False:
        print('Error: Cerberus cannot find get value file: ' + File)
        logger.error('Cerberus cannot find get value file: ' + File)
        return False
    VariablesList = open(File, 'r')
    HasSpliteCode = False
    FindVariableName = False
    for FileLine in VariablesList:
        FileLine = PurifyLine(FileLine)
        if FileLine.upper().find(VariableName.upper()) == 0:
            FindVariableName = True
            if FileLine.upper().find(SpliteCode.upper()) == -1:
                continue
            HasSpliteCode = True
            Variable = FileLine.split(SpliteCode, 1)
            if len(Variable) == 1:
                return ''
            if len(Variable) == 2:
                return Variable[1]
            if len(Variable) > 2:
                count = 1
                Value = []
                while count < len(Variable) - 1:
                    Value.append(Variable[count])
                    Value.append(SpliteCode)
                    count = count + 1
                Value.append(Variable[count])
                Value = ''.join(Value)
                return Value
    if HasSpliteCode is False and FindVariableName is True:
        print('Cerberus successfully find your variable: ' + VariableName + ', but cannot find your splite code: ' + SpliteCode)
        logger.info('Cerberus successfully find your variable: ' + VariableName + ', but cannot find your splite code: ' + SpliteCode)
    print('Error: Cerberus cannot find ' + VariableName + '\'s value in file ' + File)
    logger.error('Cerberus cannot find ' + VariableName + '\'s value in file ' + File)
    return False

#Function: Generate specific step's response file with parameter substituted
def GetResponseFile(ProjectPath, StepName):
    FolderStatus = os.path.isdir(ProjectPath + '\\installinfo')
    if FolderStatus is False:
        os.mkdir(ProjectPath + '\\installinfo')
    if StepName.upper() == 'SKIPSTEP':
        return ''
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if SupportedStepsList is False:
        print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        return False
    FoundStep = False
    for SupportedStep in SupportedStepsList:
        if StepName.upper() == SupportedStep.upper():
            FoundStep = True
    if FoundStep is False:
        print('Error: Cerberus current do not support your input step: ' + StepName)
        logger.error('Cerberus current do not support your input step: ' + StepName)
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\Setup.ini')
    if FileStatus is False:
        print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    ResponseFileName = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', StepName, '=')
    if ResponseFileName is False:
        print('Error: Cerberus cannot find step: ' + StepName + '\'s response file name in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        logger.error('Cerberus cannot find step: ' + StepName + '\'s response file name in ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\installinfo\\' + ResponseFileName)
    if FileStatus is True:
        RenameFile(ProjectPath + '\\installinfo', ResponseFileName)
    if SubParameter(ProjectPath + '\\installinfo\\installinfo.ini', ProjectPath + '\\setup\\ResponseFiles\\' + ResponseFileName, ProjectPath + '\\installinfo\\' + ResponseFileName) is False:
        print('Error: Cerberus cannot generate response file')
        logger.error('Cerberus cannot generate response file')
        return False
    return ProjectPath + '\\installinfo\\' + ResponseFileName

#Function: Interprete step to correct steps
def GetCorrectStep(ProjectPath, Step, InstalledBOEVersion, InstalledDSVersion, InstalledBOEType, ExOption=''):
    try:
        InstalledBOEVersion = float(InstalledBOEVersion)
    except ValueError:
        print('Error: InstalledBOEVersion must be number')
        logger.error('InstalledBOEVersion must be number')
        return False
    try:
        InstalledDSVersion = float(InstalledDSVersion)
    except ValueError:
        print('Error: InstalledDSVersion must be number')
        logger.error('InstalledDSVersion must be number')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\Setup.ini')
    if FileStatus is False:
        print('Error: Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        logger.error('Cerberus missing important file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini')
        return False
    if len(Step) != 2:
        print(Step)
        logger.info(Step)
        print('Error: Your step does not meet the step format')
        logger.error('Your step does not meet the step format')
        return False
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if SupportedStepsList is False:
        print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        return False
    FoundStep = False
    for SupportedStep in SupportedStepsList:
        if Step[0].upper() == SupportedStep.upper():
            FoundStep = True
    if FoundStep is False:
        print('Error: Cerberus currently does not support your input step: ' + Step[0])
        logger.error('Cerberus currently does not support your input step: ' + Step[0])
        return False
    if Step[1] != '' and Step[0].upper() !='REMOVEBOEPATCH' and Step[0].upper() !='REMOVEFULLBOEPATCH' and Step[0].upper() !='REMOVEMINIBIPPATCH':
        FolderStatus = os.path.isdir(Step[1])
        if FolderStatus is False:
            print('Error: Cerberus cannot reach your package location: ' + Step[1])
            logger.error('Cerberus cannot reach your package location: ' + Step[1])
            return False
        FileStatus = os.path.isfile(Step[1] + '\\setup.exe')
        if FileStatus is False:
            print('Error: Your package location: ' + Step[1] + ' do not contain setup.exe')
            logger.error('Your package location: ' + Step[1] + ' do not contain setup.exe')
            return False

    CorrectStep = []
    if Step[0].upper() == 'REMOVEMINIBIPPACKAGE':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEMINIBIPPACKAGE will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEMINIBIPPACKAGE will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            if InstalledBOEType != 'MINIBIPPACKAGE':
                print('Error: Installed BOE is not Mini BIP, step REMOVEMINIBIPPACKAGE cannot be processed, Cerberus will stop')
                logger.error('Installed BOE is not Mini BIP, step REMOVEMINIBIPPACKAGE cannot be processed, Cerberus will stop')
                return False
            else:
                CorrectStep.append(Step)
        return CorrectStep

    if Step[0].upper() == 'REMOVEFULLBOEPACKAGE':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEFULLBOEPACKAGE will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEFULLBOEPACKAGE will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            if InstalledBOEType != 'FULLBOEPACKAGE':
                print('Error: Installed BOE is not full BOE, step REMOVEFULLBOEPACKAGE cannot be processed, Cerberus will stop')
                logger.error('Installed BOE is not full BOE, step REMOVEFULLBOEPACKAGE cannot be processed, Cerberus will stop')
                return False
            else:
                CorrectStep.append(Step)
        return CorrectStep

    if Step[0].upper() == 'REMOVEDS':
        if InstalledDSVersion == -1:
            print('Warning: No DS installed on your machine, step REMOVEDS will be skipped')
            logger.warning('No DS installed on your machine, step REMOVEDS will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            CorrectStep.append(Step)
        return CorrectStep

    if Step[0].upper() == 'REMOVEFULLBOEPATCH':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEFULLBOEPATCH will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEFULLBOEPATCH will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            if InstalledBOEType != 'FULLBOEPACKAGE' and InstalledBOEType != 'FULLBOEPATCH':
                print('Error: Installed BOE is not full BOE, step REMOVEFULLBOEPATCH cannot be processed, Cerberus will stop')
                logger.error('Installed BOE is not full BOE, step REMOVEFULLBOEPATCH cannot be processed, Cerberus will stop')
                return False
            else:
                BOEProductCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                if BOEProductCodeList is False:
                    print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    return False
                FoundBOEProductCode = False
                for BOEProductCode in BOEProductCodeList:
                    if BOEProductCode == Step[1]:
                        FoundBOEProductCode = True
                if FoundBOEProductCode is False:
                    print('Warning: Cannot find your BOE product Code: ' + Step[1] + ', may cause problem later')
                    logger.warning('Cannot find your BOE product Code: ' + Step[1] + ', may cause problem later')
                InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
                if InstalledBOEList is False:
                    print('Error: Error getting installed BOE list')
                    logger.error('Error getting installed BOE list')
                    return False
                if InstalledBOEList == []:# or len(InstalledBOEList) == 1:
                    print('Warning: No BOE patch installed on your machine, step REMOVEFULLBOEPATCH will be skipped')
                    logger.warning('No BOE patch installed on your machine, step REMOVEFULLBOEPATCH will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                FoundBOEProductCode = False
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find(Step[1]) != -1 and InstalledBOE[2].find('patch') != -1:
                        FoundBOEProductCode =True
                if FoundBOEProductCode is False:
                    print('Warning: Cannot find installed BOE patch match with your input product code: ' + Step[1] + ', step REMOVEFULLBOEPATCH will be skipped')
                    logger.warning('Cannot find installed BOE patch match with your input product code: ' + Step[1] + ', step REMOVEFULLBOEPATCH will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                else:
                    tempStep = InstalledBOEList[0][2]
                    for BOEProductCode in BOEProductCodeList:
                        tempStep = tempStep.replace(BOEProductCode, '')
                    Step[1] = tempStep + Step[1]
                CorrectStep.append(Step)
        return CorrectStep

    if Step[0].upper() == 'REMOVEMINIBIPPATCH':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEFULLBOEPATCH will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEFULLBOEPATCH will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            if InstalledBOEType != 'MINIBIPPACKAGE' and InstalledBOEType != 'MINIBIPPATCH':
                print('Error: Installed BOE is not Mini BIP, step REMOVEMINIBIPPATCH cannot be processed, Cerberus will stop')
                logger.error('Installed BOE is not Mini BIP, step REMOVEMINIBIPPATCH cannot be processed, Cerberus will stop')
                return False
            else:
                BOEProductCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                if BOEProductCodeList is False:
                    print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    return False
                FoundBOEProductCode = False
                for BOEProductCode in BOEProductCodeList:
                    if BOEProductCode == Step[1]:
                        FoundBOEProductCode = True
                if FoundBOEProductCode is False:
                    print('Warning: Cannot find your BOE product Code: ' + Step[1] + ', may cause problem later')
                    logger.warning('Cannot find your BOE product Code: ' + Step[1] + ', may cause problem later')
                InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
                if InstalledBOEList is False:
                    print('Error: Error getting installed BOE list')
                    logger.error('Error getting installed BOE list')
                    return False
                if InstalledBOEList == []:# or len(InstalledBOEList) == 1:
                    print('Warning: No BOE patch installed on your machine, step REMOVEMINIBIPPATCH will be skipped')
                    logger.warning('No BOE patch installed on your machine, step REMOVEMINIBIPPATCH will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                FoundBOEProductCode = False
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find(Step[1]) != -1 and InstalledBOE[2].find('patch') != -1:
                        FoundBOEProductCode =True
                if FoundBOEProductCode is False:
                    print('Warning: Cannot find installed BOE patch match with your input product code: ' + Step[1] + ', step REMOVEMINIBIPPATCH will be skipped')
                    logger.warning('Cannot find installed BOE patch match with your input product code: ' + Step[1] + ', step REMOVEMINIBIPPATCH will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                else:
                    tempStep = InstalledBOEList[0][2]
                    for BOEProductCode in BOEProductCodeList:
                        tempStep = tempStep.replace(BOEProductCode, '')
                    Step[1] = tempStep + Step[1]
                CorrectStep.append(Step)
        return CorrectStep

    if Step[0].upper() == 'REMOVEBOEPATCH':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEBOEPATCH will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEBOEPATCH will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            if InstalledBOEType == 'MINIBIPPACKAGE':
                Step[0] = 'REMOVEMINIBIPPATCH'
            if InstalledBOEType == 'FULLBOEPACKAGE':
                Step[0] = 'REMOVEFULLBOEPATCH'
            if InstalledBOEType != 'FULLBOEPACKAGE' and InstalledBOEType != 'MINIBIPPACKAGE' and InstalledBOEType != 'MINIBIPPATCH' and InstalledBOEType != 'FULLBOEPATCH':
                print('Error: Installed BOE is not full BOE or Mini BIP, step REMOVEBOEPATCH cannot be processed, Cerberus will stop')
                logger.error('Installed BOE is not full BOE or Mini BIP, step REMOVEBOEPATCH cannot be processed, Cerberus will stop')
                return False
            else:
                BOEProductCodeList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                if BOEProductCodeList is False:
                    print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\BOEProductCode.ini')
                    return False
                FoundBOEProductCode = False
                for BOEProductCode in BOEProductCodeList:
                    if BOEProductCode == Step[1]:
                        FoundBOEProductCode = True
                if FoundBOEProductCode is False:
                    print('Warning: Cannot find your BOE product Code: ' + Step[1] + ', may cause problem later')
                    logger.warning('Cannot find your BOE product Code: ' + Step[1] + ', may cause problem later')
                InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
                if InstalledBOEList is False:
                    print('Error: Error getting installed BOE list')
                    logger.error('Error getting installed BOE list')
                    return False
                if InstalledBOEList == []: #or len(InstalledBOEList) == 1:
                    print('Warning: No BOE patch installed on your machine, step REMOVEBOEPATCH will be skipped')
                    logger.warning('No BOE patch installed on your machine, step REMOVEBOEPATCH will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                FoundBOEProductCode = False
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find(Step[1]) != -1 and InstalledBOE[2].find('patch') != -1:
                        FoundBOEProductCode =True
                if FoundBOEProductCode is False:
                    print('Warning: Cannot find installed BOE patch match with your input product code: ' + Step[1] + ', step REMOVEBOEPATCH will be skipped')
                    logger.warning('Cannot find installed BOE patch match with your input product code: ' + Step[1] + ', step REMOVEBOEPATCH will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                else:
                    tempStep = InstalledBOEList[0][2]
                    for BOEProductCode in BOEProductCodeList:
                        tempStep = tempStep.replace(BOEProductCode, '')
                    Step[1] = tempStep + Step[1]
                CorrectStep.append(Step)
        return CorrectStep

    if Step[0].upper() == 'REMOVEBOE':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEBOE will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEBOE will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1, True)
            if InstalledBOEList is False:
                print('Error: Error getting installed BOE list')
                logger.error('Error getting installed BOE list')
            if InstalledBOEType == 'MINIBIPPACKAGE':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEMINIBIPPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEMINIBIPPACKAGE', InstalledBOE[2]])
            if InstalledBOEType == 'FULLBOEPACKAGE':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEFULLBOEPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEFULLBOEPACKAGE', InstalledBOE[2]])
            if InstalledBOEType == 'MINIBIPPATCH':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEMINIBIPPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEMINIBIPPACKAGE', InstalledBOE[2]])
            if InstalledBOEType == 'FULLBOEPATCH':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEFULLBOEPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEFULLBOEPACKAGE', InstalledBOE[2]])
            return CorrectStep

    if Step[0].upper() == 'REMOVEALLBOEPATCH':
        if InstalledBOEVersion == -1:
            print('Warning: No BOE installed on your machine, step REMOVEALLBOEPATCH will be skipped')
            logger.warning('No BOE installed on your machine, step REMOVEALLBOEPATCH will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        else:
            InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1, True)
            FoundInstalledBOEPatch = False
            if InstalledBOEList is False:
                print('Error: Error getting installed BOE list')
                logger.error('Error getting installed BOE list')
            if InstalledBOEType == 'MINIBIPPACKAGE':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEMINIBIPPATCH', InstalledBOE[2]])
                        FoundInstalledBOEPatch = True
            if InstalledBOEType == 'FULLBOEPACKAGE':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEFULLBOEPATCH', InstalledBOE[2]])
                        FoundInstalledBOEPatch = True
            if InstalledBOEType == 'MINIBIPPATCH':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEMINIBIPPATCH', InstalledBOE[2]])
                        FoundInstalledBOEPatch = True
            if InstalledBOEType == 'FULLBOEPATCH':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEFULLBOEPATCH', InstalledBOE[2]])
                        FoundInstalledBOEPatch = True
            if FoundInstalledBOEPatch is False:
                print('Warning: No BOE patch installed on your machine, step REMOVEALLBOEPATCH will be skipped')
                logger.warning('No BOE patch installed on your machine, step REMOVEALLBOEPATCH will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
            return CorrectStep

    if Step[0].upper() == 'CLEANUP':
        if InstalledBOEVersion >= 0:
            InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1, True)
            if InstalledBOEList is False:
                print('Error: Error getting installed BOE list')
                logger.error('Error getting installed BOE list')
            if InstalledBOEType == 'MINIBIPPACKAGE':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEMINIBIPPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEMINIBIPPACKAGE', InstalledBOE[2]])
            if InstalledBOEType == 'FULLBOEPACKAGE':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEFULLBOEPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEFULLBOEPACKAGE', InstalledBOE[2]])
            if InstalledBOEType == 'MINIBIPPATCH':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEMINIBIPPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEMINIBIPPACKAGE', InstalledBOE[2]])
            if InstalledBOEType == 'FULLBOEPATCH':
                for InstalledBOE in InstalledBOEList:
                    if InstalledBOE[2].find('patch') != -1:
                        CorrectStep.append(['REMOVEFULLBOEPATCH', InstalledBOE[2]])
                    else:
                        CorrectStep.append(['REMOVEFULLBOEPACKAGE', InstalledBOE[2]])
        if InstalledDSVersion >= 0:
            CorrectStep.append(['REMOVEDS',''])
        if InstalledBOEVersion == -1 and InstalledDSVersion == -1:
            print('Warning: No DS and BOE installed on your machine, step CLEANUP will be skipped')
            logger.warning('No DS and BOE installed on your machine, step CLEANUP will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
        return CorrectStep

    if Step[0].upper() == 'UPGRADEDS':
        DSUpgradeForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'DSUpgradeForceInstall', '=')
        if DSUpgradeForceInstall != '0' and DSUpgradeForceInstall != '1':
            print('Warning: Parameter DSUpgradeForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter DSUpgradeForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if DSUpgradeForceInstall is False:
            print('Warning: No parameter DSUpgradeForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter DSUpgradeForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        DSUpgradeForceUpgrade = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'DSUpgradeForceUpgrade', '=')
        if DSUpgradeForceUpgrade != '0' and DSUpgradeForceUpgrade != '1':
            print('Warning: Parameter DSUpgradeForceUpgrade in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter DSUpgradeForceUpgrade in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if DSUpgradeForceUpgrade is False:
            print('Warning: No parameter DSUpgradeForceUpgrade in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter DSUpgradeForceUpgrade in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')

        if InstalledDSVersion == -1:
            if DSUpgradeForceInstall == '1':
                print('Warning: No DS installed on your machine, according to setup, will force install DS')
                logger.warning('No DS installed on your machine, according to setup, will force install DS')
                if InstalledBOEVersion > 0:
                    CorrectStep.append(['INSTALLDS',Step[1]])
                if InstalledBOEVersion == -1:
                    CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                return  CorrectStep
            print('Warning: No DS installed on your machine, step UPGRADEDS will be skipped')
            logger.warning('No DS installed on your machine, step UPGRADEDS will be skipped')
            CorrectStep.append(['SKIPSTEP',''])
            return  CorrectStep
        if InstalledDSVersion >= 0:
            PackageDSVersion = GetDSVersion(Step[1])
            if PackageDSVersion is False:
                return False
            else:
                if float(PackageDSVersion) > InstalledDSVersion:
                    CorrectStep.append(Step)
                else:
                    if DSUpgradeForceUpgrade == '1':
                        print('Warning: your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will remove installed DS first, than install your DS package')
                        logger.warning('According to your setup, will remove installed DS first, than install your DS package')
                        CorrectStep.append(['REMOVEDS',''])
                        if InstalledBOEVersion > 0:
                            CorrectStep.append(['INSTALLDS',Step[1]])
                        if InstalledBOEVersion == -1:
                            CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                        return  CorrectStep
                    print('Warning: your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion) + ' step UPGRADEDS will be skipped')
                    logger.warning('your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion) + ' step UPGRADEDS will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
            return  CorrectStep

    if Step[0].upper() == 'INSTALLMINIBIP':
        MiniBIPInstallForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'MiniBIPInstallForceInstall', '=')
        if ExOption != '':
            MiniBIPInstallForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', ExOption, '=')
        if MiniBIPInstallForceInstall != '0' and MiniBIPInstallForceInstall != '1':
            print('Warning: Parameter MiniBIPInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter MiniBIPInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if MiniBIPInstallForceInstall is False:
            print('Warning: No parameter MiniBIPInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter MiniBIPInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        PackageBOEVersion = GetBOEVersion(Step[1])
        PackageBOEType = GetBOEPackageType(Step[1])
        if PackageBOEVersion is False or PackageBOEType is False:
            return False
        if InstalledBOEVersion == -1:
            if PackageBOEType != 'MINIBIPPACKAGE' and MiniBIPInstallForceInstall != '1':
                print('Error: Your BOE package at location: ' + Step[1] + ' is not Mini BIP package')
                logger.error('Your BOE package at location: ' + Step[1] + ' is not Mini BIP package')
                return False
            CorrectStep.append(Step)
            return  CorrectStep
        if InstalledBOEVersion >= 0:
            if MiniBIPInstallForceInstall == '1':
                # BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType != 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep


                # BOE package version equals installed BOE version
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep


                #BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.error('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False
            if float(PackageBOEVersion) == InstalledBOEVersion:
                print('Warning: BOE already installed on your machine, step INSTALLMINIBIP will be skipped')
                logger.warning('BOE already installed on your machine, step INSTALLMINIBIP will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return  CorrectStep
            if float(PackageBOEVersion) != InstalledBOEVersion:
                print('Error: BOE already installed on your machine')
                logger.error('BOE already installed on your machine')
                return  False

    if Step[0].upper() == 'INSTALLFULLBOE':
        FullBOEInstallForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'FullBOEInstallForceInstall', '=')
        if ExOption != '':
            FullBOEInstallForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', ExOption, '=')
        if FullBOEInstallForceInstall != '0' and FullBOEInstallForceInstall != '1':
            print('Warning: Parameter FullBOEInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter FullBOEInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if FullBOEInstallForceInstall is False:
            print('Warning: No parameter FullBOEInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter FullBOEInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        PackageBOEVersion = GetBOEVersion(Step[1])
        PackageBOEType = GetBOEPackageType(Step[1])
        if PackageBOEVersion is False or PackageBOEType is False:
            return False
        if InstalledBOEVersion == -1:
            if PackageBOEType != 'FULLBOEPACKAGE' and FullBOEInstallForceInstall != '1':
                print('Error: Your BOE package at location: ' + Step[1] + ' is not full BOE package')
                logger.error('Your BOE package at location: ' + Step[1] + ' is not full BOE package')
                return False
            CorrectStep.append(Step)
            return  CorrectStep
        if InstalledBOEVersion >= 0:
            if FullBOEInstallForceInstall == '1':
                # BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType != 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep


                # BOE package version equals installed BOE version
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep


                #BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.error('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

            if float(PackageBOEVersion) == InstalledBOEVersion:
                print('Warning: BOE already installed on your machine, step INSTALLMINIBIP will be skipped')
                logger.error('BOE already installed on your machine, step INSTALLMINIBIP will be skipped')
                CorrectStep.warning(['SKIPSTEP',''])
                return  CorrectStep
            if float(PackageBOEVersion) != InstalledBOEVersion:
                print('Error: BOE already installed on your machine')
                logger.error('BOE already installed on your machine')
                return  False

    if Step[0].upper() == 'INSTALLBOE':
        PackageBOEVersion = GetBOEVersion(Step[1],1)
        PackageBOEType = GetBOEPackageType(Step[1],1)
        if PackageBOEVersion is False or PackageBOEType is False:
            print('Error; Error getting BOE package version or type')
            logger.info('Error; Error getting BOE package version or type')
            return False
        if PackageBOEType == 'MINIBIPPACKAGE' or PackageBOEType == 'MINIBIPPATCH':
            return GetCorrectStep(ProjectPath, ['INSTALLMINIBIP',Step[1]],InstalledBOEVersion,InstalledDSVersion,InstalledBOEType,'BOEInstallForceInstall')
        if PackageBOEType == 'FULLBOEPACKAGE' or PackageBOEType == 'FULLBOEPATCH':
            return GetCorrectStep(ProjectPath, ['INSTALLFULLBOE',Step[1]],InstalledBOEVersion,InstalledDSVersion,InstalledBOEType,'BOEInstallForceInstall')
        return False

    if Step[0].upper() == 'PATCHMINIBIP':
        MiniBIPPatchForcePatch = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'MiniBIPPatchForcePatch', '=')
        if ExOption != '':
            MiniBIPPatchForcePatch = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', ExOption, '=')
        if MiniBIPPatchForcePatch != '0' and MiniBIPPatchForcePatch != '1':
            print('Warning: Parameter MiniBIPPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter MiniBIPPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if MiniBIPPatchForcePatch is False:
            print('Warning: No parameter MiniBIPPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter MiniBIPPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        PackageBOEVersion = GetBOEVersion(Step[1])
        PackageBOEType = GetBOEPackageType(Step[1])
        if PackageBOEVersion is False or PackageBOEType is False:
            return False
        if InstalledBOEVersion == -1:
            print('Error: Cannot install a patch without first install a package')
            logger.error('Cannot install a patch without first install a package')
            return False
        if InstalledBOEVersion >= 0:
            if MiniBIPPatchForcePatch == '1':
                # BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.info('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType != 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep


                # BOE package version equals installed BOE version
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, step PATCHMINIBIP will be skipped')
                    logger.warning('According to your setup, step PATCHMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step PATCHMINIBIP will be skipped')
                    logger.warning('According to your setup, step PATCHMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step PATCHMINIBIP will be skipped')
                    logger.warning('According to your setup, step PATCHMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step PATCHMINIBIP will be skipped')
                    logger.warning('According to your setup, step PATCHMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step PATCHMINIBIP will be skipped')
                    logger.warning('According to your setup, step PATCHMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step PATCHMINIBIP will be skipped')
                    logger.warning('According to your setup, step PATCHMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep


                #BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.error('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

            if PackageBOEType != 'MINIBIPPATCH':
                print('Error: Your BOE package type is not Mini BIP patch')
                logger.error('Your BOE package type is not Mini BIP patch')
                return False
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE':
                print('Warning: Your installed Mini BIP package version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed Mini BIP package version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                print('According to your setup, will patch Mini BIP')
                logger.warning('According to your setup, will patch Mini BIP')
                CorrectStep.append(['PATCHMINIBIP',Step[1]])
                return CorrectStep
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE':
                print('Error: Your installed BOE is full BOE package, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                logger.error('Your installed BOE is full BOE package, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                return False
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH':
                print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                print('According to your setup, will patch Mini BIP')
                logger.warning('According to your setup, will patch Mini BIP')
                CorrectStep.append(['PATCHMINIBIP',Step[1]])
                return CorrectStep
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH':
                print('Error: Your installed BOE is full BOE patch, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                logger.error('Your installed BOE is full BOE patch, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                return False

            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE':
                print('Warning: Your installed Mini BIP package version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed Mini BIP package version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHMINIBIP will be skipped')
                logger.warning('According to your setup, Step PATCHMINIBIP will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE':
                print('Error: Your installed BOE is full BOE package, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                logger.error('Your installed BOE is full BOE package, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                return False
            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH':
                print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHMINIBIP will be skipped')
                logger.warning('According to your setup, Step PATCHMINIBIP will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH':
                print('Error: Your installed BOE is full BOE patch, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                logger.error('Your installed BOE is full BOE patch, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                return False

            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE':
                print('Warning: Your installed Mini BIP package version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed Mini BIP package version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHMINIBIP will be skipped')
                logger.warning('According to your setup, Step PATCHMINIBIP will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE':
                print('Error: Your installed BOE is full BOE package, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                logger.error('Your installed BOE is full BOE package, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                return False
            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH':
                print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHMINIBIP will be skipped')
                logger.warning('According to your setup, Step PATCHMINIBIP will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH':
                print('Error: Your installed BOE is full BOE patch, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                logger.error('Your installed BOE is full BOE patch, but your BOE Package type is Mini BIP patch, cannot patch a full BOE with Mini BIP patch')
                return False

    if Step[0].upper() == 'PATCHFULLBOE':
        FullBOEPatchForcePatch = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'FullBOEPatchForcePatch', '=')
        if ExOption != '':
            FullBOEPatchForcePatch = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', ExOption, '=')
        if FullBOEPatchForcePatch != '0' and FullBOEPatchForcePatch != '1':
            print('Warning: Parameter FullBOEPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter FullBOEPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if FullBOEPatchForcePatch is False:
            print('Warning: No parameter FullBOEPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter FullBOEPatchForcePatch in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        PackageBOEVersion = GetBOEVersion(Step[1])
        PackageBOEType = GetBOEPackageType(Step[1])
        if PackageBOEVersion is False or PackageBOEType is False:
            return False
        if InstalledBOEVersion == -1:
            print('Error: Cannot install a patch without first install a package')
            logger.error('Cannot install a patch without first install a package')
            return False
        if InstalledBOEVersion >= 0:
            if FullBOEPatchForcePatch == '1':
                # BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.warning('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.warning('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType != 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch Mini BIP')
                    logger.warning('According to your setup, will patch Mini BIP')
                    CorrectStep.append(['PATCHMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will patch full BOE')
                    logger.warning('According to your setup, will patch full BOE')
                    CorrectStep.append(['PATCHFULLBOE',Step[1]])
                    return CorrectStep


                # BOE package version equals installed BOE version
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, step INSTALLMINIBIP will be skipped')
                    logger.warning('According to your setup, step INSTALLMINIBIP will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep


                #BOE package version is higher than installed BOE version
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.error('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    logger.warning('According to your setup, will remove installed full BOE first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed Mini BIP patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    logger.warning('But your BOE Package type is full BOE package, according to your setup, will remove installed Mini BIP patch first, than install your full BOE package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Error: Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed Mini BIP patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is full BOE patch, cannot force install a patch without first install a package')
                    return False

                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP package version: ' + str(PackageBOEVersion))
                    print('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('According to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLMINIBIP',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'MINIBIPPATCH':
                    print('Error: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    logger.error('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your Mini BIP patch version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    logger.error('But your BOE Package type is Mini BIP patch, cannot force install a patch without first install a package')
                    return False
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPACKAGE':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE package version: ' + str(PackageBOEVersion))
                    print('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    logger.warning('But your BOE Package type is Mini BIP package, according to your setup, will remove installed full BOE patch first, than install your Mini BIP package')
                    CorrectStep = GetCorrectStep(ProjectPath,[ 'REMOVEBOE',''], InstalledBOEVersion, InstalledDSVersion, InstalledBOEType)
                    if CorrectStep is False:
                        return False
                    CorrectStep.append(['INSTALLFULLBOE',Step[1]])
                    return CorrectStep
                if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH' and PackageBOEType == 'FULLBOEPATCH':
                    print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                    print('Cannot force install a patch without first install a package')
                    logger.warning('Cannot force install a patch without first install a package')
                    return False

            if PackageBOEType != 'FULLBOEPATCH':
                print('Error: Your BOE package type is not full BOE patch')
                logger.error('Your BOE package type is not full BOE patch')
                return False
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE':
                print('Error: Your installed BOE is Mini BIP package, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                logger.error('Your installed BOE is Mini BIP package, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                return False
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE':
                print('Warning: Your installed full BOE package version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed full BOE package version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                print('According to your setup, will patch full BOE')
                logger.warning('According to your setup, will patch full BOE')
                CorrectStep.append(['PATCHFULLBOE',Step[1]])
                return CorrectStep
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH':
                print('Error: Your installed BOE is Mini BIP patch, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                logger.error('Your installed BOE is Mini BIP patch, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                return False
            if float(PackageBOEVersion) > InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH':
                print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is lower than your full BOE patch version: ' + str(PackageBOEVersion))
                print('According to your setup, will patch full BOE')
                logger.warning('According to your setup, will patch full BOE')
                CorrectStep.append(['PATCHFULLBOE',Step[1]])
                return CorrectStep

            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE':
                print('Error: Your installed BOE is Mini BIP package, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                logger.error('Your installed BOE is Mini BIP package, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                return False
            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE':
                print('Warning: Your installed full BOE package version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed full BOE package version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHFULLBOE will be skipped')
                logger.warning('According to your setup, Step PATCHFULLBOE will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH':
                print('Error: Your installed BOE is Mini BIP patch, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                logger.error('Your installed BOE is Mini BIP patch, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                return False
            if float(PackageBOEVersion) == InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH':
                print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' equals your full BOE patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHFULLBOE will be skipped')
                logger.warning('According to your setup, Step PATCHFULLBOE will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep

            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPACKAGE':
                print('Error: Your installed BOE is Mini BIP package, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                logger.error('Your installed BOE is Mini BIP package, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                return False
            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPACKAGE':
                print('Warning: Your installed full BOE package version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed full BOE package version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHFULLBOE will be skipped')
                logger.warning('According to your setup, Step PATCHFULLBOE will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'MINIBIPPATCH':
                print('Error: Your installed BOE is Mini BIP patch, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                logger.error('Your installed BOE is Mini BIP patch, but your BOE Package type is full BOE patch, cannot patch a Mini BIP with full BOE patch')
                return False
            if float(PackageBOEVersion) < InstalledBOEVersion and InstalledBOEType == 'FULLBOEPATCH':
                print('Warning: Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                logger.warning('Your installed full BOE patch version: ' + str(InstalledBOEVersion) + ' is higher than your full BOE patch version: ' + str(PackageBOEVersion))
                print('According to your setup, Step PATCHFULLBOE will be skipped')
                logger.warning('According to your setup, Step PATCHFULLBOE will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep

    if Step[0].upper() == 'PATCHBOE':
        PackageBOEVersion = GetBOEVersion(Step[1],1)
        PackageBOEType = GetBOEPackageType(Step[1],1)
        if PackageBOEVersion is False or PackageBOEType is False:
            print('Error: Error getting BOE package version or type')
            logger.error('Error getting BOE package version or type')
            return False
        if PackageBOEType == 'MINIBIPPACKAGE' or PackageBOEType == 'MINIBIPPATCH':
            return GetCorrectStep(ProjectPath, ['PATCHMINIBIP',Step[1]],InstalledBOEVersion,InstalledDSVersion,InstalledBOEType,'BOEPatchForcePatch')
        if PackageBOEType == 'FULLBOEPACKAGE' or PackageBOEType == 'FULLBOEPATCH':
            return GetCorrectStep(ProjectPath, ['PATCHFULLBOE',Step[1]],InstalledBOEVersion,InstalledDSVersion,InstalledBOEType,'BOEPatchForcePatch')
        return False

    if Step[0].upper() == 'INSTALLDS':
        DSInstallForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'DSInstallForceInstall', '=')
        if DSInstallForceInstall != '0' and DSInstallForceInstall != '1':
            print('Warning: Parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if DSInstallForceInstall is False:
            print('Warning: No parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        PackageDSVersion = GetDSVersion(Step[1])
        if PackageDSVersion is False:
            return False
        if DSInstallForceInstall != '1':
            if InstalledBOEVersion == -1:
                if InstalledDSVersion == -1:
                    CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                    return CorrectStep
                if InstalledDSVersion == float(PackageDSVersion):
                    print('Warning: DS with same version already installed on your machine, step INSTALLDS will be skipped')
                    logger.warning('DS with same version already installed on your machine, step INSTALLDS will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if InstalledDSVersion != float(PackageDSVersion):
                    print('Error: DS already installed on your machine')
                    logger.error('DS already installed on your machine')
                    return False
            if InstalledBOEVersion >= 0:
                if InstalledDSVersion == -1:
                    CorrectStep.append(Step)
                    return CorrectStep
                if InstalledDSVersion == float(PackageDSVersion):
                    print('Warning: DS with same version already installed on your machine, step INSTALLDS will be skipped')
                    logger.warning('DS with same version already installed on your machine, step INSTALLDS will be skipped')
                    CorrectStep.append(['SKIPSTEP',''])
                    return CorrectStep
                if InstalledDSVersion != float(PackageDSVersion):
                    print('Error: DS already installed on your machine')
                    logger.error('DS already installed on your machine')
                    return False
        if DSInstallForceInstall == '1':
            if InstalledBOEVersion == -1:
                if InstalledDSVersion == -1:
                    CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                if InstalledDSVersion >= 0:
                    if float(PackageDSVersion) > InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will upgrade DS')
                        logger.warning('According to your setup, will upgrade DS')
                        CorrectStep.append(['UPGRADEDS',Step[1]])
                    if float(PackageDSVersion) == InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, step INSTALLDS will be skipped')
                        logger.warning('According to your setup, step INSTALLDS will be skipped')
                        CorrectStep.append(['SKIPSTEP',''])
                    if float(PackageDSVersion) < InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will remove installed DS first, than install your DS package')
                        logger.warning('According to your setup, will remove installed DS first, than install your DS package')
                        CorrectStep.append(['REMOVEDS',''])
                        CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                return CorrectStep
            if InstalledBOEVersion >= 0:
                if InstalledDSVersion == -1:
                    CorrectStep.append(Step)
                if InstalledDSVersion >= 0:
                    if float(PackageDSVersion) > InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will upgrade DS')
                        logger.warning('According to your setup, will upgrade DS')
                        CorrectStep.append(['UPGRADEDS',Step[1]])
                    if float(PackageDSVersion) == InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, step INSTALLDS will be skipped')
                        logger.warning('According to your setup, step INSTALLDS will be skipped')
                        CorrectStep.append(['SKIPSTEP',''])
                    if float(PackageDSVersion) < InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will remove installed DS first, than install your DS package')
                        logger.warning('According to your setup, will remove installed DS first, than install your DS package')
                        CorrectStep.append(['REMOVEDS',''])
                        CorrectStep.append(Step)
                return CorrectStep

    if Step[0].upper() == 'SKIPINSTALLDS':
        DSInstallForceInstall = GetValueFromFile(ProjectPath + '\\setup\\Cerberus\\Setup.ini', 'DSInstallForceInstall', '=')
        if DSInstallForceInstall != '0' and DSInstallForceInstall != '1':
            print('Warning: Parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
            logger.warning('Parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini must be 0 or 1, will use default value 0')
        if DSInstallForceInstall is False:
            print('Warning: No parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
            logger.warning('No parameter DSInstallForceInstall in file: ' + ProjectPath + '\\setup\\Cerberus\\Setup.ini, will use default value 0')
        PackageDSVersion = GetDSVersion(Step[1])
        if PackageDSVersion is False:
            return False
        if DSInstallForceInstall != '1':
            if InstalledDSVersion == -1:
                CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                return CorrectStep
            if InstalledDSVersion == float(PackageDSVersion):
                print('Warning: DS with same version number already installed on your machine, step SKIPINSTALLDS will be skipped')
                logger.warning('DS with same version number already installed on your machine, step SKIPINSTALLDS will be skipped')
                CorrectStep.append(['SKIPSTEP',''])
                return CorrectStep
            if InstalledDSVersion != float(PackageDSVersion):
                print('Error: DS already installed on your machine')
                logger.error('DS already installed on your machine')
                return False
        if DSInstallForceInstall == '1':
            if InstalledBOEVersion == -1:
                if InstalledDSVersion == -1:
                    CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                if InstalledDSVersion >= 0:
                    if float(PackageDSVersion) > InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will upgrade DS')
                        logger.warning('According to your setup, will upgrade DS')
                        CorrectStep.append(['UPGRADEDS',Step[1]])
                    if float(PackageDSVersion) == InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, step INSTALLDS will be skipped')
                        logger.warning('According to your setup, step INSTALLDS will be skipped')
                        CorrectStep.append(['SKIPSTEP',''])
                    if float(PackageDSVersion) < InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will remove installed DS first, than install your DS package')
                        logger.warning('According to your setup, will remove installed DS first, than install your DS package')
                        CorrectStep.append(['REMOVEDS',''])
                        CorrectStep.append(['SKIPINSTALLDS',Step[1]])
                return CorrectStep
            if InstalledBOEVersion >= 0:
                if InstalledDSVersion == -1:
                    CorrectStep.append(Step)
                if InstalledDSVersion >= 0:
                    if float(PackageDSVersion) > InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is lower than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will upgrade DS')
                        logger.warning('According to your setup, will upgrade DS')
                        CorrectStep.append(['UPGRADEDS',Step[1]])
                    if float(PackageDSVersion) == InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' equals your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, step INSTALLDS will be skipped')
                        logger.warning('According to your setup, step INSTALLDS will be skipped')
                        CorrectStep.append(['SKIPSTEP',''])
                    if float(PackageDSVersion) < InstalledDSVersion:
                        print('Warning: Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        logger.warning('Your installed DS version: ' + str(InstalledDSVersion) + ' is higher than your DS package version: ' + str(PackageDSVersion))
                        print('According to your setup, will remove installed DS first, than install your DS package')
                        logger.warning('According to your setup, will remove installed DS first, than install your DS package')
                        CorrectStep.append(['REMOVEDS',''])
                        CorrectStep.append(Step)
                return CorrectStep

#Function: Delete duplicate steps
def SimplifySteps(Steps):
    StepCount = 0
    DeleteElement = []
    while StepCount < len(Steps) - 1:
        if Steps[StepCount] == Steps[StepCount + 1]:
            DeleteElement.append(StepCount)
        StepCount = StepCount + 1
    DeleteElementCount = 0
    while DeleteElementCount < len(DeleteElement):
        del Steps[DeleteElement[DeleteElementCount]]
        DeleteElementCount = DeleteElementCount + 1
    return Steps

#Function: Check step success or not
def CheckStepStatus(ProjectPath, Step):
    if len(Step) != 2:
        print(Step)
        logger.info(Step)
        print('Error: Your step do not meet the step format')
        logger.error('Your step do not meet the step format')
        return False
    if Step[0].upper() == 'SKIPSTEP':
        return True
    FileStatus = os.path.isfile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if FileStatus is False:
        print('Error: Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Cerberus summon scroll missing spell! spell Name: setup\\Cerberus\\SupportedSteps.ini')
        return False
    SupportedStepsList = ReadFromFile(ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
    if SupportedStepsList is False:
        print('Error: Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        logger.error('Error reading from file: ' + ProjectPath + '\\setup\\Cerberus\\SupportedSteps.ini')
        return False
    FoundStep = False
    for SupportedStep in SupportedStepsList:
        if Step[0].upper() == SupportedStep.upper():
            FoundStep = True
    if FoundStep is False:
        print('Error: Cerberus current do not support your input step: ' + Step[0])
        logger.error('Cerberus current do not support your input step: ' + Step[0])
        return False

    if Step[0].upper() == 'REMOVEDS':
        if CheckDSVersion(ProjectPath, 1) == -1:
            return True
        else:
            return False

    if Step[0].upper() == 'REMOVEFULLBOEPACKAGE':
        if CheckBOEType(ProjectPath, 1) != 'FULLBOEPACKAGE':
            return True
        else:
            return False

    if Step[0].upper() == 'REMOVEMINIBIPPACKAGE':
        if CheckBOEType(ProjectPath, 1) != 'MINIBIPPACKAGE':
            return True
        else:
            return False

    if Step[0].upper() == 'REMOVEMINIBIPPATCH':
        InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
        if InstalledBOEList is False:
            print('Error: Error getting installed BOE list')
            logger.error('Error getting installed BOE list')
            return False
        InstalledBOECount = 0
        while InstalledBOECount < len(InstalledBOEList):
            if InstalledBOEList[InstalledBOECount][2].find(Step[1]) != -1:
                return False
            InstalledBOECount = InstalledBOECount + 1
        return True

    if Step[0].upper() == 'REMOVEFULLBOEPATCH':
        InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
        if InstalledBOEList is False:
            print('Error: Error getting installed BOE list')
            logger.error('Error getting installed BOE list')
            return False
        InstalledBOECount = 0
        while InstalledBOECount < len(InstalledBOEList):
            if InstalledBOEList[InstalledBOECount][2].find(Step[1]) != -1:
                return False
            InstalledBOECount = InstalledBOECount + 1
        return True

    if Step[0].upper() == 'INSTALLDS' or Step[0].upper() == 'SKIPINSTALLDS' or Step[0].upper() == 'UPGRADEDS':
        if CheckDSVersion(ProjectPath, 1) == GetDSVersion(Step[1], 1) and GetDSVersion(Step[1], 1) is not False:
            return True
        else:
            return False

    if Step[0].upper() == 'INSTALLMINIBIP':
        if CheckBOEVerison(ProjectPath, 1) == GetBOEVersion(Step[1], 1) and GetBOEVersion(Step[1], 1) is not False and CheckBOEType(ProjectPath, 1) == 'MINIBIPPACKAGE':
            return True
        else:
            return False

    if Step[0].upper() == 'INSTALLFULLBOE':
        if CheckBOEVerison(ProjectPath, 1) == GetBOEVersion(Step[1], 1) and GetBOEVersion(Step[1], 1) is not False and CheckBOEType(ProjectPath, 1) == 'FULLBOEPACKAGE':
            return True
        else:
            return False

    if Step[0].upper() == 'PATCHMINIBIP':
        InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
        if InstalledBOEList is False:
            print('Error: Error getting installed BOE list')
            logger.error('Error getting installed BOE list')
            return False
        InstalledBOECount = 0
        while InstalledBOECount < len(InstalledBOEList):
            if InstalledBOEList[InstalledBOECount][1].find(GetBOEVersion(Step[1], 1)) != -1:
                return True
            InstalledBOECount = InstalledBOECount + 1
        return False

    if Step[0].upper() == 'PATCHFULLBOE':
        InstalledBOEList = CheckInstalledBOEList(ProjectPath, 1)
        if InstalledBOEList is False:
            print('Error: Error getting installed BOE list')
            logger.error('Error getting installed BOE list')
            return False
        InstalledBOECount = 0
        while InstalledBOECount < len(InstalledBOEList):
            if InstalledBOEList[InstalledBOECount][1].find(GetBOEVersion(Step[1], 1)) != -1:
                return True
            InstalledBOECount = InstalledBOECount + 1
        return False

#Function: Print machine deployment status
def PrintMachineInstallationStatus(ProjectPath):
    print('Your current machine status is:')
    logger.info('Your current machine status is:')
    #InstalledBOEVersion = CheckBOEVerison(ProjectPath, 1)
    InstalledBOEInfoList = CheckInstalledBOEList(ProjectPath, 1)
    if InstalledBOEInfoList is False:
        print('Error: Error getting installed BOE list')
        logger.error('Error getting installed BOE list')
    else:
        if InstalledBOEInfoList == []:
            print('BOE is not installed on your machine')
            logger.info('BOE is not installed on your machine')
        else:
            for InstalledBOEInfo in InstalledBOEInfoList:
                print('Installed BOE: ' + InstalledBOEInfo[0] + ' version: ' + InstalledBOEInfo[1])
                logger.info('Installed BOE: ' + InstalledBOEInfo[0] + ' version: ' + InstalledBOEInfo[1])

    InstalledDSVersion = CheckDSVersion(ProjectPath, 1)
    if InstalledDSVersion is False:
        print('Error: Cerberus get error when trying to get installed DS version')
        logger.error('Cerberus get error when trying to get installed DS version')
    else:
        if InstalledDSVersion == -1:
            print('DS is not installed on your machine')
            logger.info('DS is not installed on your machine')
        if InstalledDSVersion != -1:
            print('Installed DS version: ' + InstalledDSVersion)
            logger.info('Installed DS version: ' + InstalledDSVersion)
