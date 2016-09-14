__author__ = 'AndyLu'

from Sandboxfunc import *
import os
import logging
import time
import platform


ProjectPath = os.path.abspath('.')
if platform.system() == 'Windows':
    PathSplitter = '\\'
else:
    PathSplitter = '/'

InputFolder = ProjectPath + PathSplitter + 'input'
OutputFolder = ProjectPath + PathSplitter + 'output'
ConfigFolder = ProjectPath + PathSplitter + 'config'

#Create log folder and log file
FolderStatus = os.path.isdir(ProjectPath + PathSplitter + 'log')
if FolderStatus is False:
    os.mkdir(ProjectPath + PathSplitter + 'log')
LogSuffix = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
LogFileName = 'LogStart' + LogSuffix + '.log'
LogFileLoc = ProjectPath + PathSplitter + 'log' + PathSplitter + LogFileName

#Create instance of logging
logger = logging.getLogger('Log')
logger.setLevel(logging.DEBUG)
#File handler
fh = logging.FileHandler(LogFileLoc)
fh.setLevel(logging.DEBUG)
#Formatter
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmt)
#Add formatter to handler
logger.addHandler(fh)


if Init(ProjectPath) is False:
    print('Error: SanBox Env has problem')
    logger.error('Error: SanBox Env has problem')
    quit()


EachTypeAHotelSalesVolume = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeAHotelSalesVolume', '=')
EachTypeBHotelSalesVolume = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeBHotelSalesVolume', '=')
EachTypeCHotelSalesVolume = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeCHotelSalesVolume', '=')
EachTypeDHotelSalesVolume = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeDHotelSalesVolume', '=')
StartBrandEffect = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'StartBrandEffect', '=')
TranslateBrandEffectUpper = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateBrandEffectUpper', '=')
TranslateBrandEffectLower = GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateBrandEffectLower', '=')
TranslateBrandEffectExceedFactor=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateBrandEffectExceedFactor', '=')
TranslateBrandEffectNormalFactor=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateBrandEffectNormalFactor', '=')
TranslateBrandEffectBehindFactor=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateBrandEffectBehindFactor', '=')
TranslateDealerInvestUpper=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateDealerInvestUpper', '=')
TranslateDealerInvestLower=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateDealerInvestLower', '=')
TranslateDealerExceedFactor=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateDealerExceedFactor', '=')
TranslateDealerNormalFactor=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateDealerNormalFactor', '=')
TranslateDealerBehindFactor=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TranslateDealerBehindFactor', '=')
OriAchieveRate1=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'OriAchieveRate1', '=')
OriAchieveRate2=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'OriAchieveRate2', '=')
OriAchieveRate3=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'OriAchieveRate3', '=')
OriAchieveRate4=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'OriAchieveRate4', '=')
EachTypeADealerTypeAHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeADealerTypeAHotelNum', '=')
EachTypeADealerTypeBHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeADealerTypeBHotelNum', '=')
EachTypeADealerTypeCHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeADealerTypeCHotelNum', '=')
EachTypeADealerTypeDHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeADealerTypeDHotelNum', '=')
EachTypeBDealerTypeAHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeBDealerTypeAHotelNum', '=')
EachTypeBDealerTypeBHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeBDealerTypeBHotelNum', '=')
EachTypeBDealerTypeCHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeBDealerTypeCHotelNum', '=')
EachTypeBDealerTypeDHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeBDealerTypeDHotelNum', '=')
EachTypeCDealerTypeAHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeCDealerTypeAHotelNum', '=')
EachTypeCDealerTypeBHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeCDealerTypeBHotelNum', '=')
EachTypeCDealerTypeCHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeCDealerTypeCHotelNum', '=')
EachTypeCDealerTypeDHotelNum=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'EachTypeCDealerTypeDHotelNum', '=')
TypeAHotelRelatedRate=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TypeAHotelRelatedRate', '=')
TypeBHotelRelatedRate=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TypeBHotelRelatedRate', '=')
TypeCHotelRelatedRate=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TypeCHotelRelatedRate', '=')
TypeDHotelRelatedRate=GetValueFromFile(ConfigFolder + PathSplitter + 'config.txt', 'TypeDHotelRelatedRate', '=')

AllCitys = GetAllFileName(InputFolder)

for City in AllCitys:
    if City.find('.txt') != -1:
        TypeAHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeAHotelNum', '=')
        TypeBHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeBHotelNum', '=')
        TypeCHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeCHotelNum', '=')
        TypeDHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeDHotelNum', '=')
        TypeADealerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeADealerNum', '=')
        TypeBDealerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeBDealerNum', '=')
        TypeCDealerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'TypeCDealerNum', '=')
        CoveredTypeAHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeAHotelNum', '=')
        CoveredTypeBHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeBHotelNum', '=')
        CoveredTypeCHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeCHotelNum', '=')
        CoveredTypeDHotelNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeDHotelNum', '=')
        CoveredTypeADealerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeADealerNum', '=')
        CoveredTypeBDealerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeBDealerNum', '=')
        CoveredTypeCDealerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CoveredTypeCDealerNum', '=')
        DealerTimeInvest=GetValueFromFile(InputFolder + PathSplitter + City, 'DealerTimeInvest', '=')
        DealerResourceFactor=GetValueFromFile(InputFolder + PathSplitter + City, 'DealerResourceFactor', '=')
        DisplayCustomerNum=GetValueFromFile(InputFolder + PathSplitter + City, 'DisplayCustomerNum', '=')
        CalculateYearNum=GetValueFromFile(InputFolder + PathSplitter + City, 'CalculateYearNum', '=')

        DealerInvestFactor = CalDealerInvestFactor(DealerTimeInvest, TranslateDealerInvestUpper, TranslateDealerInvestLower, TranslateDealerExceedFactor, TranslateDealerNormalFactor, TranslateDealerBehindFactor)
        BrandEffectFactor = CalBrandEffectFactor(StartBrandEffect, TranslateBrandEffectUpper, TranslateBrandEffectLower, TranslateBrandEffectExceedFactor, TranslateBrandEffectNormalFactor, TranslateBrandEffectBehindFactor)

        AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
        AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
        AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
        AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
        TypeAHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeAHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeAHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeAHotelNum)
        OutputA = CalOutput(CoveredTypeAHotelNum, TypeAHotelCoveredDealerNum, TypeAHotelNum, EachTypeAHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
        #print(OutputA)
        OutputFile = OutputFolder + PathSplitter + City.replace('.txt', 'Year1.txt')
        WriteToFile(OutputFile, 'TypeAHotelUserNum=' + str(OutputA[0]), True)
        WriteToFile(OutputFile, 'TypeAHotelSales=' + str(OutputA[1]))

        AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
        AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
        AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
        AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
        TypeBHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeBHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeBHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeBHotelNum)
        OutputB = CalOutput(CoveredTypeBHotelNum, TypeBHotelCoveredDealerNum, TypeBHotelNum, EachTypeBHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
        #print(OutputB)
        WriteToFile(OutputFile, 'TypeBHotelUserNum=' + str(OutputB[0]))
        WriteToFile(OutputFile, 'TypeBHotelSales=' + str(OutputB[1]))

        AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
        AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
        AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
        AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
        TypeCHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeCHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeCHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeCHotelNum)
        OutputC = CalOutput(CoveredTypeCHotelNum, TypeCHotelCoveredDealerNum, TypeCHotelNum, EachTypeCHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
        #print(OutputC)
        WriteToFile(OutputFile, 'TypeCHotelUserNum=' + str(OutputC[0]))
        WriteToFile(OutputFile, 'TypeCHotelSales=' + str(OutputC[1]))

        AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
        AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
        AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
        AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
        TypeDHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeDHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeDHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeDHotelNum)
        OutputD = CalOutput(CoveredTypeDHotelNum, TypeDHotelCoveredDealerNum, TypeDHotelNum, EachTypeDHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
        #print(OutputD)
        WriteToFile(OutputFile, 'TypeDHotelUserNum=' + str(OutputD[0]))
        WriteToFile(OutputFile, 'TypeDHotelSales=' + str(OutputD[1]))

        if int(CalculateYearNum) <= 1:
            continue
        i = 1
        while i < int(CalculateYearNum):
            TypeAHotelUserNum = GetValueFromFile(OutputFolder + PathSplitter + City.replace('.txt', 'Year' + str(i) + '.txt'), 'TypeAHotelUserNum', '=')
            TypeBHotelUserNum = GetValueFromFile(OutputFolder + PathSplitter + City.replace('.txt', 'Year' + str(i) + '.txt'), 'TypeBHotelUserNum', '=')
            TypeCHotelUserNum = GetValueFromFile(OutputFolder + PathSplitter + City.replace('.txt', 'Year' + str(i) + '.txt'), 'TypeCHotelUserNum', '=')
            TypeDHotelUserNum = GetValueFromFile(OutputFolder + PathSplitter + City.replace('.txt', 'Year' + str(i) + '.txt'), 'TypeDHotelUserNum', '=')
            V1 = CalV1(DisplayCustomerNum, TypeADealerNum, TypeBDealerNum, TypeCDealerNum)
            V2 = CalV2(TypeAHotelNum, TypeBHotelNum, TypeCHotelNum, TypeDHotelNum, TypeAHotelUserNum, TypeBHotelUserNum, TypeCHotelUserNum, TypeDHotelUserNum)
            V3 = CalV3(TypeADealerNum, TypeBDealerNum, TypeCDealerNum, CoveredTypeADealerNum, CoveredTypeBDealerNum, CoveredTypeCDealerNum)
            V4 = CalV4(TypeAHotelNum, TypeBHotelNum, TypeCHotelNum, TypeDHotelNum, TypeAHotelUserNum, TypeBHotelUserNum, TypeCHotelUserNum, TypeDHotelUserNum, EachTypeAHotelSalesVolume, EachTypeBHotelSalesVolume, EachTypeCHotelSalesVolume, EachTypeDHotelSalesVolume)
            SecBrandEffect = CalSecBrandEffect(V1, V2, V3, V4)
            BrandEffectFactor = CalBrandEffectFactor(SecBrandEffect, TranslateBrandEffectUpper, TranslateBrandEffectLower, TranslateBrandEffectExceedFactor, TranslateBrandEffectNormalFactor, TranslateBrandEffectBehindFactor)
            DealerInvestFactor = CalDealerInvestFactor(DealerTimeInvest, TranslateDealerInvestUpper, TranslateDealerInvestLower, TranslateDealerExceedFactor, TranslateDealerNormalFactor, TranslateDealerBehindFactor)

            AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
            AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
            AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
            AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeAHotelRelatedRate)
            TypeAHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeAHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeAHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeAHotelNum)
            OutputA = CalOutput(CoveredTypeAHotelNum, TypeAHotelCoveredDealerNum, TypeAHotelNum, EachTypeAHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
            #print(OutputA)
            OutputFile = OutputFolder + PathSplitter + City.replace('.txt', 'Year' + str(i + 1) + '.txt')
            WriteToFile(OutputFile, 'TypeAHotelUserNum=' + str(OutputA[0]), True)
            WriteToFile(OutputFile, 'TypeAHotelSales=' + str(OutputA[1]))

            AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
            AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
            AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
            AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeBHotelRelatedRate)
            TypeBHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeBHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeBHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeBHotelNum)
            OutputB = CalOutput(CoveredTypeBHotelNum, TypeBHotelCoveredDealerNum, TypeBHotelNum, EachTypeBHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
            #print(OutputB)
            WriteToFile(OutputFile, 'TypeBHotelUserNum=' + str(OutputB[0]))
            WriteToFile(OutputFile, 'TypeBHotelSales=' + str(OutputB[1]))

            AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
            AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
            AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
            AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeCHotelRelatedRate)
            TypeCHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeCHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeCHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeCHotelNum)
            OutputC = CalOutput(CoveredTypeCHotelNum, TypeCHotelCoveredDealerNum, TypeCHotelNum, EachTypeCHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
            #print(OutputC)
            WriteToFile(OutputFile, 'TypeCHotelUserNum=' + str(OutputC[0]))
            WriteToFile(OutputFile, 'TypeCHotelSales=' + str(OutputC[1]))

            AchieveRate1 = CalAchieveRate(OriAchieveRate1, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
            AchieveRate2 = CalAchieveRate(OriAchieveRate2, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
            AchieveRate3 = CalAchieveRate(OriAchieveRate3, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
            AchieveRate4 = CalAchieveRate(OriAchieveRate4, DealerInvestFactor, DealerResourceFactor, BrandEffectFactor, TypeDHotelRelatedRate)
            TypeDHotelCoveredDealerNum = CalHotelCoveredDealerNum(CoveredTypeADealerNum, EachTypeADealerTypeDHotelNum) + CalHotelCoveredDealerNum(CoveredTypeBDealerNum, EachTypeBDealerTypeDHotelNum) + CalHotelCoveredDealerNum(CoveredTypeCDealerNum, EachTypeCDealerTypeDHotelNum)
            OutputD = CalOutput(CoveredTypeDHotelNum, TypeDHotelCoveredDealerNum, TypeDHotelNum, EachTypeDHotelSalesVolume, AchieveRate1, AchieveRate2, AchieveRate3, AchieveRate4)
            #print(OutputD)
            WriteToFile(OutputFile, 'TypeDHotelUserNum=' + str(OutputD[0]))
            WriteToFile(OutputFile, 'TypeDHotelSales=' + str(OutputD[1]))

            i = i + 1
