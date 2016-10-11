#coding:utf-8
import os,sys
source="www.laifudao.com"
parent_path = os.path.dirname(os.getcwd())
sys.path.insert(0,parent_path)
os.environ['DJANGO_SETTINGS_MODULE']="ty166.settings"

import django
django.setup()
from cms.models import Content

from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_article(url=""):
    try:
        html=urlopen(url).read()
        try:
            body=BeautifulSoup(html,"html5lib",from_encoding="utf-8").find(class_="articleList").find_all("article")
            return body
        except:
            return None
    except:
        return None
#
# lists=get_article(url=urls)

def get_content(lists,page):
    if lists is not None:
        try:
            for article in lists:
                try:
                    title=article.find("h1").get_text()
                    category=article.find(class_="cats").get_text()
                    content= article.find(class_="article-content").prettify()
                    time=article.find("time").get_text()
                    Content.objects.create(title=title,category=category,content=content,source=source+"_"+time)
                except:
                    pass

            return "========complete %d page==========="%page
        except:
            return None



url="http://www.laifudao.com/wangwen/index_%d.htm"

for i in range(80,1000):
    urls=url%i
    lists = get_article(urls)
    print(get_content(lists,i))



