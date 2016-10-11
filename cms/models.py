from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name="名称")
    shortcut = models.CharField(max_length=120, unique=True, verbose_name="字母缩写")

    def __str__(self):
        return self.shortcut + "_" + self.name

    class Meta:
        verbose_name_plural = "栏目分类"


class EncodeFormat(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name="编码格式", default="UTF-8")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "编码格式"


class Content(models.Model):
    title = models.CharField(max_length=240, verbose_name="文章标题",db_index=True)

    encodeformat = models.CharField(max_length=120, verbose_name="编码格式", null=True)
    source = models.CharField(max_length=240, verbose_name="来源", null=True, blank=True, db_index=True)
    isMedia = models.BooleanField(default=False, verbose_name="媒体吗", db_index=True)
    content = RichTextUploadingField(verbose_name="文章内容", max_length=1024)
    category= models.CharField(max_length=120,null=True,db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)
    published_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章"
        unique_together=('title','source','content')
