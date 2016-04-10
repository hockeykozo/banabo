# -*- coding: utf-8 -*-
import urllib2 as request
import re
from bs4 import BeautifulSoup
from xml.dom.minidom import parse, parseString

url = "http://www.yahoo.co.jp"
response = request.urlopen(url)
html = response.read().decode("utf-8","replace")
response.close()
soup = BeautifulSoup(html, "html.parser")
#print soup.prettify()

#for link in soup.findAll("a", text=re.compile("http://news.yahoo.co.jp")):
for link in soup.findAll("a", href=re.compile("http://news.yahoo.co.jp/pickup/")):
    link_url = link.get("href")
    print link.string
    print link_url

"""

# 記事タイトルの入った <div> の一覧を取得する ('class' 要素が 'title' のもの)
for title_div in title_divs:
    # <div> の中にある <a> を取り出して内容を表示する
    link = title_div.a
    title = title.href 
    url = link['href']
    msg = u'{title} <{url}>'.format(title=title, url=url)
    print(msg)
"""
