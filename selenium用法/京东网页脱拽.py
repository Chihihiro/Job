#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/8 0008 13:06 
# @Author : Chihiro 
# @Site :  
# @File : 京东网页脱拽.py 
# @Software: PyCharm


from selenium.webdriver import Chrome
from urllib import request
from scrapy.http.response import urljoin
from scrapy import Selector
from time import sleep
import csv


# 京东首页
danci = '古筝'
jd_url = f"https://search.jd.com/Search?keyword={request.quote(danci)}&enc=utf-8&spm=a.0.0&pvid=60aa147f26a44161b4f3491cf8ab5ca1"
"https://search.jd.com/Search?keyword=%E5%8F%A4%E7%AD%9D&enc=utf-8&wq=%E5%8F%A4%E7%AD%9D&pvid=baa8b0181aea45d387af9e6ca2273ddd"
"https://search.jd.com/Search?keyword=%E5%8F%A4%E7%AD%9D&enc=utf-8&qrst=1&rt=1&stop=1&spm=a.0.0&vt=2&page=5&s=109&click=0"
# jd_url = 'https://www.jd.com/'


def get_html():
    # 实例化浏览器
    browser = Chrome()
    browser.maximize_window()

    # 访问url
    browser.get(jd_url)
    sleep(3)

    for i in range(0, 10000, 5):
        # 拖动网页的js代码
        js = f"window.scroll(0,{i})"
        print(i)
        sleep(0.001)
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
    # shop_list = selector.css("#J_more ul li")
    shop_list = selector.xpath('//*[@id="J_goodsList"]/ul/li')
    print(shop_list)

    csv_file = open("京东商品信息.csv", "w", encoding="gbk", newline="")
    writer = csv.writer(csv_file)
    for i, each in enumerate(shop_list):
        # name = each.css("a::attr(title)").extract()
        i = i+1
        name = each.xpath(f"//li[{i}]/div/div[3]/a/em/text()").extract()
        print(len(name))
        print(name)
        # price = each.css("span::text").extract()
        price = each.xpath(f"//li[{i}]/div/div[2]/strong/i/text()").extract()
        print(price)
        if name and price:
            name = "".join(name)
            price = price[0]
            value = [name, price]
            writer.writerow(value)
    csv_file.close()

get_html()
# parse()

