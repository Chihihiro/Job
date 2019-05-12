# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018年12月28日 15:57
# @Author  : 逗比i
# @Project : Job51
# @File    : JobInfo.py
# @Software: PyCharm
# @Describe: 

from scrapy import Selector
from scrapy.spiders import CrawlSpider, Spider
from Job51.items import Job51Item
from scrapy import Request
from copy import deepcopy


class JobInfo(CrawlSpider):
    # 爬虫名称  固定名称 name =
    name = "info"
    # 设置url队列  固定名称!
    start_urls = [
        "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
    ]
    # 计数
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
           'Job51.middlewares.Job51DownloaderMiddleware2': 543,
        },
        "ITEM_PIPELINES": {
            'Job51.pipelines.riyuPipeline': 300,
        }
    }
    counts = 0

    # 解析函数
    def parse(self, response):
        # 实例化item
        item = Job51Item()
        # 构造选择器
        selector = Selector(response)

        # 获取总模块
        result_list = selector.css("#resultList")
        all_list = result_list.xpath('./div[@class="el"]')[1:]
        for each in all_list:
            job_name = "".join(each.xpath('./p/span/a/text()').extract()).strip()
            company = each.xpath('./span[@class="t2"]/a/@title').extract()[0]
            local = each.xpath('./span[@class="t3"]/text()').extract()[0]
            salary = each.xpath('./span[@class="t4"]/text()').extract()
            if salary:
                salary = salary[0]
            else:
                salary = "面谈"

            # 提交字段给item
            item["job_name"] = job_name
            item["company"] = company
            item["local"] = local
            item["salary"] = salary

            # 获取详情页连接
            detail_page = each.xpath('./p/span/a/@href').extract()[0]
            # 提交请求
            yield Request(detail_page, callback=self.detail_parse, meta={"item": deepcopy(item)})

        if self.counts < 10:
            # 获取下一页url
            next_link = selector.xpath('//li[@class="bk"]')[1].xpath('./a/@href').extract()[0]
            self.counts += 1

            # 提交下一页的请求  response.urljoin(url) --> 相对地址转绝对地址
            yield Request(response.urljoin(next_link), callback=self.parse, dont_filter=True)

    def detail_parse(self, response):
        # 接受item
        item = response.meta["item"]
        # 构造Selector
        selector = Selector(response)
        welfare = selector.css(".jtag span::text").extract()
        if welfare:
            welfare = ",".join(welfare)
        else:
            welfare = "暂无介绍"

        # 提交welfare给item
        item["welfare"] = welfare

        # 提交item
        yield item





















