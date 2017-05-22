import shlex
import re
import hashlib
import os
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

def subvalue2(input, output):
    if os.path.isfile(input):
        inputFilePath = os.path.abspath(input)
    else:
        raise IOError("Cannot find file: %s" % input)
        sys.exit(1)

    outputFilePath = os.path.abspath(output)

    re_env = re.compile(r'(%(\w+)%)')
    with open(inputFilePath, 'r') as finput:
        with open(outputFilePath, 'w') as foutput:
            os.chmod(outputFilePath, 0777)
            for ln in finput:
                for m in re_env.finditer(ln):
                    value = os.environ.get(m.group(2))
                    if value[0] == '"' and value[len(value) - 1] == '"':
                        value = value[1:len(value) - 1] if len(value) > 2 else ''
                    if value == None:
                        value = ''
                    ln = ln.replace(m.group(1), value)
                foutput.write(ln)

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

def replace_env(fo, fn):
    fo = replace_env_str(fo)
    fn = replace_env_str(fn)
    dic = os.environ
    with open(fo, 'r') as fin:
        with open(fn, 'w') as fout:
            os.chmod(fn, 0777)
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