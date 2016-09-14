__author__ = 'i067382'

import os

#Function: Read content from a file. Support read specific number of lines, start read from specific line number, skip every specific number of lines
def ReadFromFile(FileLoc, LineLimit = 'ALL', StartLine = 1, SkipRead = 0):
    LineLimit = str(LineLimit)
    if LineLimit.upper() != 'ALL' and not LineLimit.isdigit():
        print('Error: LineCount must be number or ALL')
        return False
    if StartLine < 1:
        print('Error: StartLine must larger than or equal to 1')
        return False
    if SkipRead < 0:
        print('Error: SkipRead must larger than or equal to 0')
        return False
    FileStatus = os.path.isfile(FileLoc)
    if FileStatus is False:
        print('Error: Cerberus fail to find file: ' + FileLoc + ', cannot read it')
        return False
    File = open(FileLoc, 'r')
    LineCount = 0
    LineContent = []
    SkipReadTemp = SkipRead
    try:
        if LineLimit.upper() == 'ALL':
            FileLine = File.readline()
            while FileLine:
                FileLine = PurifyLine(FileLine)
                if LineCount == StartLine - 1:
                    LineContent.append(FileLine)
                if LineCount > StartLine - 1 and SkipReadTemp == 0:
                    LineContent.append(FileLine)
                    SkipReadTemp = SkipRead
                    LineCount = LineCount + 1
                    FileLine = File.readline()
                    #FileLine = PurifyLine(FileLine)
                    continue
                if LineCount > StartLine - 1 and SkipReadTemp >= 1:
                    SkipReadTemp = SkipReadTemp - 1
                LineCount = LineCount + 1
                FileLine = File.readline()
                #FileLine = PurifyLine(FileLine)
            return LineContent
        else:
            LineLimit = int(LineLimit)
            if LineLimit < 0:
                print('Error: LineLimit must larger than or equal to 0')
                return False
            FileLine = File.readline()
            while FileLine and LineLimit > 0:
                FileLine = PurifyLine(FileLine)
                if LineCount == StartLine - 1:
                    LineContent.append(FileLine)
                if LineCount > StartLine - 1 and SkipReadTemp == 0:
                    LineContent.append(FileLine)
                    SkipReadTemp = SkipRead
                    LineLimit = LineLimit - 1
                    LineCount = LineCount + 1
                    FileLine = File.readline()
                    #FileLine = PurifyLine(FileLine)
                    continue
                if LineCount > StartLine - 1 and SkipReadTemp >= 1:
                    SkipReadTemp = SkipReadTemp - 1
                LineLimit = LineLimit - 1
                LineCount = LineCount + 1
                FileLine = File.readline()
                #FileLine = PurifyLine(FileLine)
            return LineContent
    finally:
        File.close()

#Function: Keep line string only and remove specific content from a line
def PurifyLine(Line, ExtraPurifyCode = ''):
    if not Line:
        return Line
    Line = Line.replace('\n', '')
    Line = Line.replace('\r', '')
    Line = Line.replace('\t', '')
    Line = Line.lstrip()
    Line = Line.rstrip()
    if ExtraPurifyCode != '':
        Line = Line.replace(ExtraPurifyCode, '')
    return Line

#Function: Wrtie line to a file
def WriteToFile(FileLoc, InputLine, DeleteBeforeWrite = False):
    if DeleteBeforeWrite is True:
        FileStatus = os.path.isfile(FileLoc)
        if FileStatus is True:
            os.remove(FileLoc)
    File = open(FileLoc, 'a')
    try:
        File.write(InputLine + '\n')
    finally:
        File.close()