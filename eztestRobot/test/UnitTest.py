from OSHelper import *
from bin import utils
import os
import subprocess
import re

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
    gf = os.path.join(testRoot, 'partition_df_patch.atl')
    wf = os.path.join(testRoot, 'wpartition_df_patch.atl')
    print(diff_unordered_files(gf, wf))

def testSplitParams():
    print(utils.splitParams('''-V'HANA 1.x' -V 'HANA 1.x'"-KspS1 -l${UDS_WORK}/${JOBNAME}.log -z${UDS_WORK}/${JOBNAME}.txt"'''))

def testReplaceEnv():
    cmd = "al_engine -Kversion'hana 1.x' -shana -v "+"-kspS1"+" -lc/build/log -ec/build/error"
    print(utils.shlex.split("sh -c \"%s\"" % cmd.replace('\"','\\\"')))
    print(utils.splitParams("sh -c \"%s\"" % cmd.replace('\"','\\\"')))


if __name__ == '__main__':
    testDiff()