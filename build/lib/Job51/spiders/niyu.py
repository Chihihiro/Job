#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/31 0031 9:01 
# @Author : Chihiro 
# @Site :  
# @File : niyu.py 
# @Software: PyCharm


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/12/28 0028 10:24
# @Author : Chihiro
# @Site :
# @File : riyu.py
# @Software: PyCharm
import scrapy
import re
import json
from scrapy.spiders import CrawlSpider
import time
from Job51.items import niyuItem
from scrapy import Selector


def str_time(zwtime):
    try:
        t = time.strptime(zwtime, '%Y年%m月%d日')
        r = time.strftime('%Y-%m-%d', t)
    except BaseException:
        return None
    else:
        pass
    return r


class TencentpositionSpider(scrapy.Spider):
    """
    单词抓取
    """
    # 爬虫名
    name = "nihongo"
    start_urls = ["http://jp.qsbdc.com/jpword/index.php"]
    # allowed_domains = ['jp.qsbdc.com']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
           'Job51.middlewares.Job51DownloaderMiddleware': 543,
        },
        "ITEM_PIPELINES": {
            'Job51.pipelines.riyuPipeline': 300,
        }
    }

    def parse(self, response):
        print("*"*100)
        selector = Selector(response)
        print(response.body)
        index_url = selector.xpath('/html/body/div[5]/div[2]/table/tbody/tr/td[2]/a/@href').extract()
        print(index_url)
        for each in index_url:
            yield scrapy.Request(response.urljoin(each), callback=self.next_parse)

    def next_parse(self, response):
        """头页目录"""
        print("头页目录")
        first_page = response.xpath('/html/body/div[5]/div[2]/table//tr/td[2]/a[1]/@href').extract()
        index_page = [response.urljoin(url) for url in first_page]
        print(index_page)
        page = response.xpath('/html/body/div[5]/div[2]/table//tr[last()]/td/a/@href').extract()
        print(page)
        if len(page):
            for i in page:
                """加入其他页"""
                other_page = response.urljoin(i)
                print('有第二页' + other_page)
                # index_page.append(other_page)
                yield scrapy.Request(other_page, callback=self.next_parse2)
        print(index_page)
        for each in index_page:
            yield scrapy.Request(each, callback=self.last_parse)

    def next_parse2(self, response):
        """其他页目录"""
        print("其他页目录")
        first_page = response.xpath('/html/body/div[5]/div[2]/table//tr/td[2]/a[1]/@href').extract()
        print(first_page)
        index_page = [response.urljoin(url) for url in first_page]
        for each in index_page:
            yield scrapy.Request(each, callback=self.last_parse)

    def last_parse(self, response):
        """万一有下一页"""
        print('万一有下一页')
        next_page = response.xpath('/html/body/div[5]/div[2]/table//tr[last()]/td/a/@href').extract()
        if next_page:
            for each in next_page:
                next_each = response.urljoin(each)
                yield scrapy.Request(next_each, callback=self.last_parse2)
        print('开始抓取单词')
        book = response.xpath('//*[@id="learn_nav"]/a[2]/text()').extract()
        first_page = response.xpath('//table[@class="table_solid"]')
        word = first_page.xpath('//tr/td[3]/div/span/text()').extract()
        # word2 = first_page.css(' tr td span::text').extract()
        henmei = first_page.xpath('//tr/td[4]/div/span/text()').extract()
        hanyu = first_page.xpath('//tr/td[6]/div/span/text()').extract()
        hinshi = first_page.xpath('//tr/td[7]/text()').extract()[1:]
        item = niyuItem()
        item['book'] = book * len(word)
        item['word'] = word
        item['henmei'] = henmei
        item['hanyu'] = hanyu
        item['hinshi'] = hinshi
        print(item)
        yield item

    def last_parse2(self, response):
        """万一有下一页"""
        print('开始抓取单词')
        book = response.xpath('//*[@id="learn_nav"]/a[2]/text()').extract()
        first_page = response.xpath('//table[@class="table_solid"]')
        word = first_page.xpath('//tr/td[3]/div/span/text()').extract()
        # word2 = first_page.css(' tr td span::text').extract()
        henmei = first_page.xpath('//tr/td[4]/div/span/text()').extract()
        hanyu = first_page.xpath('//tr/td[6]/div/span/text()').extract()
        hinshi = first_page.xpath('//tr/td[7]/text()').extract()[1:]
        item = niyuItem()
        item['book'] = book * len(word)
        item['word'] = word
        item['henmei'] = henmei
        item['hanyu'] = hanyu
        item['hinshi'] = hinshi
        print(item)
        yield item
