class InvalidMyError(AttributeError):
    'Test how to use my error'

class PythonClassTest(object):
    'Test how to use Python class'
    def TestTrownError(self):
        raise InvalidMyError, 'Test how to thrown error'

pct = PythonClassTest()
try:
    pct.TestTrownError()
except InvalidMyError, err:
    print(InvalidMyError, err)