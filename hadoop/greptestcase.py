import os
import re

input = 'Y:\\landy\\EZTEST\\diqa\\generic\\HANA'
output = 'C:\\Temp'

reg_testcase = re.compile(r'\s*!testcase\s+(\w+)\s*\w*')


def main():
    for (root, dirs, files) in os.walk(input):
        for fileName in files:
            print('checking file %s' % os.path.join(root, fileName))
            if fileName == "testcase":
                print('now handling %s' % os.path.basename(root))
                with open(os.path.join(root, fileName), 'r') as inf:
                    with open(os.path.join(output, 'testcase-merge'), 'a') as outf:
                        lines = inf.readlines()
                        for line in lines:
                            match = reg_testcase.match(line)
                            if match:
                                outf.write('%s, %s' % (os.path.basename(root), match.group(1)))
                                outf.write('\n')
    print('Done')


if __name__ == "__main__":
    main()
