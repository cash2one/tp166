# coding:utf-8
import os
import sys

parent_path = os.path.dirname(os.getcwd())
sys.path.insert(0, parent_path)


os.environ['DJANGO_SETTINGS_MODULE'] = "ty166.settings"
import pickle
class Tools():
    def __init__(self):
        pass
    @staticmethod
    def pickle_file(dest, contents):
        f = open(dest, 'wb')
        pickle.dump(contents, f)
        f.close()
    @staticmethod
    def retive_file(source):
        f = open(source, 'rb')
        d = pickle.load(f)
        f.close()
        return d
import django

django.setup()
from cms.models import Content
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlparse

def get_tags_lists(url="http://www.mahua.com/tags"):
    try:
        html = urlopen(url).read()
        try:
            body = BeautifulSoup(html, "html5lib", from_encoding="utf-8").find(class_="main main-tags").find_all("li")

            return body
        except:
            return None
    except:
        return None

def get_last_page(url):
    try:
        html = urlopen(url).read()
        try:
            body = BeautifulSoup(html, "html5lib", from_encoding="utf-8").find(class_="page").find_all("a")


            if "_" in body[5].attrs['href']:
                temp=body[5].attrs['href'].split("_")[1]
                return temp.split(".")[0]
            if "=" in body[5].attrs['href']:
                return body[5].attrs['href'].split("=")[1]
        except:
            return None
    except:
        return None
def get_tags(tags=""):
    data=[]
    for tag in tags:
        try:
            title = tag.find("a").attrs['title']
            url = tag.find("a").attrs['href']
            last_page = get_last_page(url)
            if last_page is None:
                last_page=1
            d=urlparse(url).path.split("/")[2]
            if "_" in d:
                t="http://www.mahua.com/tags/"+(d.split("_"))[0]+"_%d.htm"
                flag=False
            else:
                t="http://www.mahua.com/tags/"+d+"?p=%d"
                flag=True
            # print({'url':t,'title':title,"end_page":last_page,'flag':flag})
            data.append({'url':t,'title':title,"end_page":last_page,'flag':flag})
        except:
            pass
    return data


def get_lists(url=""):
    try:
        html = urlopen(url).read()
        try:
            body = BeautifulSoup(html, "html5lib", from_encoding="utf-8").find(class_="left").find_all(class_="mahua")
            return body
        except:
            return None
    except:
        return None
def get_article(lists=""):
    for l in lists:
        if "mahua" in l.attrs:
            types = l.attrs['joke-type']
            data = {}
            if types == "pic":
                title = l.find(class_="joke-title").get_text()
                isMedia = True
                img = l.find(class_="content").find("img")
                content = None
                if "src" in img.attrs:
                    content = l.find(class_="content").find("img").attrs['src']
                if "mahuaimg" in img.attrs:
                    content = l.find(class_="content").find("img").attrs['mahuaimg']
                data = {'title': title,
                        'isMedia': isMedia,
                        'category': types,
                        'content': content
                        }

            elif types == "gif":
                title = l.find(class_="joke-title").get_text()
                content = l.find(class_="content").find("img").attrs['mahuagifimg']
                isMedia = True
                data = {'title': title,
                        'isMedia': isMedia,
                        'category': types,
                        'content': content
                        }

            elif types == "text":
                title = l.find(class_="joke-title").find("a").get_text()
                content = l.find(class_="content").prettify()
                isMedia = False
                data = {'title': title,
                        'isMedia': isMedia,
                        'category': types,
                        'content': content
                        }
            try:
                Content.objects.create(title=title, category=data['category'], content=content, source=source,isMedia=data['isMedia'])
                print(title,types,source,isMedia,content)
            except:
                print("XX")


        else:
            print("..")
source = "http://www.mahua.com/tags"


# tag_lists = get_tags_lists()
# tags= get_tags(tag_lists)
# # tags=[{"a":1,"b":2},{"a":3,"b":4}]
filename="manhua.txt"
# Tools.pickle_file(filename,tags)
tags=Tools.retive_file(filename)
for tag in tags:
    for i in range(1,int(tag['end_page'])):
        url=tag['url']%i
        print(url)
        lists = get_lists(url)
        content=get_article(lists)



# url="http://www.mahua.com/tags/juhua?p=4"
# lists = get_lists(url)
# get_article(lists)
