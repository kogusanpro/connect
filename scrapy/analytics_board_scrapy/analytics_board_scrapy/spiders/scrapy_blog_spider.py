import scrapy
import re
from analytics_board_scrapy.items import AnalyticsBoardScrapyItem
import requests
from bs4 import BeautifulSoup


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['su-gi-rx.com']
    start_urls = ['http://su-gi-rx.com/']

    def parse(self, response):
        for quote in response.css('article.post-list'):
            scrapy_items = AnalyticsBoardScrapyItem()
            scrapy_items['url'] = []
            scrapy_items['text'] = []
            scrapy_items['keyword_counts'] = []
            scrapy_items['url'].append(quote.css('a::attr("href")').extract_first().strip())
            scrapy_items['text'].append(quote.xpath('a/section/h1/text()').extract_first().strip())
            # 特定キーワードの抽出
            resp = requests.get(url=scrapy_items['url'][0])
            html = resp.content
            soup = BeautifulSoup(html, "lxml")
            all_text=soup.find(class_="entry-content cf").text
            scrapy_items['keyword_counts'].append(all_text.count('プログラミング'))

            yield scrapy_items

        next_page = response.css('li a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(next_page)
        # 次のページをのリクエストを実行する
        yield scrapy.Request(older_post_link, callback=self.parse)
