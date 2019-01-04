# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018年12月29日 12:27
# @Author  : 逗比i
# @Project : Requests与BeautifulSoup
# @File    : 1.requests的基本使用.py
# @Software: PyCharm
# @Describe: 

import requests
import chardet

# 准备url  必须要有http:// 或 https://
url = "http://www.baidu.com"

# 请求url  requests.get(url)  /   requests.post(url)
response = requests.get(url)

# 指定编码
code = chardet.detect(response.content)["encoding"]
response.encoding = code

# 获取html代码
html = response.text
print(html)
















