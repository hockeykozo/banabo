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
pickup_links = soup.findAll("a", href=re.compile("http://news.yahoo.co.jp/pickup/"))

print "===== 今日のPick Up ====="
for link in pickup_links:
    link_url = link.get("href")
    if str(link).count('<img'):
        link.img.decompose()
    #    link.img.unwrap()
    print link.string.encode('utf-8')
    print link_url
