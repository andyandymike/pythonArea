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
    driver = webdriver.PhantomJS(executable_path='C:\\phantomjs\\bin\\phantomjs.exe')  # 浏览器的地址
    driver.get("https://mm.taobao.com/search_tstar_model.htm?")  # 目标网页地址
    bsObj = BeautifulSoup(driver.page_source, "lxml")  # 解析html语言
    checkFile('mm.txt')
    fp = open('mm.txt', 'a', encoding='utf-8')  # 用来将主页上的个人信息存储
    fp.write(driver.find_element_by_id('J_GirlsList').text)


if __name__ == '__main__':
    main()