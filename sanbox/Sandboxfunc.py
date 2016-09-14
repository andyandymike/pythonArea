__author__ = 'AndyLu'

import os
import logging
import time
import random
import platform


logger = logging.getLogger('Log')
if platform.system() == 'Windows':
    PathSplitter = '\\'
else:
    PathSplitter = '/'

#FUnction: Check and initialize env
def Init(ProjectPath):
    FolderStatus = os.path.isdir(ProjectPath + PathSplitter + 'input')
    if FolderStatus is False:
        os.mkdir(ProjectPath + PathSplitter + 'input')
    FolderStatus = os.path.isdir(ProjectPath + PathSplitter + 'output')
    if FolderStatus is False:
        os.mkdir(ProjectPath + PathSplitter + 'output')
    FolderStatus = os.path.isdir(ProjectPath + PathSplitter + 'config')
    if FolderStatus is False:
        os.mkdir(ProjectPath + PathSplitter + 'config')



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


#Function: Read content from a file. Support read specific number of lines, start read from specific line number, skip every specific number of lines
def ReadFromFile(FileLoc, LineLimit = 'ALL', StartLine = 1, SkipRead = 0):
    LineLimit = str(LineLimit)
    if LineLimit.upper() != 'ALL' and not LineLimit.isdigit():
        print('Error: LineCount must be number or ALL')
        logger.error('LineCount must be number or ALL')
        return False
    if StartLine < 1:
        print('Error: StartLine must larger than or equal to 1')
        logger.error('StartLine must larger than or equal to 1')
        return False
    if SkipRead < 0:
        print('Error: SkipRead must larger than or equal to 0')
        logger.error('SkipRead must larger than or equal to 0')
        return False
    FileStatus = os.path.isfile(FileLoc)
    if FileStatus is False:
        print('Error: Fail to find file: ' + FileLoc + ', cannot read it')
        logger.error('Fail to find file: ' + FileLoc + ', cannot read it')
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
                logger.error('LineLimit must larger than or equal to 0')
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


#Function: Get a variable's value from a parameter file. eg: value=3 in param.ini, input(param.ini, value, '='), output 3
def GetValueFromFile(File, VariableName, SpliteCode):
    VariableName = str(VariableName)
    SpliteCode = str(SpliteCode)
    if VariableName == '' or SpliteCode == '':
        print('Error: VariableName and SpliteCode cannot be blank')
        logger.error('VariableName and SpliteCode cannot be blank')
        return False
    Temp = VariableName.split(SpliteCode)
    if len(Temp) > 1:
        RandSuffix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        VariableName = VariableName.replace(SpliteCode, SpliteCode + RandSuffix)
    FileStatus = os.path.isfile(File)
    if FileStatus is False:
        print('Error: Cannot find get value file: ' + File)
        logger.error('Cannot find get value file: ' + File)
        return False
    VariablesList = open(File, 'r')
    HasSpliteCode = False
    FindVariableName = False
    for FileLine in VariablesList:
        FileLine = PurifyLine(FileLine)
        if FileLine.upper().find(VariableName.upper()) == 0:
            FindVariableName = True
            if FileLine.upper().find(SpliteCode.upper()) == -1:
                continue
            HasSpliteCode = True
            Variable = FileLine.split(SpliteCode, 1)
            if len(Variable) == 1:
                return ''
            if len(Variable) == 2:
                return Variable[1]
            if len(Variable) > 2:
                count = 1
                Value = []
                while count < len(Variable) - 1:
                    Value.append(Variable[count])
                    Value.append(SpliteCode)
                    count = count + 1
                Value.append(Variable[count])
                Value = ''.join(Value)
                return Value
    if HasSpliteCode is False and FindVariableName is True:
        print('Successfully find your variable: ' + VariableName + ', but cannot find your splite code: ' + SpliteCode)
        logger.info('Successfully find your variable: ' + VariableName + ', but cannot find your splite code: ' + SpliteCode)
    print('Error: Cannot find ' + VariableName + '\'s value in file ' + File)
    logger.error('Cannot find ' + VariableName + '\'s value in file ' + File)
    return False

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

#Function: Output 1 or 0 depending on input successfully rate
def OutputOnRate(Rate):
    if float(Rate) < 0:
        print('Error: Rate must bigger than 0')
        logger.error('Rate must bigger than 0')
        return False
    RanNum = random.randint(0,100)
    if float(RanNum) <= float(Rate) * 100:
        #print('RanNum=' + str(RanNum) + ' Rate=' + str(float(Rate) * 100))
        return 1
    else:
        return 0


#Function: Get all file names under input folder
def GetAllFileName(FloderPath):
    FolderStatus = os.path.isdir(FloderPath)
    if FolderStatus is False:
        print('Error: Folder Path ' + FloderPath + ' do not exists')
        logger.error('Error: Folder Path ' + FloderPath + ' do not exists')
        return False
    return os.listdir(FloderPath)

#Function: Calculate Dealer invest factor
def CalDealerInvestFactor(DealerInvest, TranslateDealerInvestUpper, TranslateDealerInvestLower, TranslateDealerExceedFactor, TranslateDealerNormalFactor, TranslateDealerBehindFactor):
    if float(DealerInvest) >= float(TranslateDealerInvestUpper):
        return float(TranslateDealerExceedFactor)
    if float(DealerInvest) <= float(TranslateDealerInvestLower):
        return float(TranslateDealerBehindFactor)
    if float(DealerInvest) < float(TranslateDealerInvestUpper) and float(DealerInvest) > float(TranslateDealerInvestLower):
        return float(TranslateDealerNormalFactor)

#Function: Calculate Brand effect factor
def CalBrandEffectFactor(StartBrandEffect, TranslateBrandEffectUpper, TranslateBrandEffectLower, TranslateBrandEffectExceedFactor, TranslateBrandEffectNormalFactor, TranslateBrandEffectBehindFactor):
    if float(StartBrandEffect) >= float(TranslateBrandEffectUpper):
        return float(TranslateBrandEffectExceedFactor)
    if float(StartBrandEffect) <= float(TranslateBrandEffectLower):
        return float(TranslateBrandEffectBehindFactor)
    if float(StartBrandEffect) < float(TranslateBrandEffectUpper) and float(StartBrandEffect) > float(TranslateBrandEffectLower):
        return float(TranslateBrandEffectNormalFactor)

#Function: Calculate second year Brand effect
def CalSecBrandEffect(V1, V2, V3, V4):
    V1 = float(V1) * 25
    V2 = float(V2) * 25
    V3 = float(V3) * 25
    V4 = float(V4) * 25
    return  V1 + V2 + V3 + V4

#Function: Calculate second year Brand effect factor V1
def CalV1(DisplayCustomerNum, TypeADealerNum, TypeBDealerNum, TypeCDealerNum):
    Output = int(TypeADealerNum) + int(TypeBDealerNum) + int(TypeCDealerNum)
    return int(DisplayCustomerNum)/Output

#Function: Calculate second year Brand effect factor V2
def CalV2(TypeAHotelNum, TypeBHotelNum, TypeCHotelNum, TypeDHotelNum, TypeAHotelUserNum, TypeBHotelUserNum, TypeCHotelUserNum, TypeDHotelUserNum):
    Output1 = int(TypeAHotelNum) + int(TypeBHotelNum) + int(TypeCHotelNum) + int(TypeDHotelNum)
    Output2 = int(TypeAHotelUserNum) + int(TypeBHotelUserNum) + int(TypeCHotelUserNum) + int(TypeDHotelUserNum)
    return Output2/Output1

#Function: Calculate second year Brand effect factor V3
def CalV3(TypeADealerNum, TypeBDealerNum, TypeCDealerNum, CoveredTypeADealerNum, CoveredTypeBDealerNum, CoveredTypeCDealerNum):
    Output1 = int(TypeADealerNum) + int(TypeBDealerNum) + int(TypeCDealerNum)
    Output2 = int(CoveredTypeADealerNum) + int(CoveredTypeBDealerNum) + int(CoveredTypeCDealerNum)
    return Output2/Output1

#Function: Calculate second year Brand effect factor V4
def CalV4(TypeAHotelNum, TypeBHotelNum, TypeCHotelNum, TypeDHotelNum, TypeAHotelUserNum, TypeBHotelUserNum, TypeCHotelUserNum, TypeDHotelUserNum, EachTypeAHotelSalesVolume, EachTypeBHotelSalesVolume, EachTypeCHotelSalesVolume, EachTypeDHotelSalesVolume):
    Output1 = int(TypeAHotelNum) * int(EachTypeAHotelSalesVolume)
    Output1 = int(TypeBHotelNum) * int(EachTypeBHotelSalesVolume) + Output1
    Output1 = int(TypeCHotelNum) * int(EachTypeCHotelSalesVolume) + Output1
    Output1 = int(TypeDHotelNum) * int(EachTypeDHotelSalesVolume) + Output1
    Output2 = int(TypeAHotelUserNum) * int(EachTypeAHotelSalesVolume)
    Output2 = int(TypeBHotelUserNum) * int(EachTypeBHotelSalesVolume) + Output2
    Output2 = int(TypeCHotelUserNum) * int(EachTypeCHotelSalesVolume) + Output2
    Output2 = int(TypeDHotelUserNum) * int(EachTypeDHotelSalesVolume) + Output2
    return Output2/Output1

#Function: Calculate Achieve rate
def CalAchieveRate(OriAchieveRate, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, HotelRelatedRate):
    return float(OriAchieveRate) * float(DealerInvestFactor) * float(DealerResourceFactor) * float(BrandEffectFactor) * float(HotelRelatedRate)

#Function: Calculate type of hotel covered dealer number
def CalHotelCoveredDealerNum(CoveredDealerNum, EachTypeDealerTypeHotelNum):
    return int(CoveredDealerNum) * int(EachTypeDealerTypeHotelNum)

#Function: Calculate Output
def CalOutput(CoveredHotelNum, HotelCoveredDealerNum, HotelNum, EachHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4):
    UserNum1 = 0
    UserNum2 = 0
    UserNum3 = 0
    UserNum4 = 0
    CoveredHotelNum = int(CoveredHotelNum)
    HotelCoveredDealerNum = int(HotelCoveredDealerNum)
    HotelNum = int(HotelNum)
    EachHotelSalesVolume = int(EachHotelSalesVolume)
    AchieveRate1 = float(AchieveRate1)
    AchieveRate2 = float(AchieveRate2)
    AchieveRate3 = float(AchieveRate3)
    AchieveRate4 = float(AchieveRate4)
    if CoveredHotelNum < HotelCoveredDealerNum:
        i = 0
        while i < CoveredHotelNum:
            if OutputOnRate(AchieveRate1) == 1:
                UserNum1 = UserNum1 + 1
            i = i + 1
    if CoveredHotelNum >= HotelCoveredDealerNum:
        i = 0
        while i < HotelCoveredDealerNum:
            if OutputOnRate(AchieveRate1) == 1:
                UserNum1 = UserNum1 + 1
            i = i + 1
    if CoveredHotelNum < HotelCoveredDealerNum:
        i = 0
        while i < HotelCoveredDealerNum - CoveredHotelNum:
            if OutputOnRate(AchieveRate2) == 1:
                UserNum2 = UserNum2 + 1
            i = i + 1
    if CoveredHotelNum >= HotelCoveredDealerNum:
        i = 0
        while i < CoveredHotelNum - HotelCoveredDealerNum:
            if OutputOnRate(AchieveRate3) == 1:
                UserNum3 = UserNum3 + 1
            i = i + 1
    if CoveredHotelNum < HotelCoveredDealerNum:
        i = 0
        while i < HotelNum - HotelCoveredDealerNum:
            if OutputOnRate(AchieveRate4) == 1:
                UserNum4 = UserNum4 + 1
            i = i + 1
    Output=['','']
    Output[0] = UserNum1 + UserNum2 + UserNum3 + UserNum4
    Output[1] = int(Output[0]) * EachHotelSalesVolume
    return Output
