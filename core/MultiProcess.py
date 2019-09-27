#!usr/bin/env Python3
# -*- coding:utf-8 -*-
# Author : QYH
# core/MultiProcess.py

import os
import logging
from multiprocessing import Process,Pool,get_logger,log_to_stderr


class MultiProcessPool:
    # 通过ProcessPool的方式实现多线程
    def __init__(self,pool_size=3):
        # MultiProccessPool类的构造函数
        # pool_size为进程池的size
        self.pool_size = pool_size
        self.result_list = []

    def set_pool_size(self,pool_size):
        self.pool_size=pool_size
    
    def set_url_list(self,url_list):
        self.url_list = url_list
    
    def get_pool_size(self):
        return self.pool_size

    def get_url_list(self):
        return self.url_list 
    
    def get_result_list(self):
        return self.result_list

    def run(self,func,para_list):
        '''运行多进程'''
        p = Pool(self.pool_size)
        for para in para_list:
            logging.debug(f'now executing for the url:{para}')
            self.result_list.append(p.apply_async(func,args=(para,)))
        for result in self.result_list:
            print(result.get())




        
        
