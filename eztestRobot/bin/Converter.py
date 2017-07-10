#!/bin/env python
from __future__ import with_statement

import os
import sys
import re
import shlex
from Handler import *


def converter(root, fileName):
    inputFile = os.path.join(root, fileName)
    with open(inputFile, 'r') as fInputFile:
        testunit = TestUnit(os.path.basename(root))
        testcase = None
        temptestcase = None
        keyword = None

        re_export = re.compile(r'export\s+(\w+)=(.+)')
        re_adiff = re.compile(r'adiff\s+(.+)\s+(.+)')
        re_subvar = re.compile(r'subvalue2\s+(.+)\s+(.+)')
        re_regcheck = re.compile(r'!regcheck\s+(.+)\s+(.+)')
        re_export2 = re.compile(r'(\w+)=(.+)')
        re_importAtl = re.compile(r'import_atl\.sh\s+(.+)')
        re_expect = re.compile(r'!expect\s+(\w+)\s+\*?([^\*]+)\*?')
        re_define = re.compile(r'!define\s+(\w+)\s*')
        re_testcase = re.compile(r'!testcase\s+(\w+)\s*')
        re_testcase_doc = re.compile(r'!testcase\s+\w+\s+(.+)')
        re_call = re.compile(r'!call\s+(\w+)\s*')
        re_eimlauncher = re.compile(r'eim_launcher\.sh\s+(.+)')

        def findTestStep(ln):
            if ln[:2] == "cd":
                robotTestStep = ChangeWorkingDirStep(ln[3:].strip())
                return robotTestStep
            m = re_eimlauncher.match(ln.replace(r'\$', r'$').replace(r'\|', r'|'))
            if m:
                eimlauncherparams = shlex.split(m.group(1))
                jobname = shlex.split(m.group(1))[0].replace(r'$', r'\$').replace(r'|', r'\|')
                if len(eimlauncherparams) == 1:
                    robotTestStep = EIMLauncherStep(jobname)
                else:
                    eimlauncherparams = shlex.split(m.group(1))[1:]
                    robotTestStep = EIMLauncherStep(jobname, eimlauncherparams)
                return robotTestStep
            m = re_importAtl.match(ln)
            if m:
                robotTestStep = ImportATLStep(m.group(1))
                return robotTestStep
            m = re_export.match(ln)
            if m:
                robotTestStep = ExportEnvStep(m.group(1), m.group(2).replace('\\', '\\\\').replace(r'\\$', r'\$').replace(r'\\|', r'\|'))
                return robotTestStep
            m = re_adiff.match(ln)
            if m:
                robotTestStep = DiffStep(m.group(1), m.group(2))
                return robotTestStep
            m = re_subvar.match(ln)
            if m:
                robotTestStep = SubvarStep(m.group(1), m.group(2))
                return robotTestStep
            m = re_export2.match(ln)
            if m:
                robotTestStep = ExportEnvStep(m.group(1), m.group(2).replace('\\', '\\\\').replace(r'\\$', r'\$').replace(r'\\|', r'\|'))
                return robotTestStep
            robotTestStep = RunStep(ln)
            return robotTestStep

        # setup file
        setupFileTestSteps = []
        setupFile = os.path.join(root, 'setup')
        try:
            with open(setupFile, 'r') as fSetupFile:
                for ln in fSetupFile:
                    ln = ln.strip()
                    robotTestStep = None
                    if not len(ln):
                        continue
                    elif ln[0] == '#':
                        continue
                    elif ln[0] == '!':
                        ln = ln.replace(r'$', r'\$')
                        ln = ln.replace(r'|', r'\|')

                        if ln[:3] == "!sh":
                            ln = ln[4:].strip()
                            if not len(ln):
                                continue
                            robotTestStep = findTestStep(ln)

                    if robotTestStep:
                        testunit.addSetup(robotTestStep)
                        setupFileTestSteps.append(robotTestStep)
        except:
            pass

        # testcase file
        tempCaseNum = 0
        expectNextResult = False
        skipKeyWord = False
        for ln in fInputFile:
            ln = ln.strip()
            robotTestStep = None

            if not len(ln):
                continue
            elif ln[0] == '#':
                continue

            if ln[0] == '$':
                try:
                    ln = os.environ[ln[1:]]
                except KeyError:
                    continue

            if ln[0] == '!':
                ln = ln.replace(r'$', r'\$')
                ln = ln.replace(r'|', r'\|')

                if ln[:3] == "!sh":
                    ln = ln[4:].strip()
                    if not len(ln):
                        continue
                    robotTestStep = findTestStep(ln)
                    if expectNextResult:
                        expectStep.step2Expect(robotTestStep)
                        robotTestStep = expectStep
                        expectNextResult = False

                elif ln[:9] == "!regcheck":
                    m = re_regcheck.match(ln)
                    if m:
                        robotTestStep = DiffStep(m.group(1), m.group(2))

                elif ln[:5] == "!call":
                    m = re_call.match(ln)
                    if m and m.group(1) != 'setup':
                        robotTestStep = CallStep(m.group(1))

                elif ln[:9] == "!testcase":
                    m = re_testcase.match(ln)
                    mdoc = re_testcase_doc.match(ln)
                    if mdoc:
                        robotTestStep = DocStep(mdoc.group(1).strip())
                    if testcase:
                        testunit.addCase(testcase)
                    testcase = TestCase(m.group(1).strip())

                elif ln[:12] == "!endtestcase":
                    testunit.addCase(testcase)
                    testcase = None

                elif ln[:7] == "!expect":
                    expectNextResult = True
                    m = re_expect.match(ln)
                    if m.group(1).lower() == 'no':
                        expectStep = ExpectStep('no', m.group(2).strip())
                    elif m.group(1).lower() == 'any':
                        expectStep = ExpectStep('any', m.group(2).strip())
                    else:
                        expectNextResult = False

                elif ln[:7] == "!define":
                    m = re_define.match(ln)
                    if m.group(1).strip() != 'setup':
                        skipKeyWord = False
                        if keyword:
                            testunit.addKeyWord(keyword)
                        keyword = KeyWord(m.group(1))
                    else:
                        skipKeyWord = True

                elif ln[:4] == "!end":
                    if not skipKeyWord:
                        testunit.addKeyWord(keyword)
                        keyword = None

            else:
                robotTestStep = InvalidStep(ln)

            if robotTestStep is None:
                continue

            if keyword:
                keyword.addKeyWordStep(robotTestStep)
            elif testcase:
                if temptestcase is not None:
                    testunit.addCase(temptestcase)
                    temptestcase = None
                testcase.addStep(robotTestStep)
            elif testunit.numCases():
                # # finish the current test suite
                # outputFile = inputFile + "_%d.robot" % nest
                # nest += 1
                # with open(outputFile, 'w') as fOutputFile:
                #     print("Converting %s to %s ..." % (inputFile, outputFile))
                #     fOutputFile.write(str(testunit))
                # # start a new test suite
                # testunit = TestUnit(os.path.basename(root))
                # for setupFileTestStep in setupFileTestSteps:
                #     testunit.addSetup(setupFileTestStep)

                if temptestcase is None:
                    tempTestcaseName = 'InTestingSetup_' + str(tempCaseNum)
                    temptestcase = TestCase(tempTestcaseName)
                    temptestcase.addStep(TagStep('InTestingSetup'))
                    temptestcase.addStep(robotTestStep)
                    tempCaseNum += 1
                else:
                    temptestcase.addStep(robotTestStep)
                pass
            else:
                testunit.addSetup(robotTestStep)

        if testunit.numCases() == 0:
            temptestcase = TestCase('A temp testcase')
            temptestcase.addStep(DocStep('Create a temp testcase to run setup'))
            temptestcase.addStep(TagStep('InTestingSetup'))
            temptestcase.addStep(RunStep('echo A temp testcase'))
            testunit.addCase(temptestcase)

        outputFile = inputFile + ".robot"
        with open(outputFile, 'w') as fOutputFile:
            os.chmod(outputFile, 0777)
            print("Converting %s to %s ..." % (inputFile, outputFile))
            fOutputFile.write(str(testunit))


def walk(path):
    for (root, dirs, files) in os.walk(path):
        for fileName in files:
            if fileName == "testcase":
                converter(root, fileName)


def main():
    if len(sys.argv) == 1:
        print("Usage: %s <DIR|FILE> ..." % sys.argv[0])
        sys.exit(1)

    for a in sys.argv[1:]:
        if os.path.isdir(a):
            path = os.path.abspath(a)
            walk(path)
        elif os.path.isfile(a):
            path = os.path.abspath(a)
            (dir, file) = os.path.split(path)
            converter(dir, file)


if __name__ == "__main__":
    main()
