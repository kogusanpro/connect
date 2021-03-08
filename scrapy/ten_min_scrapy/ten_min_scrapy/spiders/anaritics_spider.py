import scrapy
import re
from ten_min_scrapy.items import Urldata
import requests
from bs4 import BeautifulSoup


class AnariticsSpider(scrapy.Spider):
    name = 'anaritics'
    start_urls = [
        'https://su-gi-rx.com/page/1',
    ]

    def parse(self, response):
        for quote in response.css('article.post-list'):
            urls = Urldata()
            urls['url'] = []
            urls['text'] = []
            urls['keyword_counts'] = []
            urls['url'].append(quote.css('a::attr("href")').extract_first().strip())
            urls['text'].append(quote.xpath('a/section/h1/text()').extract_first().strip())
            resp = requests.get(url=urls['url'][0])
            html = resp.content
            soup = BeautifulSoup(html, "lxml")
            #ここで「書籍情報」内のテキストを全取得
            all_text=soup.find(class_="entry-content cf").text
            urls['keyword_counts'].append(all_text.count('プログラミング'))

            yield urls
            # url_list.append(url)

        next_page = response.css('li a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(next_page)
        # 次のページをのリクエストを実行する
        yield scrapy.Request(older_post_link, callback=self.parse)