#!/bin/env python
from __future__ import with_statement

import sys
import os
import re


def main():
    if len(sys.argv) != 3:
        print("Usage: %s <DIR|FILE> <DIR|FILE>" % sys.argv[0])
        sys.exit(1)

    if os.path.isfile(sys.argv[1]):
        inputFilePath = os.path.abspath(sys.argv[1])
    else:
        raise IOError("Cannot find file: %s" % sys.argv[1])
        sys.exit(1)

    outputFilePath = os.path.abspath(sys.argv[2])

    re_env = re.compile(r'(%(\w+)%)')
    with open(inputFilePath, 'r') as finput:
        with open(outputFilePath, 'w') as foutput:
            os.chmod(outputFilePath, 0777)
            for ln in finput:
                for m in re_env.finditer(ln):
                    value = os.environ.get(m.group(2))
                    if value == None:
                        value = ''
                    ln = ln.replace(m.group(1), value)
                foutput.write(ln)


if __name__ == '__main__':
    main()
