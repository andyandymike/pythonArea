from __future__ import with_statement
import test


def printresult(result):
    for item in result:
        print(item)

if __name__ == '__main__':
    instance1 = test.test()
    instance1.test = 'hello'
    print(instance1.test)
    reload(test)
    print(instance1.test)
