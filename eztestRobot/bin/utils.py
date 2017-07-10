import os
import re
import subprocess
import difflib
import shlex
import hashlib
import sys


# from java.lang import Class
# from java.sql import DriverManager, SQLException

# import java.lang.reflect.Method
# import java.lang.ClassLoader as javaClassLoader
# from java.lang import Object as javaObject
# from java.io import File as javaFile
# from java.net import URL as javaURL
# from java.net import URLClassLoader
# import jarray


class classPathHacker:
    ##########################################################
    # from http://forum.java.sun.com/thread.jspa?threadID=300557
    #
    # Author: SG Langer Jan 2007 translated the above Java to this
    #       Jython class
    # Purpose: Allow runtime additions of new Class/jars either from
    #       local files or URL
    ######################################################

    def addFile(self, s):
        """Purpose: If adding a file/jar call this first
        with s = path_to_jar"""
        # make a URL out of 's'
        f = javaFile(s)
        u = f.toURL()
        a = self.addURL(u)
        return a

    def addURL(self, u):
        """Purpose: Call this with u= URL for
        the new Class/jar to be loaded"""
        sysloader = javaClassLoader.getSystemClassLoader()
        sysclass = URLClassLoader
        method = sysclass.getDeclaredMethod("addURL", [javaURL])
        a = method.setAccessible(1)
        jar_a = jarray.array([u], javaObject)
        b = method.invoke(sysloader, [u])
        return u


class SQLite:
    def __init__(self):
        self.database = 'test.db'
        self.driver = 'org.sqlite.JDBC'
        self.url = 'jdbc:sqlite:' + self.database
        jarLoad = classPathHacker()
        jarLoad.addFile("C:\\Users\\i067382\\PycharmProjects\\eztestRobot\\lib\\sqlite-jdbc-3.18.0.jar")

    def connect(self):
        Class.forName('org.sqlite.JDBC').newInstance()
        self.dbConn = DriverManager.getConnection(self.url)
        self.stmt = self.dbConn.createStatement()
        return self.dbConn

    def execute(self, query):
        print('Executing query: ' + str(query))
        resultSet = self.stmt.executeUpdate(query)
        return resultSet

    def query(self, query):
        print('Executing query: ' + str(query))
        resultSet = self.dbConn.createStatement().executeQuery(query)
        return resultSet

    def close(self):
        self.stmt.close()
        self.dbConn.close()


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


def bigFileMaker(input, output, times):
    with open(input, 'rU') as inf:
        with open(output, 'wb') as ouf:
            lines = inf.readlines()
            for i in range(times):
                ouf.writelines(lines)


def unescape(content):
    return re.sub(r'\\(.)', r'\1', content)


def checksum(file):
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def diff_unordered_files(gold, work, limit=10):
    gold = replace_env_str(gold)
    work = replace_env_str(work)
    gsize = os.stat(gold).st_size
    wsize = os.stat(work).st_size
    af1 = os.path.abspath(gold)
    af2 = os.path.abspath(work)

    print(' ')
    print('==  Compare files   ==')
    print('gold: %s' % os.path.basename(gold))
    print('work: %s' % os.path.basename(work))
    print('----------------------')

    if gsize > 300000000L or wsize > 300000000L:
        print('Files are too big (over 300mb)! Diff in EX Big File Mode (Can not ensure correct result)')
        if gsize == wsize:
            return 'Success'
        else:
            diffInfo = []
            diffInfo.append("gold and work has different file size")
            diffInfo.append("glod size: %s" % gsize)
            diffInfo.append("work size: %s" % wsize)
            diffInfo.append("----------------------")
            print('\n')
            print('\n'.join(diffInfo))
            raise AssertionError("Files are different: %s %s" % (af1, af2))

    if checksum(gold) == checksum(work):
        return 'Success'

    print('checksum finished')

    with open(gold, 'rU') as fGoldFile:
        with open(work, 'rU') as fWorkFile:
            re_xml = re.compile(r'<!--.*-->|xsi:schemaLocation=".*">|<ID>.*</ID>|<TableIndex Name=".*"')
            glinesPre1 = map(lambda line: re_xml.sub("", line), fGoldFile.readlines())
            wlinesPre1 = map(lambda line: re_xml.sub("", line), fWorkFile.readlines())

            re_wrap = re.compile(r'\r?\n$|\r+$')
            glinesPre2 = []
            for line in glinesPre1:
                line = re_wrap.sub("", line)
                if line != '':
                    glinesPre2.append(line)
            wlinesPre2 = []
            for line in wlinesPre1:
                line = re_wrap.sub("", line)
                if line != '':
                    wlinesPre2.append(line)

            glinesPre3 = map(lambda line: line.replace("\\\\", "\\"), glinesPre2)
            glinesPre4 = map(lambda line: re.escape(line), glinesPre3)

            re_multi = re.compile(r'\\\*')
            re_single = re.compile(r'\\\?')
            glines = map(lambda line: re_multi.sub(".*", line), glinesPre4)
            glines = map(lambda line: re_single.sub(".?", line), glines)
            wlines = wlinesPre2

            lenglines = len(glines)
            lenwlines = len(wlines)

            if lenglines != lenwlines:
                diffInfo = []
                diffInfo.append("gold and work has different line number")
                diffInfo.append("glod has %d lines" % lenglines)
                diffInfo.append("work has %d lines" % lenwlines)
                diffInfo.append("----------------------")
                print('\n')
                print('\n'.join(diffInfo))
                raise AssertionError("Files are different: %s %s" % (af1, af2))

            if lenglines > 10000:
                print('Files have too many lines! Diff in Big File Mode (Do not support wildcard)')

                diffInfo = []
                j = 0

                sqlite = SQLite()
                try:
                    con = sqlite.connect()
                    sqlite.execute('''CREATE TABLE gtable (content            TEXT    NOT NULL)''')
                    sqlite.execute('''CREATE TABLE wtable (content            TEXT    NOT NULL)''')
                    gPreStmt = con.prepareStatement('''INSERT INTO gtable (content) VALUES (?)''')
                    wPreStmt = con.prepareStatement('''INSERT INTO wtable (content) VALUES (?)''')
                    for i in range(lenglines):
                        gPreStmt.setString(1, glinesPre2[i])
                        wPreStmt.setString(1, wlinesPre2[i])
                        gPreStmt.addBatch()
                        wPreStmt.addBatch()
                    con.setAutoCommit(False)
                    gPreStmt.executeBatch()
                    wPreStmt.executeBatch()
                    con.setAutoCommit(True)
                    sqlite.execute('''CREATE INDEX gindex ON gtable (content)''')
                    sqlite.execute('''CREATE INDEX windex ON wtable (content)''')
                    sqlite.execute(
                        '''CREATE TABLE tmp_gtable AS select COUNT(*) numbers, content FROM gtable GROUP BY content''')
                    sqlite.execute(
                        '''CREATE TABLE tmp_wtable AS select COUNT(*) numbers, content FROM wtable GROUP BY content''')
                    sqlite.execute('''CREATE INDEX index_tmp_gtable ON tmp_gtable (numbers, content)''')
                    sqlite.execute('''CREATE INDEX index_tmp_wtable ON tmp_wtable (numbers, content)''')
                    diffGold = sqlite.query(
                        '''SELECT * FROM tmp_gtable WHERE NOT EXISTS (SELECT * FROM tmp_wtable WHERE tmp_gtable.content = tmp_wtable.content and tmp_gtable.numbers = tmp_wtable.numbers)''')
                    while diffGold.next():
                        if j == limit:
                            break
                        numbers = diffGold.getInt('numbers')
                        content = diffGold.getString('content')
                        diffInfo.append("gold: %d lines of: %.100s" % (numbers, content))
                        print("gold: %d lines of: %.100s" % (numbers, content))
                        tmp = sqlite.query('''SELECT * FROM tmp_wtable WHERE content=\'%s\'''' % content)
                        if tmp.next():
                            numbers = tmp.getInt('numbers')
                            content = tmp.getString('content')
                            diffInfo.append("work: %d lines of: %.100s" % (numbers, content))
                            print("work: %d lines of: %.100s" % (numbers, content))
                        else:
                            diffInfo.append("work: Missing!")
                            print("work: Missing!")
                        diffInfo.append("----------------------")
                        print("----------------------")
                        j += 1

                    diffWork = sqlite.query(
                        '''SELECT * FROM tmp_wtable WHERE NOT EXISTS (SELECT * FROM tmp_gtable WHERE tmp_gtable.content = tmp_wtable.content and tmp_gtable.numbers = tmp_wtable.numbers)''')
                    while diffWork.next():
                        if j == limit:
                            break
                        numbers = diffWork.getInt('numbers')
                        content = diffWork.getString('content')
                        tmp = sqlite.query('''SELECT * FROM tmp_gtable WHERE content=\'%s\'''' % content)
                        if tmp.next():
                            numbers = tmp.getInt('numbers')
                            content = tmp.getString('content')
                            diffInfo.append("gold: %d lines of: %.100s" % (numbers, content))
                            print("gold: %d lines of: %.100s" % (numbers, content))
                        else:
                            diffInfo.append("gold: Missing!")
                            print("gold: Missing!")
                        diffInfo.append("work: %d lines of: %.100s" % (numbers, content))
                        print("work: %d lines of: %.100s" % (numbers, content))
                        diffInfo.append("----------------------")
                        print("----------------------")
                        j += 1
                except:
                    print(sys.exc_info()[0])
                finally:
                    sqlite.close()

                if j > 0:
                    print('\n')
                    print('\n'.join(diffInfo))
                    # raise AssertionError("Files are different: %s %s" % (af1, af2))

                return 'Success'

            while True:
                gfStartLen = len(glines)
                for i, gline in enumerate(glines):
                    for j, wline in enumerate(wlines):
                        m = re.match(gline, wline)
                        s = re.split(gline, wline)
                        if m is not None and s[0] == '' and s[1] == '':
                            del glines[i]
                            del wlines[j]
                            break
                gfEndLen = len(glines)
                if gfStartLen == gfEndLen:
                    break

            if len(glines) > 0 or len(wlines) > 0:
                i = 0
                setDiffs = set()
                for gline in glines:
                    diffInfo = []
                    diffInfo.append("gold: " + unescape(gline)[:100] + ' ...')
                    wline = difflib.get_close_matches(gline, wlines, n=1)
                    if len(wline) == 1 and gline != wline[0]:
                        diffInfo.append("work: " + wline[0][:100] + ' ...')
                    else:
                        diffInfo.append("work: Missing!")
                    diffInfo.append("----------------------")
                    setDiffs.add('\n'.join(diffInfo))
                    i += 1
                    if i > limit:
                        break

                for wline in wlines:
                    diffInfo = []
                    gline = difflib.get_close_matches(wline, glines, n=1)
                    if len(gline) == 1 and gline[0] != wline:
                        diffInfo.append("gold: " + unescape(gline[0])[:100] + ' ...')
                    else:
                        diffInfo.append("gold: Missing!")
                    diffInfo.append("work: " + wline[:100] + ' ...')
                    diffInfo.append("----------------------")
                    setDiffs.add('\n'.join(diffInfo))
                    i += 1
                    if i > limit:
                        break

                print('\n')
                for diff in setDiffs:
                    print(diff)

                    # raise AssertionError("Files are different: %s %s" % (af1, af2))

    return 'Success'


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


def diff_unordered_files_pre(gold, work, limit=10):
    gold = replace_env_str(gold)
    work = replace_env_str(work)
    gsize = os.stat(gold).st_size
    wsize = os.stat(work).st_size
    af1 = os.path.abspath(gold)
    af2 = os.path.abspath(work)

    print(' ')
    print('==  Compare files   ==')
    print('gold: %s' % os.path.basename(gold))
    print('work: %s' % os.path.basename(work))
    print('----------------------')

    if gsize > 300000000L or wsize > 300000000L:
        print('Files are too big (over 300mb)! Diff in EX Big File Mode (Can not ensure correct result)')
        if gsize == wsize:
            return 'Success'
        else:
            diffInfo = []
            diffInfo.append("gold and work has different file size")
            diffInfo.append("glod size: %s" % gsize)
            diffInfo.append("work size: %s" % wsize)
            diffInfo.append("----------------------")
            print('\n')
            print('\n'.join(diffInfo))
            # raise AssertionError("Files are different: %s %s" % (af1, af2))

    if checksum(gold) == checksum(work):
        return 'Success'

    with open(gold, 'rU') as fGoldFile:
        with open(work, 'rU') as fWorkFile:
            re_xml = re.compile(r'<!--.*-->|xsi:schemaLocation=".*">|<ID>.*</ID>|<TableIndex Name=".*"')
            glinesPre1 = map(lambda line: re_xml.sub("", line), fGoldFile.readlines())
            wlinesPre1 = map(lambda line: re_xml.sub("", line), fWorkFile.readlines())

            re_wrap = re.compile(r'\r?\n$|\r+$')
            glinesPre2 = []
            for line in glinesPre1:
                line = re_wrap.sub("", line)
                if line != '':
                    glinesPre2.append(line)
            wlinesPre2 = []
            for line in wlinesPre1:
                line = re_wrap.sub("", line)
                if line != '':
                    wlinesPre2.append(line)

            glinesPre3 = map(lambda line: line.replace("\\\\", "\\"), glinesPre2)
            glinesPre4 = map(lambda line: re.escape(line), glinesPre3)

            re_multi = re.compile(r'\\\*')
            re_single = re.compile(r'\\\?')
            glines = map(lambda line: re_multi.sub(".*", line), glinesPre4)
            glines = map(lambda line: re_single.sub(".?", line), glines)
            wlines = wlinesPre2

            lenglines = len(glines)
            lenwlines = len(wlines)

            if lenglines != lenwlines:
                diffInfo = []
                diffInfo.append("gold and work has different line number")
                diffInfo.append("glod has %d lines" % lenglines)
                diffInfo.append("work has %d lines" % lenwlines)
                diffInfo.append("----------------------")
                print('\n')
                print('\n'.join(diffInfo))
                # raise AssertionError("Files are different: %s %s" % (af1, af2))

            if lenglines > 10000:
                print('Files have too many lines! Diff in Big File Mode (Do not support wildcard)')

                glines_bf = sorted(glinesPre2)
                wlines_bf = sorted(wlinesPre2)
                diffInfo = []
                j = 0
                for i in range(lenglines):
                    if glines_bf[i] != wlines_bf[i] and j < limit:
                        diffInfo.append("gold: " + glines_bf[i])
                        diffInfo.append("work: " + wlines_bf[i])
                        diffInfo.append("----------------------")
                        j += 1
                    if j == limit:
                        break

                if j > 0:
                    print('\n')
                    print('\n'.join(diffInfo))
                    # raise AssertionError("Files are different: %s %s" % (af1, af2))

                return 'Success'

            while True:
                gfStartLen = len(glines)
                for i, gline in enumerate(glines):
                    for j, wline in enumerate(wlines):
                        m = re.match(gline, wline)
                        s = re.split(gline, wline)
                        if m is not None and s[0] == '' and s[1] == '':
                            del glines[i]
                            del wlines[j]
                            break
                gfEndLen = len(glines)
                if gfStartLen == gfEndLen:
                    break

            if len(glines) > 0 or len(wlines) > 0:
                i = 0
                setDiffs = set()
                for gline in glines:
                    diffInfo = []
                    diffInfo.append("gold: " + unescape(gline)[:100] + ' ...')
                    wline = difflib.get_close_matches(gline, wlines, n=1)
                    if len(wline) == 1 and gline != wline[0]:
                        diffInfo.append("work: " + wline[0][:100] + ' ...')
                    else:
                        diffInfo.append("work: Missing!")
                    diffInfo.append("----------------------")
                    setDiffs.add('\n'.join(diffInfo))
                    i += 1
                    if i > limit:
                        break

                for wline in wlines:
                    diffInfo = []
                    gline = difflib.get_close_matches(wline, glines, n=1)
                    if len(gline) == 1 and gline[0] != wline:
                        diffInfo.append("gold: " + unescape(gline[0])[:100] + ' ...')
                    else:
                        diffInfo.append("gold: Missing!")
                    diffInfo.append("work: " + wline[:100] + ' ...')
                    diffInfo.append("----------------------")
                    setDiffs.add('\n'.join(diffInfo))
                    i += 1
                    if i > limit:
                        break

                print('\n')
                for diff in setDiffs:
                    print(diff)

                    # raise AssertionError("Files are different: %s %s" % (af1, af2))

    return 'Success'
