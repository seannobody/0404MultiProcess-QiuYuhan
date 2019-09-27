#!usr/bin/env Python3
#-*- coding:utf-8 -*-
# Author: QYH
# bin/main.py

# Requests:
# 1. 使用类                                                          done
# 2. 添加日志                                                        done
# 3. 保存文件                                                        done
# 3. 可以传入某个url链接，爬取此页面的所有链接地址                      done
# 4. 添加命令行命令，可以直接通过参数执行（至少有帮助和url两个选项）      done

'''
代码结构：
                          main()        主函数
                        /      
                    MenuCL-get_option_from_CL()     菜单（命令行选项）
                      /
                MultiProcess-run()                  进程池运行
                    /
                Crawler-get_all_link_to_file()      爬虫及内容分析+log+文件存储
'''
              
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.MenuCL import MenuCL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def main():
    MenuCL().get_option_from_CL()

if __name__ == "__main__":
    main()