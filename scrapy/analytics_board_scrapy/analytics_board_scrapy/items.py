# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnalyticsBoardScrapyItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    keyword_counts = scrapy.Field()
    image_counts = scrapy.Field()
    internal_links = scrapy.Field()
    afi_links = scrapy.Field()