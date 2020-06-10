# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShangguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    resorce = scrapy.Field()
    writer = scrapy.Field()
    release_time = scrapy.Field()
    content = scrapy.Field()
    news_type = scrapy.Field()

