# -*- coding: utf-8 -*-

from OSHelper import *
from bin import summary
from bin import utils
import os
import subprocess
import re
import ConfigParser
import io
from bin import Converter
from timeit import Timer

root = os.path.abspath('.')
testRoot = os.path.join(root, '')


def testImportATL():
    atl = os.path.join(testRoot, 'test.atl')
    export_env('test', '%netezza 7.5%')
    import_atl(atl)


def testSubvalue2():
    atl = os.path.join(testRoot, 'test.atl')
    out = os.path.join(testRoot, 'ttest.atl')
    export_env('test', '你好')
    utils.subvalue2(atl, out)


def testProcessOut():
    process = subprocess.Popen('echo hello', stdout=subprocess.PIPE, shell=True)
    status = process.communicate()[0].strip()
    rc = process.returncode
    print(status)


def testDiff():
    gf = os.path.join(testRoot, 'json_goldlog.json')
    wf = os.path.join(testRoot, 'json.json')
    print(diff_unordered_files(gf, wf))


def testDiff_big():
    gf = os.path.join(testRoot, '1coreb')
    wf = os.path.join(testRoot, '2coreb')
    print(diff_unordered_files(gf, wf))


def testDiff_pre():
    gf = os.path.join(testRoot, 'gb.out')
    wf = os.path.join(testRoot, 'wb.out')
    print(utils.diff_unordered_files_pre(gf, wf))


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
    export_env('DS_BUILD', 'SAP Data Services Engine Version 14.2.9.1541')
    summary.sum(testRoot, 'gbq_reader_output.xml')


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


def testSqlite():
    con = sqlite3.connect(":memory:")
    con.execute('''CREATE TABLE TEST
                   (ID INT PRIMARY KEY     NOT NULL,
                   NAME            TEXT    NOT NULL,
                   AGE             INT     NOT NULL)''')
    con.execute('''INSERT INTO TEST (ID,NAME,AGE)
                   VALUES (1, 'Paul', 32)''')
    for line in con.execute('''SELECT * FROM TEST'''):
        print(line)


def testBifFileMaker():
    input = os.path.join(testRoot, '1core')
    output = os.path.join(testRoot, '1coreb')
    utils.bigFileMaker(input, output, 4)
    input = os.path.join(testRoot, '2core')
    output = os.path.join(testRoot, '2coreb')
    utils.bigFileMaker(input, output, 4)


def testReadConfig():
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    content = '''[test] t1 = 1'''
    config.readfp(io.BytesIO(content))
    print(config.get('test', 't1'))


def testTest():
    #os.environ['ICC_PROJECT_NAME'] = 'ICCMats_mssql_1'
    gf = os.path.join(testRoot, 'zion_hd-g.txt')
    wf = os.path.join(testRoot, 'zion_hd_sort-w.txt')
    print(test(gf, wf))


def testadiff():
    gf = os.path.join(testRoot, 'g.txt')
    wf = os.path.join(testRoot, 'w.txt')
    print(test(gf, wf))
    gf = os.path.join(testRoot, 'english_document_tc24_out-g-n')
    wf = os.path.join(testRoot, 'english_document_tc24_out-w')
    print(test(gf, wf))
    with open(r'C:\Users\i067382\PycharmProjects\eztestRobot\test\obg', 'w') as g:
        for i in range(80646):
            g.write(str(i) + 'xxxxxxxxxa\n')
    with open(r'C:\Users\i067382\PycharmProjects\eztestRobot\test\obw', 'w') as g:
        for i in range(80646):
            g.write(str(i) + 'xxxxxxxxxx\n')
    gf = os.path.join(testRoot, 'obg')
    wf = os.path.join(testRoot, 'obw')
    print(test(gf, wf))


def testConverter():
    export_env('RUNTYPE', 'FIRST-DELTA')
    export_env('LOADTYPE', "'DELTA'")
    export_env('G_SDATE', "'2007.07.01'")
    export_env('G_EDATE', "'2007.12.31'")
    export_env('EXECUTEJOB', 'General_Ledger_New_Load_SAP')
    export_env('TESTSUITE_COMPARES', '!call Compares_Files')
    export_env('TESTSUITE_INITIALIZE_DB', '!call Initialize_DB')
    Converter.converter(root, 'testcase')

def createTestcase():
    file = os.path.join(testRoot, 'output.txt')
    with open(file, 'w') as f:
        for i in range(49):
            if i < 10:
                f.write('!testcase voraodbc00{}\n'.format(i))
                f.write('!sh export JOBNAME=voraodbc00{}\n'.format(i))
            else:
                f.write('!testcase voraodbc0{}\n'.format(i))
                f.write('!sh export JOBNAME=voraodbc0{}\n'.format(i))
            f.write('!sh eim_launcher.sh ${JOBNAME}\n')
            f.write('#!expect no *Failed*\n')
            f.write('#!sh adiff ${runtest}/goldlog/${JOBNAME}.out ${DS_WORK}/${JOBNAME}.out\n')
            f.write('!endtestcase\n')
            f.write('\n')

if __name__ == '__main__':
    t1 = Timer("testTest()", "from __main__ import testTest")
    print t1.timeit(1)
    # t2 = Timer("testDiff_big()", "from __main__ import testDiff_big")
    # print t2.timeit(1)
    # testDecFunc2("andy")
    pass
