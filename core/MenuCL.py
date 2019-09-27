#!usr/bin/env Python3
#-*- coding:utf-8 -*-
# Author: QYH
# core/MenuCL.py

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.MultiProcess import MultiProcessPool
from core.Crawler import Crawler

class MenuCL:
    # 命令行菜单类
    def __init__(self):
        self.option = ''
        self.parameter = ''

    def get_option_from_CL(self):
        if '-h' in sys.argv:
            self.menu_help()
        elif '-u' in sys.argv:
            self.menu_url()
        else:
            self.menu_null()

    def menu_help(self):
        print('请输入 -h(帮助) 或 -u <url>(输入url进行爬取)')
    def menu_url(self):
        url_list = sys.argv[sys.argv.index('-u')+1:]
        mpp = MultiProcessPool()
        mpp.run(func = Crawler().get_all_link_to_file,para_list=url_list)
    def menu_null(self):
        self.menu_help()
