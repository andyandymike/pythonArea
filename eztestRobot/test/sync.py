import os
import re
import hashlib
import shutil
from datetime import datetime


def ignore(fileName):
    m1 = re.compile(r'.*\.jar$')
    if m1.match(fileName):
        return True
    m2 = re.compile(r'.*\.db$')
    if m2.match(fileName):
        return True
    m3 = re.compile(r'.*\.exe$')
    if m3.match(fileName):
        return True
    return False


def checksum(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def main():
    flag = 'ezrobot'
    #flag = 'sikuli'
    bk = True
    robotRoot = os.path.abspath('..')
    syncRoot = robotRoot
    #syncRoot = 'C:\\Users\\i067382\\EIMTest\\eim_ui_testing\\DSSeleniumTests\\src'
    des = 'Y:\\landy\\keep\\robot\\eztestRobot'
    #des = 'Y:\\landy\\keep\\EIMTest\\eim_ui_testing\\DSSeleniumTests\\src'

    for (root, dirs, files) in os.walk(syncRoot):
        print(os.path.basename(root))
        if flag!= 'sikuli'and os.path.basename(root) == 'test':
            continue
        for fileName in files:
            if not ignore(fileName):
                folder = os.path.abspath(root)[len(os.path.abspath(syncRoot)) + 1:]
                srcfile = os.path.join(os.path.abspath(root), fileName)
                desfolder = os.path.join(os.path.abspath(des), folder)
                desfile = os.path.join(desfolder, fileName)
                try:
                    os.mkdir(desfolder)
                except WindowsError:
                    pass
                if os.path.isfile(desfile):
                    print('Sync file: ' + srcfile)
                    if not checksum(desfile) == checksum(srcfile):
                        if bk:
                            if os.path.isfile(desfile + '.bk'):
                                os.remove(desfile + '.bk')
                            os.rename(desfile, desfile + '.bk')
                        else:
                            os.remove(desfile)
                        shutil.copy(srcfile, desfile)
                        continue
                    else:
                        continue
                else:
                    print('Sync file: ' + srcfile)
                    shutil.copy(srcfile, desfile)


if __name__ == '__main__':
    main()
    print('Finish time : %s' % datetime.strftime(datetime.now(), '%a %b %d %H:%M:%S %Y'))
