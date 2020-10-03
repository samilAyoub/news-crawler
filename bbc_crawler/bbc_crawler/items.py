# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BBCNewsItem(scrapy.Item):
    # Define fields of BBC news items
    title = scrapy.Field()
    summary = scrapy.Field()
    body = scrapy.Field()
    url = scrapy.Field()
