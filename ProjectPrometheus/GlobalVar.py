__author__ = 'I067382'


import os


rootPath = os.path.abspath('.')
setupFolder = '\\Setup'
attributeFolder = '\\DBAttribute'
installationPackageFolder = '\\InstallationPackage'
rspFileFolder = '\\RspFile'
installConfigFileName = 'installConfig.json'

attributePath = rootPath + setupFolder + attributeFolder
rspFilePath = rootPath + setupFolder + rspFileFolder
installConfigFileLoc = rootPath + setupFolder + '\\' + installConfigFileName


sybaseASEJsonFileName = 'sybase_ase.json'
sybaseASEInstallationPackagesFolder = '\\SYBASE_ASE'
sybaseASEInstallationPackagesPath = rootPath + setupFolder + installationPackageFolder + sybaseASEInstallationPackagesFolder