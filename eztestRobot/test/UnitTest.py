from OSHelper import *
from bin import summary
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
    gf = os.path.join(testRoot, 'g.txt')
    wf = os.path.join(testRoot, 'w.txt')
    print(diff_unordered_files(gf, wf))


def testSplitParams():
    print(utils.splitParams(
        '''-V'HANA 1.x' -V 'HANA 1.x'"-KspS1 -l${UDS_WORK}/${JOBNAME}.log -z${UDS_WORK}/${JOBNAME}.txt"'''))


def testReplaceEnv():
    cmd = "al_engine -Kversion'hana 1.x' -shana -v " + "-kspS1" + " -lc/build/log -ec/build/error"
    print(utils.shlex.split("sh -c \"%s\"" % cmd.replace('\"', '\\\"')))
    print(utils.splitParams("sh -c \"%s\"" % cmd.replace('\"', '\\\"')))


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


def testSummary():
    summary.sum(testRoot, 'HANA_Pipe_File_Options_output.xml')


def testGrep():
    export_env('TEST', "i'm testing grep")
    print(os.path.expandvars('%TEST%'))


def testLine():
    gf = os.path.join(testRoot, 'g.txt')
    with open(gf, 'rU') as f:
        print(len(f.readlines()))


def testShellCommand():
    export_env("test", "hello")
    shell_command("echo %test%", True, False)


def testUseShellCommand():
    cmd = "\$(ls -ld \${runtest}/goldlog/LINEITEM30A.json \| awk '{print int(\$5/1024)}')"
    print(utils.use_shell_command(cmd))
    cmd = "\${test}"
    print(utils.use_shell_command(cmd))
    cmd = "test"
    print(utils.use_shell_command(cmd))


if __name__ == '__main__':
    testUseShellCommand()
