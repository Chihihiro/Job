# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018年12月31日 13:01
# @Author  : Joyce
# @Project : 模拟拖拽网页
# @File    : 1.拖动京东网页.py
# @Software: PyCharm
# @Describe: 

from selenium.webdriver import Chrome
from urllib import request
from scrapy.http.response import urljoin
from scrapy import Selector
from time import sleep
import csv


# 京东首页
jd_url = "https://www.jd.com/"


def get_html():
    # 实例化浏览器
    browser = Chrome()
    browser.maximize_window()

    # 访问url
    browser.get(jd_url)
    sleep(3)

    for i in range(0, 50000, 5):
        # 拖动网页的js代码
        js = f"window.scroll(0,{i})"
        # 执行js脚本
        browser.execute_script(js)

    # 获取html代码
    html = browser.page_source
    # 写入文件中
    file = open("京东.html", "w", encoding="utf-8")
    file.write(html)
    file.close()
    browser.quit()


def parse():
    # 读取html代码
    with open("京东.html", "r", encoding="utf-8") as file:
        content = file.read()

    selector = Selector(text=content)
    shop_list = selector.css("#J_more ul li")

    csv_file = open("京东商品信息.csv", "w", encoding="gbk", newline="")
    writer = csv.writer(csv_file)
    for i, each in enumerate(shop_list):
        name = each.css("a::attr(title)").extract()

        price = each.css("span::text").extract()
        if name and price:
            name = name[0]
            price = price[0]
            value = [name, price]
            writer.writerow(value)
    csv_file.close()


parse()











