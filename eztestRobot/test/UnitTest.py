from OSHelper import *
from bin import Converter
import os
import subprocess

root = os.path.abspath('.')
testRoot = os.path.join(root, 'test')

def testImportATL():
    atl = os.path.join(testRoot, 'ezTest_hana_ansijoin_Datastore.atl')
    export_env('IMPORT', 'FALSE')
    import_atl(atl)


def testProcessOut():
    process = subprocess.Popen('echo hello', stdout=subprocess.PIPE, shell=True)
    status = process.communicate()[0].strip()
    rc = process.returncode
    print(status)

def testDiff():
    gf = os.path.join(testRoot, 'g.txt')
    wf = os.path.join(testRoot, 'w.txt')
    print(diff_unordered_files(gf, wf))


if __name__ == '__main__':
    shell_command('echo hello')