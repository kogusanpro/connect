import scrapy


class Urldata(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
    keyword_counts = scrapy.Field()