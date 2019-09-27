#!usr/bin/env Python3
#-*- coding:utf-8 -*-
# Author: QYH
# core/crawler.py

import os
import time
import requests
import re
from datetime import datetime
from urllib.parse import urlparse
import logging

from bs4 import BeautifulSoup

# 默认头和url
HEADER = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'referer' : 'https://www.baidu.com'
}
URL = 'https://www.baidu.com'

# 配置log
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s:%(processName)-10s:%(message)s',
)

class throttle:
    '''对相同域名的访问添加延迟时间'''
    def __init__(self,delay=2):
        '''# delay为延迟时间'''
        self.delay = delay
        self.domains = {}


    def wait(self,url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay <= 0:
            return
        if last_accessed == None:
            return
        
        sleep_secs = self.delay - (datetime.now()-last_accessed).seconds
        if sleep_secs > 0:
            time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()

class Crawler:
    '''爬取类'''
    def __init__(self,header=HEADER,retries = 5):
        '''url 为url链接，header为请求头，retries为失败重复尝试次数'''
        self.url = ''
        self.retries = retries
        self.header = header
        self.webpage = ''
        self.link_list = []
    
    def get_webpage(self,url=URL,retries=-1):
        '''获取网页'''
        self.url=url
        if retries == -1:
            retries = 5
        throttle().wait(url=self.url)
        response = requests.get(self.url,headers=self.header)
        if response.status_code == 200:
            logging.debug('get_webpage_successful')
            self.webpage=response
            return response
        elif response.status_code>=500 and retries>0:
            logging.debug(f'get_webpage_failed,status code: {response.status_code}, will retry later')
            self.webpage=response
            return self.get_webpage(retries=retries-1)
        else:
            logging.debug('get_webpage failed, will not retry')
            self.webpage=response
            return None
    
    def show_webpage_content(self):
        print(self.webpage.content)
    
    def get_all_links(self,url=URL):
        '''取得网页中所有链接'''
        logging.debug('now running get_all_links')
        page = self.get_webpage(url)
        # pattern = '<.*?*(href=".*?").*?'
        if page:
            # 转换成soup
            page_soup = BeautifulSoup(page.content,"lxml")
            # 找到所有a对象
            for link in page_soup.find_all('a'):
                # 找到所有href条目
                self.link_list.append(link.get('href'))
            # set去重
            link_set = set(self.link_list)
            self.link_list = list(link_set)
            return self.link_list
        else:
            logging.debug('did not get webpage successfully, get_all_links failed.')
            return None
    
    def get_all_link_to_file(self,url=URL):
        '''取得网页中所有链接并写入文件'''
        logging.debug('now running get_all_links_to_file')
        url_name = url
        # 替换字符
        file_name = os.path.join('..',f'db{os.sep}{url_name.replace("/","_").replace(":","-")}.data')
        with open(file_name,'w') as f:
            all_links = self.get_all_links(url)
            for link in all_links:
                f.write(link+'\n')

# Test Code
'''
def main():
    my_crawler = Crawler()
    # my_crawler.get_webpage()
    print(my_crawler.get_all_links())

if __name__ == '__main__':
    main()
'''
