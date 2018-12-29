# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import json


class Job51Pipeline(object):
    def __init__(self):
        # 创建工作簿
        self.work_book = Workbook()
        # 激活工作表
        self.sheet = self.work_book.active

    # 爬虫开始执行 执行的方法
    def open_spider(self, spider):
        self.sheet.append(["职位名称", "公司名称", "工作地点", "薪资"])

    # 执行爬虫的时候执行的方法
    def process_item(self, item, spider):
        # value = list()
        self.sheet.append(list(dict(item).values()))
        # pass

    # 爬虫执行结束后 执行的方法
    def close_spider(self, spider):
        # 保存为本地文件
        self.work_book.save("python职位信息.xlsx")
        self.work_book.close()



