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
            # キーワード数
            all_text=soup.find(class_="entry-content cf")
            # 画像数
            img_src = []
            all_img=all_text.find_all('img')
            for img in all_img:
                img_src.append(img['src'])
            # 内部リンク数
            internal_link_list=[]
            all_internal_link=all_text.find_all('a', href=re.compile('^https://su-gi-rx.com/archives/'))
            for link in all_internal_link:
                internal_link_list.append(link.get('href'))
            link_set = set(internal_link_list)
            # アフィリエイトリンク数
            afi_link_list=[]
            all_afi_link=soup.find_all(class_="adsbygoogle")
            # all_link=soup.find_all('iframe', src=re.compile('^https://www.googleadservices.com/pagead/'))
            for link in all_afi_link:
                afi_link_list.append(link)
            yield ABI(
                url=quote.css('a::attr("href")').extract_first().strip(),
                title=quote.xpath('a/section/h1/text()').extract_first().strip(),
                keyword_counts=all_text.text.count('プログラミング'),
                image_counts=len(img_src),
                internal_links=len(link_set),
                afi_links=len(afi_link_list)
            )

        next_page = response.css('li a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(next_page)
        # 次のページをのリクエストを実行する
        yield scrapy.Request(older_post_link, callback=self.parse)
