# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    排名 = scrapy.Field()
    名字 = scrapy.Field()
    导演 = scrapy.Field()
#    主演 = scrapy.Field()
    年份 = scrapy.Field()
    国家 = scrapy.Field()
    类型 = scrapy.Field()
    评分 = scrapy.Field()
    评价 = scrapy.Field()
    
