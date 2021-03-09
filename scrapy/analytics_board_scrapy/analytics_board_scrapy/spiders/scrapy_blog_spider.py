import scrapy
import re
from analytics_board_scrapy.items import AnalyticsBoardScrapyItem as ABI
import requests
from bs4 import BeautifulSoup


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['su-gi-rx.com']
    start_urls = ['http://su-gi-rx.com/']

    def parse(self, response):
        for quote in response.css('article.post-list'):
            # 特定キーワードの抽出
            url=quote.css('a::attr("href")').extract_first().strip()
            resp = requests.get(url=url)
            html = resp.content
            soup = BeautifulSoup(html, "lxml")
            all_text=soup.find(class_="entry-content cf").text

            yield ABI(
                url=quote.css('a::attr("href")').extract_first().strip(),
                title=quote.xpath('a/section/h1/text()').extract_first().strip(),
                keyword_counts=all_text.count('プログラミング')
                image_counts=

            )

        next_page = response.css('li a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(next_page)
        # 次のページをのリクエストを実行する
        yield scrapy.Request(older_post_link, callback=self.parse)
