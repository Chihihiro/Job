#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/2 0002 15:46 
# @Author : Chihiro 
# @Site :  
# @File : tio.py 
# @Software: PyCharm

import os
import xlrd
from openpyxl import Workbook


def load():
    # 所有数据
    data = []
    # 获取所有文件名称
    file_list = os.listdir("./file/")
    for each_file in file_list:
        # 打开工作簿
        work_book = xlrd.open_workbook("./file/"+each_file)
        # 工作表
        sheet = work_book.sheets()[0]
        for row in range(1, sheet.nrows):
            value = sheet.row_values(row)
            data.append(value)
            print(value)

    new_wbk = Workbook()
    new_sheet = new_wbk.active
    for each in data:
        new_sheet.append(each)
    new_wbk.save("./result/"+input("请输入文件名称:     ")+".xlsx")
    new_wbk.close()


load()
