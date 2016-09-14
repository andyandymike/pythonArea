from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os
import threading
import re

def checkFile(file):
    if os.path.isfile(file):
        os.remove(file)

def main():
    driver = webdriver.PhantomJS(executable_path='C:\\phantomjs\\bin\\phantomjs.exe')
    driver.get("https://mm.taobao.com/search_tstar_model.htm?")
    bsObj = BeautifulSoup(driver.page_source, "lxml")
    checkFile('mm.txt')
    fp = open('mm.txt','a+',encoding='utf-8')
    content = driver.find_element_by_id('J_GirlsList').text
    fp.write(content)
    fp.close()
    print("[*]OK GET MM's BOOK")
    MMsinfoUrl = bsObj.findAll("a",{"href":re.compile("\/\/.*\.htm\?(userId=)\d*")})#解析出MM的个人主页
    #print(MMsinfoUrl)
    imagesUrl=bsObj.findAll("img",{"data-ks-lazyload":re.compile(".*\.jpg")})#解析出MM的封面图片
    fp = open('mm.txt', 'r+', encoding='utf-8')
    items = fp.readlines()
    content1 = []
    n = 0
    m = 1
    while(n<14):#将MM的信息都集合在同一个容器中，方便查询操作
        content1.append([items[n].strip('\n'),items[m].strip('\n')])
        n += 3
        m += 3
    content2 = []
    for MMinfoUrl in MMsinfoUrl:
        content2.append(MMinfoUrl["href"])
        print(MMinfoUrl)
    contents = [[a, b] for a, b in zip(content1, content2)]

if __name__ == '__main__':
    main()