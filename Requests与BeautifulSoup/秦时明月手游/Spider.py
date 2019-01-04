# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018年12月29日 13:38
# @Author  : 逗比i
# @Project : Requests与BeautifulSoup
# @File    : Spider.py
# @Software: PyCharm
# @Describe: 

from bs4 import BeautifulSoup
from urllib import request
from 秦时明月手游.GetHtml import get_html
from openpyxl import Workbook


# BeautifulSoup对象
soup = BeautifulSoup(get_html(), "html.parser")
# 获取总模块
main = soup.find("ul", class_="det_main").find_all("li")
# 获取所有信息
data = []

for each_li in main:
    all_tr = each_li.find_all("tr")[1:]
    for each_tr in all_tr[1:]:
        # 每行数据
        row_value = []
        all_td = each_tr.find_all("td")
        # 提取图片地址
        src = all_td[0].find("img")["src"]
        for each_td in all_td[1:]:
            row_value.append(each_td.text)
        print(row_value)

        name = row_value[0]
        # 保存图片到本地
        request.urlretrieve(src, f"image/{name}.jpg")

        data.append(row_value)


# 写入excel文件
wbk = Workbook()
sheet = wbk.active
for each in data:
    sheet.append(each)
wbk.save("秦时明月弟子信息.xlsx")
wbk.close()













