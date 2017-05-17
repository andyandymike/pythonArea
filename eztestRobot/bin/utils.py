import shlex
import re
import hashlib
import subprocess


def splitParams(params):
    lex = shlex.shlex(params, posix=False)
    lex.whitespace_split = True
    tempoutput = list(lex)
    output = []
    temp = ''
    merge = False
    m1 = re.compile(r'.*\'.+\'.*')
    m2 = re.compile(r'.*\\\'.*')
    for arg in tempoutput:
        if m1.match(arg) is None:
            if m2.match(arg) is None:
                if arg.find("'") != -1:
                    print(arg)
                    merge = not merge
                    if not merge:
                        temp += ' ' + arg
                        output.append(temp.strip())
                        continue
        if merge:
            temp += ' ' + arg
        else:
            output.append(arg)

    return output

def checksum(file):
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def use_shell_command(val):
    re_export_val = re.compile(r'\\\$\(.+\s.*.+\)')
    m = re_export_val.match(val)
    if m:
        return True
    else:
        return False