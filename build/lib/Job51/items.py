# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Job51Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = Field()  # 职位名称
    company = Field()  # 公司名称
    local = Field()  # 工作地点
    salary = Field()  # 薪资
    welfare = Field()  # 福利
    pass


class niyuItem(Item):
    book = Field()
    word = Field()
    hanyu = Field()
    henmei = Field()
    hinshi = Field()
    # word = Field()
    pass


class JobItem(Item):
    job_name = Field()
    company = Field()
    salary = Field()
    welfare = Field()
    pass





