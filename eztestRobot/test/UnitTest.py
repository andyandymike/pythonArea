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
    gf = os.path.join('Y:\\landy\\EZTEST\diqa\\generic\\google_big_query\\gbq_reader\\goldlog', 'tcase033.xml')
    wf = os.path.join(testRoot, 'gBJ_054.out')
    print(diff_unordered_files(gf, wf))

def testSplitParams():
    print(utils.splitParams('''-V'HANA 1.x' -V 'HANA 1.x'"-KspS1 -l${UDS_WORK}/${JOBNAME}.log -z${UDS_WORK}/${JOBNAME}.txt"'''))

def testReplaceEnv():
    cmd = "al_engine -Kversion'hana 1.x' -shana -v "+"-kspS1"+" -lc/build/log -ec/build/error"
    print(utils.shlex.split("sh -c \"%s\"" % cmd.replace('\"','\\\"')))
    print(utils.splitParams("sh -c \"%s\"" % cmd.replace('\"','\\\"')))

def testReMatch():
    reg = re.compile('2\\;44\\;10\\;2003\\;27\\;300\\;(.*?)\\;(.*?)')
    m = reg.match('2;44;10;2003;27;300;2017.04.24 23:45:07;1900.01.01 23:45:07')
    if m:
        print(m.group(1))
        print(m.group(2))

def testReSplit():
    reg = re.compile('2\\;44\\;10\\;2003\\;27\\;300\\;.*?\\;.*?')
    s = reg.split('2;44;10;2003;27;300;2017.04.24 23:45:07;1900.01.01 23:45:07')
    print(s)

def testSorted():
    file = os.path.join(testRoot, 'gST_089.out')
    with open(file, 'r') as f:
        sortedfile = sorted(f.readlines())
    print(sortedfile[1])

def testGetFileSize():
    f = os.path.join('Y:\\landy\\EZTEST\diqa\\generic\\google_big_query\\gbq_reader\\goldlog', 'tcase033.xml')
    print(os.stat(f).st_size - 872888511L)

def testGetCheckSum():
    f = os.path.join('Y:\\landy\\EZTEST\diqa\\generic\\google_big_query\\gbq_reader\\goldlog', 'tcase033.xml')
    print(utils.checksum(f))


if __name__ == '__main__':
    testDiff()