# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import json
from sqlalchemy import create_engine

engine_crawl = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
    'root', 'chihiro123', '47.107.35.189', 3306, 'crawl', ), connect_args={"charset": "utf8"}, echo=True, )

# class Job51Pipeline(object):
#     def __init__(self):
#         # 创建工作簿
#         self.work_book = Workbook()
#         # 激活工作表
#         self.sheet = self.work_book.active
#
#     # 爬虫开始执行 执行的方法
#     def open_spider(self, spider):
#         self.sheet.append(["职位名称", "公司名称", "工作地点", "薪资"])
#
#     # 执行爬虫的时候执行的方法
#     def process_item(self, item, spider):
#         # value = list()
#         self.sheet.append(list(dict(item).values()))
#         # pass
#
#     # 爬虫执行结束后 执行的方法
#     def close_spider(self, spider):
#         # 保存为本地文件
#         self.work_book.save("python职位信息.xlsx")
#         self.work_book.close()

import pandas as pd
from Job51.iosjk import to_sql


def dff_df(df):
    df2 = df.T
    df4 = df2[df2[0] != ""]
    dff = df4.T
    return dff


def clean(x):
    if type(x) is list:
        if x:
            y = [str(i) for i in x]
            return ','.join(y)
        else:

            return None
    else:
        return x


def for_columns(df):
    col = df.columns
    for i in col:
        df[i] = df[i].apply(lambda x: clean(x))
    return df


class riyuPipeline(object):

    def process_item(self, item, spider):
        print(type(item))
        df = pd.DataFrame(dict(item))
        to_sql('nihongo', engine_crawl, df, type="update")
        return item


# sql = 'SELECT * FROM `nihongo`'
# df = pd.read_sql(sql, engine_crawl)
# print(df)
# df.to_excel('日语.xlsx')