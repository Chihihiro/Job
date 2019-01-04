#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/2 0002 14:07 
# @Author : Chihiro 
# @Site :  
# @File : EXCEL.py 
# @Software: PyCharm


lis1 = [1, 2, 3]
lis2 = ["a", "b", "c"]
lis3 = ["A", "B"]

# zip(*iterable)
print(list(zip(lis1, lis2, lis3)))

# 导入模块 xlrd  --> excel read
import xlrd

# step1:打开工作簿
work_book = xlrd.open_workbook("file/秦时明月弟子信息.xlsx")

# step2:获取工作表
sheet1 = work_book.sheets()[0]
# sheet1 = work_book.sheets()  -- 列表  需要索引
# sheet2 = work_book.sheet_by_index(0)  -- 通过位置查找  从0开始
# sheet3 = work_book.sheet_by_name("弟子属性") -- 通过工作表名称查找

# 获取最大行数 最大列数
max_row = sheet1.nrows
max_col = sheet1.ncols
# print("共有", max_row, "行")
# print("共有", max_col, "列")

# 读取内容  1) 按行读取   2)按列读取
for r in range(max_row):
    # 获取每一行数据  sheet.row_values(n)
    value = sheet1.row_values(r)
    print(value)

for c in range(max_col):
    # 获取每一行数据  sheet.row_values(n)
    value = sheet1.col_values(c)
    print(value)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from openpyxl import Workbook

# 实例化工作簿
work_book = Workbook()
# 激活工作表 / 添加工作表
sheet = work_book.active
# 修改工作表名称
sheet.title = "new"
data = [
    [1, "张三", "男"],
    [2, "李四", "女"],
    [3, "王五", "女"],
]
# 写入数据
for each in data:
    sheet.append(each)

# 保存为本地文件
work_book.save("result.xlsx")
# 关闭工作簿
work_book.close()

"""
    科学计算库:  Numpy Scipy
    数据分析库:  Pandas
    图标库:     Matplotlib  Pyecharts
"""

