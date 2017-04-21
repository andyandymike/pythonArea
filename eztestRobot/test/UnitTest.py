from OSHelper import *
from bin import utils
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
    gf = os.path.join(testRoot, 'gALL_TDP_42_03_Query_After_TDP.out')
    wf = os.path.join(testRoot, 'wALL_TDP_42_03_Query_After_TDP.out')
    print(diff_unordered_files(gf, wf))

def testSplitParams():
    print(utils.splitParams('''-V'HANA 1.x' -V 'HANA 1.x'"-KspS1 -l${UDS_WORK}/${JOBNAME}.log -z${UDS_WORK}/${JOBNAME}.txt"'''))

def testReplaceEnv():
    print(utils.splitParams("\"-k'hana 1.x' -s test \"-lkkk -pppp\"\""))


if __name__ == '__main__':
    testReplaceEnv()