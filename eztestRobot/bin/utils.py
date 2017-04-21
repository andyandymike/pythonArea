import shlex
import re


def splitParams(params):
    lex = shlex.shlex(params, posix=False)
    lex.whitespace_split = True
    tempoutput = list(lex)
    tempoutput = ['sh', '-c', '"al_engine -NHANA -Svanpgcmsdb06.pgdev.sap.corp -UI067382 -PPassword1 -Kserver -Kport30815 -Kversion\'HANA 1.x\' -QI067382 -shana_ansi_inserttables -l/net/vanhome/teams/sheimbuild/landy/Jenkins_Working/AIX/work/HANA/HANA_ANSI_Datastore/hana_ansi_inserttables.log -t/net/vanhome/teams/sheimbuild/landy/Jenkins_Working/AIX/work/HANA/HANA_ANSI_Datastore/hana_ansi_inserttables.err"']
    output = []
    temp = ''
    merge = False
    m1 = re.compile(r'\'.*\'')
    m2 = re.compile(r'\\\'')
    for arg in tempoutput:
        if m1.match(arg) is None:
            if m2.match(arg) is None:
                if arg.find("'") != -1:
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