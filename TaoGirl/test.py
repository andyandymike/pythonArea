from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os
import re
from datetime import datetime
from pymongo import *

def printformat(style=1):
    if style == 1:
        print('--------------------')

def main():
    driver = webdriver.PhantomJS(executable_path='C:\\phantomjs\\bin\\phantomjs.exe')
    driver.get('http://www.fangdi.com.cn/')
    bsObj = BeautifulSoup(driver.page_source, 'lxml')
    allTr = bsObj.findAll('tr',{'class': 'indextabletxt'})
    content = []
    string = ''
    for tr in allTr:
        allTd = tr.findAll('td')
        for td in allTd:
            string += td.string
        string = string.replace(u'\xa0', u'')
        content.append(string)
        string = ''
    content.append(str(datetime.now()))
    fp = open('fang.txt', 'a+', encoding='utf-8')
    fp.write(str(content))
    fp.close()
    mongoRow = {}
    mongoRow['signNum'] = content[0]
    mongoRow['signArea'] = content[1]
    mongoRow['getTime'] = content[2]
    print(mongoRow)

    #mongoClient = MongoClient()
    #mongoDB = mongoClient.fang
    #mongoColl = mongoDB.yishou
    #mongoColl.insert_one(mongoRow)
    #print(mongoRow)

if __name__ == '__main__':
    main()