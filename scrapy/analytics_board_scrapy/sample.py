import requests
from bs4 import BeautifulSoup
import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

def get_link():

    # driverのセットアップ
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(30)

    url = 'https://su-gi-rx.com/archives/5363'
    # driver.get(url)

    # # ページがロードされ切るまで待機
    # WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
    # html = driver.page_source.encode('utf-8')
    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    resp = requests.get(url)
    html = resp.content
    soup = BeautifulSoup(html, "lxml")

    # 画像数
    all_img=soup.find_all('img')
    for img in all_img:
            print(img['src'])

    # 内部リンク数
    # link_list=[]
    # all_text=soup.find(class_="entry-content cf")
    # all_link=all_text.find_all('a', href=re.compile('^https://su-gi-rx.com/archives/'))
    # for link in all_link:
    #     link_list.append(link.get('href'))
    # link_set = set(link_list)

    # アフィリエイトリンク数
    link_list=[]
    all_text=soup.find_all(class_="adsbygoogle")
    # all_link=soup.find_all('iframe', src=re.compile('^https://www.googleadservices.com/pagead/'))
    for link in all_link:
        link_list.append(link)
    return link_list

if __name__ == '__main__':
    print(len(get_link()))