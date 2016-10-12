from django.shortcuts import render,get_list_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import Content
# Create your views here.
3
def index(request):
    limit=20
    contents=Content.objects.filter(isMedia=True);
    paginator=Paginator(contents,limit)
    page = request.GET.get('page')  # 获取页码
    try:
        topics = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        topics = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        topics = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render(request=request,template_name="index.html",context={'topics':topics})

