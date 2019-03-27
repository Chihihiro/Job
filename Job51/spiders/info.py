#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/27 0027 14:25 
# @Author : Chihiro 
# @Site :  
# @File : info.py 
# @Software: PyCharm


from scrapy import Selector, Request
from scrapy.spiders import CrawlSpider
# from Job.items import JobItem
from copy import deepcopy


class Job(CrawlSpider):
    name = "job"
    start_urls = [
        "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    ]

    custom_settings = {
        "FEED_URI": "job.json",
        "FEED_FORMAT": "JSON"
    }

    # 首页的解析函数
    def parse(self, response):
        item = JobItem()

        selector = Selector(response)
        mudule = selector.xpath('//div[@id="resultList"]/div[@class="el"]')[1:]

        for each in mudule:
            job_name = each.xpath('./p/span/a/@title').extract()[0]
            company = each.xpath('./span[@class="t2"]/a/@title').extract()[0]
            salary = each.xpath('./span[@class="t4"]/text()').extract()
            if salary:
                salary = salary[0]
            else:
                salary = "面谈"

            item["job_name"] = job_name
            item["company"] = company
            item["salary"] = salary

            detail_url = each.xpath('./p/span/a/@href').extract()[0]

            yield Request(detail_url, callback=self.detail_parse, meta={"index_data": deepcopy(item)})

    def detail_parse(self, response):
        # 接受item
        item = response.meta["index_data"]

        selector = Selector(response)
        welfare = selector.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/span/text()').extract()
        item["welfare"] = ",".join(welfare)

        yield item

