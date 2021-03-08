import requests
from bs4 import BeautifulSoup

url="https://su-gi-rx.com/archives/5363"
response = requests.get(url=url)
html = response.content
soup = BeautifulSoup(html, "lxml")
#ここで「書籍情報」内のテキストを全取得
all_text=soup.find(class_="entry-content cf").text
print(all_text.count('プログラミング'))
#ここで取得したテキストを1行ずつ分割してリストに収納
all_text_list=all_text.split("\n")
#リストを1行ずづ読み込んで部分一致する行だけ抽出
# for text in all_text_list:
#     if "プログラミング" in text:
#         print(text)