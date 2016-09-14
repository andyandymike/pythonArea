import subprocess
import os

def runWinCommand(command):
    ps = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (outStdout, outStderr) = ps.communicate()
    print(outStdout)
    print(outStderr)
    return ps.returncode

if __name__ == '__main__':
    currentEnv = os.environ
    os.environ['test'] = 'hello'
    print(currentEnv['test'])
    command = 'set test=hi&&echo %test%'
    runWinCommand(command)