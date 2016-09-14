__author__ = 'I067382'


import SybaseASE
import GlobalVar
from BasicFunc import *


installConfigs = getInstallConfig(GlobalVar.installConfigFileLoc)

for installConfig in installConfigs:
    if installConfig['DBName'] == 'SYBASE_ASE':
        installSybaseASE = SybaseASE.SybaseASE()
        installSybaseASE.install(installConfig['Version'], installConfig['InstallationType'])
