# import requests
# r=requests.get("http://books.toscrape.com/")
# if r.ok:
#     print(r.text)
# else:
#     print("请求失败")

import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
for start_num in range(0,250,25):
    r=requests.get(f"http://movie.douban.com/top250?start={start_num}",headers=headers)
    html=r.text
    soup=BeautifulSoup(html,"html.parser")
    all_titles=soup.findAll("span",attrs={"class":"title"})
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:
            print(title_string)
