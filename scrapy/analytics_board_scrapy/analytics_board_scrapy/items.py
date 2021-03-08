# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnalyticsBoardScrapyItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
    keyword_counts = scrapy.Field()