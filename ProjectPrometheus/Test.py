__author__ = 'I067382'


import SybaseASE
import GlobalVar
from BasicFunc import *


testdb = SybaseASE.SybaseASE()
#print(testdb.install('16', 'Client'))
print(getInstallConfig(GlobalVar.installConfigFileLoc))
