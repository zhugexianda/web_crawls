#-*- coding:utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from Douban.items import DoubanItem

class DoubanMovie(Spider):
    name = 'douban'
    headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

    def start_requests(self):
        url='https://movie.douban.com/top250'
        yield Request(url,headers=self.headers)
    
    def parse(self,response):
        item = DoubanItem()
        movies=response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item["排名"]=movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item["名字"]=movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item["导演"]=movie.xpath('.//p[@class=""]/text()[1]').extract_first().strip().split(' ')[1]
#            item["主演"]=movie.xpath('.//p[@class=""]/text()[1]').extract_first().strip().split(' ')[1]
            item["年份"]=movie.xpath('.//p[@class=""]/text()[2]').extract_first().split('/')[0].strip()
            item["国家"]=movie.xpath('.//p[@class=""]/text()[2]').extract_first().split('/')[1].strip()
            item["类型"]=movie.xpath('.//p[@class=""]/text()[2]').extract_first().split('/')[2].strip()
            item["评分"]=movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item["评价"]=movie.xpath('.//p[@class="quote"]/span/text()').extract()[0]
            yield item
        next_url=response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url='https://movie.douban.com/top250'+ next_url[0]
            yield Request(next_url,headers=self.headers) 
