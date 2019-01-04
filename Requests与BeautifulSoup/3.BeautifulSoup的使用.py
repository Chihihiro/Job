# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018年12月29日 12:52
# @Author  : 逗比i
# @Project : Requests与BeautifulSoup
# @File    : 3.BeautifulSoup的使用.py
# @Software: PyCharm
# @Describe: 

import re
from bs4 import BeautifulSoup


# 读取HTML代码
def get_html():
    with open("西刺html/index.html", "r", encoding="utf-8") as file:
        content = file.read()
    return content


# 获取html代码
html = get_html()
# 包装成BeautifulSoup对象   解释器: html.parser  lxml  html5lib
soup = BeautifulSoup(html, "html.parser")

# 普通查询  soup.find()  /  soup.find_all()
# 提取文本  节点.text/string/getText()
# 提取属性  节点["属性名称"]

# 查找class属性带有字母d  tag.find(class_=re.compile("正则表达式"))


def find(id_name):
    return "f" in str(id_name)


print(soup.find_all(id=find))








