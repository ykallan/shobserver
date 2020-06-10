# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ShangguanItem


class SgSpider(scrapy.Spider):
    name = 'sg'
    # allowed_domains = ['1.com']
    start_urls = ['https://export.shobserver.com/home']
    base_https = 'https://export.shobserver.com'

    def parse(self, response):
        news_urls = response.xpath('//li[@class="subsection-li"]/a/@href').getall()
        news_types = response.xpath('//li[@class="subsection-li"]/a/text()').getall()
        for url, news_type in zip(news_urls, news_types):
            yield scrapy.Request(url=self.base_https+url, callback=self.parse_newslist)

    def parse_newslist(self, response):
        news_urls = response.xpath('//div[@class="chengshi_wz_h"]/a/@href').getall()
        for url in news_urls:
            yield scrapy.Request(url=self.base_https+url, callback=self.parse_detail)

        next_pages = response.xpath('//div[@class="page-nav-bar"]/ul/li/a/@href').getall()
        for next_page in next_pages:
            yield scrapy.Request(url=self.base_https+next_page, callback=self.parse_newslist)

    def parse_detail(self, response):
        news_type = response.xpath('//div[@class="weizhi"]/a[last()]/text()').get()
        title = response.xpath('//div[@class="wz_contents"]/text()').get()
        summary = response.xpath('//div[@class="wz_contents1"]/div').get().strip()
        summary = re.findall(r'b>(.*?)<', summary, re.S)[1].strip()
        resorce = response.xpath('//div[@class="fenxiang_zz"]/span[1]/text()').get()
        writer = response.xpath('//div[@class="fenxiang_zz"]/span[2]/text()').get()
        release_time = response.xpath('//div[@class="fenxiang_zz"]/text()[3]').get().strip()

        contents = response.xpath('//div[@class="newscontents"]//text()').getall()
        content = ' '.join(cont.strip() for cont in contents)

        item = ShangguanItem()
        item['title'] =title
        item['summary'] =summary
        item['resorce'] =resorce
        item['writer'] =writer
        item['release_time'] =release_time
        item['content'] =content
        item['news_type'] =news_type

        yield item
