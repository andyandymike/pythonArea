__author__ = 'I067382'


import GlobalVar
from BasicClass import *
from BasicFunc import *


class SybaseASE(DB):
    def __init__(self):
        DB.__init__(self, GlobalVar.attributePath + '\\' + GlobalVar.sybaseASEJsonFileName)

    def install(self, version, type):
        dbAttributes = DB.getDBAttribute(self)
        for dbAttribute in dbAttributes:
            if dbAttribute['Version'] == version and dbAttribute['InstallationType'] == type:
                rspFileName = dbAttribute['RspFile']
                installationFolder = '\\' + dbAttribute['Version'] + '\\' + dbAttribute['InstallationPackage']

                rspFileLoc = GlobalVar.rspFilePath + '\\' + rspFileName
                installationPackagePath = GlobalVar.sybaseASEInstallationPackagesPath + installationFolder

                if version == '16' and type == 'Client':
                    returnCode = self.installSybaseASE16Client(installationPackagePath, rspFileLoc)
                    print(returnCode)

    def installSybaseASE16Client(self, installationPackagePath, rspFileLoc):
        installCommand = '\"' + installationPackagePath + '\\setupConsole.exe\" -f ' + '\"' + rspFileLoc + '\"' + ' -i silent -DAGREE_TO_SAP_LICENSE=true'
        returnCode = runWinShellCommand(installCommand)
        return returnCode
