# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 09:57
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1024, verbose_name='文章内容'),
        ),
    ]