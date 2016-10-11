#coding:utf-8
import os,sys

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
            body=BeautifulSoup(html,"html5lib",from_encoding="utf-8").find(class_="post-line-list").find_all(class_="panel panel20 post-item post-box")
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
            for l in lists:
                try:
                    title = l.find(class_="cd-middle-image bmiddle").attrs['alt']
                    category = l.find(class_="post-author").find("a").get_text()
                    content = l.find(class_="cd-middle-image bmiddle").attrs['src']
                    source = "http://www.waduanzi.com/gif"
                    # print(title,category,content,source)

                    Content.objects.create(title=title,category=category,content=content,source=source,isMedia=True)

                except:
                    pass

            return "========complete %d page==========="%page
        except:
            return None


url="http://www.waduanzi.com/lengtu/page/%d"


for i in range(11,100):
    urls=url%i
    lists = get_article(urls)

    print(get_content(lists,i))