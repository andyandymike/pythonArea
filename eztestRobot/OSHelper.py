# to work with jython
from __future__ import with_statement

import os
import re
import glob
import subprocess
import difflib
import shlex
import hashlib

from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

__all__ = ['shell_command', 'export_env', 'change_working_directory', 'remove_wildcard_files', 'import_atl',
           'diff_unordered_files', 'replace_env', 'eim_launcher']

''' Use replace_env_str to workaround shell expansion '''


def replace_env_str(s):
    ns = os.path.expandvars(s)
    regex = re.compile(r'`(.*)`')
    it = regex.finditer(ns)
    for match in it:
        cmd = "sh -c \"%s\"" % match.group(1).replace(r'"', r'\"')
        ns = ns.replace(match.group(0), command_output(cmd))
    return ns


def command_output(cmd):
    # logger.warn('RUN: %s' % cmd)
    cmd = shlex.split(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = process.communicate()[0].strip()
    # logger.warn('RESULT: %s' % out)
    return out


def use_shell(cmd):
    cmd = cmd.strip()
    re_grep = re.compile(r'grep\s.*')
    m = re_grep.match(cmd)
    if m:
        return True
    else:
        return False


def shell_command(cmd, printOutput=True):
    useShell = use_shell(cmd)
    if not useShell:
        cmd = replace_env_str(cmd)
        # to get around shell problem under cygwin
        cmd = "sh -c \"%s\"" % cmd.replace(r'"', r'\"')
        cmd = shlex.split(cmd)

    logger.info('RUN: %s' % cmd, also_console=printOutput)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, shell=useShell)
    status = process.communicate()[0].strip()
    rc = process.returncode
    if rc != 0 or status != '' or printOutput:
        logger.info("Command exit code: %s" % rc, also_console=printOutput)
        logger.info("Command output: %s" % status, also_console=printOutput)
    return status


def export_env(key, val):
    val = replace_env_str(val)
    os.environ[key] = val


def get_env(key):
    key = replace_env_str(key)
    value = os.environ.get(key)
    return '' if value is None else value


def change_working_directory(wd):
    wd = replace_env_str(wd)
    os.chdir(wd)


def remove_wildcard_files(dir, fn):
    dir = replace_env_str(dir)
    fn = replace_env_str(fn)
    path = os.path.join(dir, fn)
    for f in glob.glob(path):
        os.remove(f)


def eim_launcher(jobname, *args):
    al_engine_param = get_env('al_engine_param')
    UDS_WORK = get_env('UDS_WORK')
    SYSPROF = get_env('SYSPROF')
    # al_engine ${al_engine_param} -s$JOBNAME -Ksp$SYSPROF $JOB_EXE_OPT $JOB_EXE_OPT2 -l${UDS_WORK}/$JOBNAME.log -t${UDS_WORK}/$JOBNAME.err
    cmd = ['al_engine', al_engine_param, '-s' + jobname, '-Ksp' + SYSPROF]
    cmd.append('-l' + UDS_WORK + '/' + jobname + '.log')
    cmd.append('-t' + UDS_WORK + '/' + jobname + '.err')
    jobexeoption = ''
    for arg in args:
        cmd.append(arg)
        jobexeoption += arg + ' '
    m_jobname = re.compile(r'\$\{(\w+)\}')
    m = m_jobname.match(jobname)
    if m:
        runjob = get_env(m.group(1))
    else:
        runjob = jobname

    logger.info(' ', also_console=True)
    logger.info('====================================================', also_console=True)
    logger.info('==  Job Executed on Server   ==', also_console=True)
    logger.info(' Job Server Host : %s' % get_env('JOBSERVERHOST'), also_console=True)
    logger.info('      Job Server : %s' % get_env('JOBSERVERNAME'), also_console=True)
    logger.info('            Port : %s' % get_env('JOBSERVERPORT'), also_console=True)
    logger.info('    Engine Param : %s' % get_env('al_engine_param'), also_console=True)
    logger.info('----------------------------------------------------', also_console=True)
    logger.info('     Running Job : %s' % runjob, also_console=True)
    logger.info('         Options : %s' % jobexeoption, also_console=True)
    logger.info('         RUNTEST : %s' % get_env('runtest'), also_console=True)
    logger.info('        LINK_DIR : %s' % get_env('LINK_DIR'), also_console=True)
    logger.info('====================================================', also_console=True)

    return shell_command(' '.join(cmd), True)


def import_atl(atlFileName, passPhrase='dsplatform'):
    atlFileName = replace_env_str(atlFileName)
    passPhrase = replace_env_str(passPhrase)
    if get_env('IMPORT').upper() == 'FALSE':
        logger.warn("No atl import")
        return
    else:
        runtest = get_env('runtest')
        DS_WORK = get_env('DS_WORK')
        JYTHON_CMD = get_env('JYTHON_CMD')
        al_engine_param = get_env('al_engine_param')
        subvalue2 = get_env('subvalue2')
        # ${JYTHON_CMD} ${subvalue2} $runtest/positive/$ATLFILE $DS_WORK/t$ATLFILE
        cmd = [JYTHON_CMD, subvalue2, runtest + '/positive/' + atlFileName, DS_WORK + '/t' + atlFileName]
        shell_command(' '.join(cmd))
        # al_engine ${al_engine_param} -f$DS_WORK/t$ATLFILE -z$DS_WORK/t$ATLFILE.txt  -passphrasedsplatform
        cmd = ['al_engine', al_engine_param, '-f' + DS_WORK + '/t' + atlFileName, '-z' + DS_WORK + '/t' + atlFileName,
               '-passphrase' + passPhrase]
        shell_command(' '.join(cmd))


def unescape(content):
    return re.sub(r'\\(.)', r'\1', content)

def checksum(file):
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def diff_unordered_files(gold, work, limit=10):
    gold = replace_env_str(gold)
    work = replace_env_str(work)
    af1 = os.path.abspath(gold)
    af2 = os.path.abspath(work)

    if checksum(gold) == checksum(work):
        return 'Success'

    with open(gold, 'r') as fGoldFile:
        with open(work, 'r') as fWorkFile:
            regex = re.compile(r'<!--.*-->|xsi:schemaLocation=".*">|<ID>.*</ID>|<TableIndex Name=".*"')
            glinesPre1 = map(lambda line: regex.sub("", line), fGoldFile.readlines())
            wlinesPre1 = map(lambda line: regex.sub("", line), fWorkFile.readlines())

            regex = re.compile(r'\r?\n$|\r$')
            glinesPre2 = map(lambda line: regex.sub("", line), glinesPre1)
            wlinesPre2 = map(lambda line: regex.sub("", line), wlinesPre1)

            glinesPre3 = map(lambda line: re.escape(line), glinesPre2)

            regex = re.compile(r'\\\*')
            glines = map(lambda line: regex.sub(".*?", line), glinesPre3)
            wlines = wlinesPre2

            lenglines = len(glines)
            lenwlines = len(wlines)

            if lenglines != lenwlines:
                diffInfo = []
                diffInfo.append("gold and work has different line number")
                diffInfo.append("glod has %d lines" % lenglines)
                diffInfo.append("====================")
                diffInfo.append("work has %d lines" % lenwlines)
                logger.info('\n', also_console=True)
                logger.info('\n'.join(diffInfo), also_console=True)
                raise AssertionError("Files are different: %s %s" % (af1, af2))

            while True:
                gfStartLen = len(glines)
                for i, gline in enumerate(glines):
                    for j, wline in enumerate(wlines):
                        m = re.match(gline, wline)
                        s = re.split(gline, wline)
                        if m is not None and s[0] == '' and s[1] == '':
                            del glines[i]
                            del wlines[j]
                            break
                gfEndLen = len(glines)
                if gfStartLen == gfEndLen:
                    break

            if len(glines) > 0 or len(wlines) > 0:
                i = 0
                setDiffs = set()
                for gline in glines:
                    diffInfo = []
                    diffInfo.append("gold: " + unescape(gline))
                    wline = difflib.get_close_matches(gline, wlines, n=1)
                    if len(wline) == 1 and gline != wline[0]:
                        diffInfo.append("work: " + wline[0])
                    else:
                        diffInfo.append("work: Missing!")
                    diffInfo.append("====================")
                    setDiffs.add('\n'.join(diffInfo))
                    i += 1
                    if i > limit:
                        break

                for wline in wlines:
                    diffInfo = []
                    gline = difflib.get_close_matches(wline, glines, n=1)
                    if len(gline) == 1 and gline[0] != wline:
                        diffInfo.append("gold: " + unescape(gline[0]))
                    else:
                        diffInfo.append("gold: Missing!")
                    diffInfo.append("work: " + wline)
                    diffInfo.append("====================")
                    setDiffs.add('\n'.join(diffInfo))
                    i += 1
                    if i > limit:
                        break

                logger.info('\n', also_console=True)
                for diff in setDiffs:
                    logger.info(diff, also_console=True)

                #raise AssertionError("Files are different: %s %s" % (af1, af2))

    return 'Success'


def replace_env(fo, fn):
    fo = replace_env_str(fo)
    fn = replace_env_str(fn)
    dic = os.environ
    with open(fo, 'r') as fin:
        with open(fn, 'w') as fout:
            regex = re.compile('\%(\w+)\%')
            for line in fin:
                it = regex.finditer(line)
                for match in it:
                    if match.group(1)[:10] == 'ENCRYPTED_':
                        key = match.group(1)
                        if key in dic:
                            line = line.replace(match.group(0), dic[key])
                        else:
                            key2 = match.group(1)[10:]
                            if key2 in dic:
                                val = encrypt(dic[key2])
                                line = line.replace(match.group(0), val)
                                dic[key] = val
                    else:
                        key = match.group(1)
                        if key in dic:
                            line = line.replace(match.group(0), dic[key])
                fout.write(line)


def encrypt(password):
    if not "DS_COMMON_DIR" in os.environ:
        raise EnvironmentError("$DS_COMMON_DIR is not defined, please source al_env.sh first.")

    exe = os.path.join(os.environ["DS_COMMON_DIR"], "bin", "AL_Encrypt")
    cmd = [exe, '-e', password, '-p', 'mats']
    # logger.console('RUN: %s' % cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return process.communicate()[0].strip()


''' Not used '''


def diff_unordered_files_reference(gold, work, limit=10):
    gold = replace_env_str(gold)
    work = replace_env_str(work)
    with open(gold, 'r') as gf:
        with open(work, 'r') as wf:
            # logger.console('DIFF: %s - %s' % (gold, work))
            regex = re.compile(r'<!--.*-->|xsi:schemaLocation=".*">|<ID>.*</ID>|<TableIndex Name=".*"')
            glines0 = list(map(lambda l: regex.sub("", l), gf.readlines()))
            wlines = list(map(lambda l: regex.sub("", l), wf.readlines()))
            regex = re.compile(r'\n')
            glines = list(map(lambda l: regex.sub("", l), glines0))
            wlines = list(map(lambda l: regex.sub("", l), wlines))
            glinest = list(map(lambda l: re.escape(l), glines))
            regex = re.compile(r'\\\*')
            glines = list(map(lambda l: regex.sub(r'.*', l), glinest))

            ok = (len(glines) == len(wlines))
            if ok:
                for i, gline in enumerate(glines):
                    ok = False
                    for j, wline in enumerate(wlines):
                        if re.match(gline, wline) is not None:
                            ok = True
                            del glines[i]
                            del wlines[j]
                            break
                    if not ok:
                        logger.info(glines0[i])
                        break

            if not ok:
                diff = difflib.unified_diff(glines0, wlines)
                i = 0
                for gline in diff:
                    logger.info(gline)
                    i += 1
                    if i > limit:
                        break
                if i > 0:
                    af1 = os.path.abspath(gold)
                    af2 = os.path.abspath(work)
                    raise AssertionError("Files are different: %s %s" % (af1, af2))
    return 'Success'


def diff_unordered_files_old(gold, work, xml=True, escape=True, limit=10):
    gold = replace_env_str(gold)
    work = replace_env_str(work)
    with open(gold, 'r') as gf:
        with open(work, 'r') as wf:
            # logger.console('DIFF: %s - %s' % (gold, work))
            if xml:
                regex = re.compile(r'<!--.*-->|xsi:schemaLocation=\".*\">|<ID>.*</ID>|<TableIndex Name=\".*\"')
                glines = map(lambda l: regex.sub("", l), gf.readlines())
                wlines = map(lambda l: regex.sub("", l), wf.readlines())

            ok = (len(glines) == len(wlines))
            if ok:
                for line in glines:
                    if escape:
                        # some gold logs have escaped chars
                        line = line.decode('string_escape')
                    if not line in wlines:
                        ok = False
                        break
            if not ok:
                diff = difflib.unified_diff(glines, wlines)
                i = 0
                for line in diff:
                    logger.info(line)
                    i += 1
                    if i > limit:
                        break
                if i > 0:
                    af1 = os.path.abspath(gold)
                    af2 = os.path.abspath(work)
                    raise AssertionError("Files are different: %s %s" % (af1, af2))


def replace_var(fo, fn):
    dic = BuiltIn().get_variables()
    with open(fo, 'r') as fin:
        with open(fn, 'w') as fout:
            regex = re.compile('\%(\w+)\%')
            for line in fin:
                it = regex.finditer(line)
                for match in it:
                    if match.group(1)[:10] == 'ENCRYPTED_':
                        key = '${%s}' % match.group(1)
                        if key in dic:
                            line = line.replace(match.group(0), dic[key])
                        else:
                            key2 = '${%s}' % match.group(1)[10:]
                            if key2 in dic:
                                val = encrypt(dic[key2])
                                line = line.replace(match.group(0), val)
                                BuiltIn().set_suite_variable(key, val)
                                dic[key] = val
                    else:
                        key = '${%s}' % match.group(1)
                        if key in dic:
                            line = line.replace(match.group(0), dic[key])
                fout.write(line)


def diff_files(f1, f2, limit=10):
    with open(f1, 'r') as fi1:
        with open(f2, 'r') as fi2:
            # logger.console('DIFF: %s - %s' % (f1, f2))
            diff = difflib.unified_diff(
                fi1.readlines(),
                fi2.readlines()
            )
            i = 0
            for line in diff:
                logger.info(line)
                i += 1
                if i > limit:
                    break
            if i > 0:
                af1 = os.path.abspath(f1)
                af2 = os.path.abspath(f2)
                raise AssertionError("Files are different: %s %s" % (af1, af2))


def diff_xml_files(f1, f2, limit=10):
    with open(f1, 'r') as fi1:
        with open(f2, 'r') as fi2:
            # logger.console('DIFF: %s - %s' % (f1, f2))
            regex = re.compile(r'^\s*<!--.*-->\s*$')
            diff = difflib.unified_diff(
                filter(lambda l: not regex.match(l), fi1.readlines()),
                filter(lambda l: not regex.match(l), fi2.readlines()),
            )
            i = 0
            for line in diff:
                logger.info(line)
                i += 1
                if i > limit:
                    break
            if i > 0:
                af1 = os.path.abspath(f1)
                af2 = os.path.abspath(f2)
                raise AssertionError("Files are different: %s %s" % (af1, af2))
