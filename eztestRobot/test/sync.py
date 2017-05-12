import os
import re
import hashlib
import shutil

def ignore(fileName):
    m1 = re.compile(r'.*\.jar$')
    if m1.match(fileName):
        return True
    return False

def checksum(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def main():

    robotRoot = os.path.abspath('..')
    des = 'Y:\\landy\\robot\\eztestRobot'

    for (root, dirs, files) in os.walk(robotRoot):
        for fileName in files:
            if not ignore(fileName):
                folder = os.path.abspath(root)[len(os.path.abspath(robotRoot)) + 1:]
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
                        if os.path.isfile(desfile + '.bk'):
                            os.remove(desfile + '.bk')
                        os.rename(desfile, desfile + '.bk')
                        shutil.copy(srcfile, desfile)
                        continue
                    else:
                        continue
                else:
                    print('Sync file: ' + srcfile)
                    shutil.copy(srcfile, desfile)


if __name__ == '__main__':
    main()