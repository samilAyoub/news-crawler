# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from ..items import BBCNewsItem
from datetime import datetime


class BBCNewsSpider(scrapy.Spider):
    name = "BBC"
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com']

    def parse(self, response):
        new_item = BBCNewsItem()
        if(response.url != self.start_urls[0]):
            new_item['url'] = response.url
            new_item['title'] = response.css('h1::text').get()
            new_item['summary'] = response.css('p b::text').get()
            new_item['body'] = response.css('p::text').getall()
            yield new_item
        else:
            URLs = response.css('div.media a::attr(href)').getall()
            if(len(URLs) != 0):
                for url in URLs:
                    if url != None:
                        absolut_url = response.urljoin(url)
                        yield scrapy.Request(absolut_url, callback=self.parse)
            yield new_item
