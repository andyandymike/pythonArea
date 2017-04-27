class TestUnit(object):
    def __init__(self, name):
        self._name = name
        self._testcases = []
        self._setups = []
        self._variables = []
        self._keywords = []

    def addCase(self, testcase):
        self._testcases.append(testcase)

    def addSetup(self, setup):
        self._setups.append(setup)

    def addKeyWord(self, keyword):
        self._keywords.append(keyword)

    def addVariable(self, variable):
        self._variables.append(variable)

    def numCases(self):
        return len(self._testcases)

    def __str__(self):
        robotContent = ["| *** Settings *** |"]
        robotContent.append("| Library | ${ROBOTHOME}/OSHelper.py |")
        robotContent.append("| Suite Setup | Combined Setup |")
        robotContent.append("| Force Tags | %s |" % self._name)
        robotContent.append("| Test Timeout | ${ROBOT_TEST_TIMEOUT} |")
        robotContent.append("")
        robotContent.append("| *** Keywords *** |")
        for keyword in self._keywords:
            robotContent.append(str(keyword))
        robotContent.append("| Combined Setup |")
        for setup in self._setups:
            robotContent.append(str(setup))
        robotContent.append("")
        robotContent.append("| *** Test Cases *** |")
        for testcase in self._testcases:
            robotContent.append(str(testcase))
        robotContent.append("")
        robotContent.append("| *** Variables *** |")
        for variable in self._variables:
            robotContent.append(str(variable))
        robotContent.append("")
        return "\n".join(robotContent)


class TestCase(object):
    def __init__(self, name):
        self._name = name
        self._steps = []

    def addStep(self, step):
        self._steps.append(step)

    def getTestCaseName(self):
        return self._name

    def __str__(self):
        robotContent = ["| %s |" % self._name]
        for step in self._steps:
            robotContent.append(str(step))
        robotContent.append("")
        return "\n".join(robotContent)


class KeyWord(object):
    def __init__(self, name):
        self._name = name
        self._keyWordSteps = []

    def addKeyWordStep(self, step):
        self._keyWordSteps.append(step)

    def __str__(self):
        robotContent = ["| %s |" % self._name]
        for step in self._keyWordSteps:
            robotContent.append(str(step))
        robotContent.append("")
        return "\n".join(robotContent)


class Variable(object):
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def __str__(self):
        return "| ${%s}         %s |" % (self._key, self._value)


class InterimSetup(object):
    def __init__(self):
        self._steps = []

    def addStep(self, step):
        self._steps.append(step)

    def __str__(self):
        robotContent = ["# Please review and move the following steps into the next test unit if necessary:"]
        for step in self._steps:
            robotContent.append("# %s" % str(step))
        robotContent.append("")
        return "\n".join(robotContent)


''' Test steps '''


class TestStep(object):
    def __init__(self, step):
        self._step = step

    def getStep(self):
        return self._step

    def __str__(self):
        return "|  %s" % self._step


class ExpectStep(TestStep):
    def __init__(self, behavior, keyword):
        self._behavior = behavior
        self._keyword = keyword
        self._steps = []
        if (self._behavior == 'any'):
            self._steps.append("|  | Should Contain | ${result} | %s " % self._keyword)
        if (self._behavior == 'no'):
            self._steps.append("|  | Should Not Contain | ${result} | %s " % self._keyword)

    def step2Expect(self, step):
        self._steps.insert(0, "|  | ${result} = %s" % step.getStep())

    def __str__(self):
        return "\n".join(self._steps)


class DocStep(TestStep):
    def __init__(self, doc):
        self._doc = doc
        super(DocStep, self).__init__("| [Documentation] | %s " % self._doc)


class TagStep(TestStep):
    def __init__(self, tag):
        self._tag = tag
        super(TagStep, self).__init__("| [Tags] | %s " % self._tag)


class IgnoreErrorStep(TestStep):
    def __init__(self, step):
        super(IgnoreErrorStep, self).__init__("| Run Keyword And Ignore Error | %s " % step.getStep())


class CallStep(TestStep):
    def __init__(self, call):
        self._call = call
        super(CallStep, self).__init__("| %s |" % self._call)


class ImportATLStep(TestStep):
    def __init__(self, atlFileName):
        self._atlFileName = atlFileName
        super(ImportATLStep, self).__init__("| Import ATL | %s " % self._atlFileName)


class EIMLauncherStep(TestStep):
    def __init__(self, jobname, args=None):
        self._args = []
        self._jobname = jobname
        if args is not None:
            for arg in args:
                self._args.append(arg.replace(r'$', r'\$').replace(r'|', r'\|'))
        if len(self._args) != 0:
            super(EIMLauncherStep, self).__init__("| EIM Launcher | %s | %s" % (self._jobname, ' | '.join(self._args)))
        else:
            super(EIMLauncherStep, self).__init__("| EIM Launcher | %s " % self._jobname)


class RunStep(TestStep):
    def __init__(self, cmd):
        self._cmd = cmd
        super(RunStep, self).__init__("| Shell Command | %s " % self._cmd)


class DiffStep(TestStep):
    def __init__(self, goldlogFile, workFile):
        self._goldlogFile = goldlogFile
        self._workFile = workFile
        super(DiffStep, self).__init__("| Diff Unordered Files | %s | %s " % (self._goldlogFile, self._workFile))


class SubvarStep(TestStep):
    def __init__(self, inputFile, outputFile):
        self._inputFile = inputFile
        self._outputFile = outputFile
        super(SubvarStep, self).__init__("| Replace Env | %s | %s " % (self._inputFile, self._outputFile))


class ExportEnvStep(TestStep):
    def __init__(self, key, val):
        self._key = key
        self._val = val
        super(ExportEnvStep, self).__init__("| Export Env | %s | %s " % (self._key, self._val))


class ChangeWorkingDirStep(TestStep):
    def __init__(self, changeWorkingDir):
        self._changeWorkingDir = changeWorkingDir
        super(ChangeWorkingDirStep, self).__init__("| Change Working Directory | %s " % self._changeWorkingDir)


class InvalidStep(TestStep):
    def __init__(self, cmd):
        self._cmd = cmd

    def __str__(self):
        return "# Invalid line: %s " % self._cmd
