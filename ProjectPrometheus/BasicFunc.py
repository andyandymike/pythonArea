__author__ = 'I067382'


import os
import json
import subprocess


def getJsonObject(jsonFileLoc):
    if os.path.isfile(jsonFileLoc) is True:
        jsonFile = open(jsonFileLoc, 'r')
        try:
            jsonObject = json.loads(jsonFile.read())
            return jsonObject
        finally:
            jsonFile.close()

def runWinShellCommand(command):
    ps = subprocess.Popen(command, shell=True)
    ps.wait()
    return ps.returncode

def getInstallConfig(installConfigFileLoc):
    installConfigObject = getJsonObject(installConfigFileLoc)
    installConfig = []
    installConfigNotLatest = []
    installConfigNotInstall = []
    installConfigIntallAll = []
    installConfigIntallAllLatest = []
    for dbConfigNum in range(len(installConfigObject)):
        currentDB = list(installConfigObject)[dbConfigNum]
        currentDBConfigs = installConfigObject[currentDB]
        #print(currentDBConfigs)
        if currentDB != 'InstallAll':
            for currentDBConfig in currentDBConfigs:
                if currentDBConfig['Install'] == 'True' and currentDBConfig['IsLatest'] == 'True':
                    installConfig.append(currentDBConfig)
                if currentDBConfig['Install'] == 'True' and currentDBConfig['IsLatest'] == 'False':
                    installConfigNotLatest.append(currentDBConfig)
                if currentDBConfig['Install'] == 'False':
                    installConfigNotInstall.append(currentDBConfig)
        if currentDB == 'InstallAll':
            for currentDBConfig in currentDBConfigs:
                if currentDBConfig['Install'] == 'True' and currentDBConfig['Version'] != 'Latest':
                    installConfigIntallAll.append(currentDBConfig)
                if currentDBConfig['Install'] == 'True' and currentDBConfig['Version'] == 'Latest':
                    installConfigIntallAllLatest.append(currentDBConfig)

    if len(installConfigIntallAll) + len(installConfigIntallAllLatest) == 0:
        return installConfig + installConfigNotLatest

    for installAllConfig in installConfigIntallAll:
        for DBConfig in installConfigNotLatest + installConfigNotInstall:
            if installAllConfig['InstallationType'] == DBConfig['InstallationType']:
                installConfig.append(DBConfig)

    for installAllConfigLatest in installConfigIntallAllLatest:
        for DBConfig in installConfigNotInstall:
            if installAllConfigLatest['InstallationType'] == DBConfig['InstallationType'] and DBConfig['IsLatest'] == 'True':
                installConfig.append(DBConfig)

    return installConfig