# -*- coding:utf-8 -*-

from django.contrib import admin

from models import *


class ArticleAdmin(admin.ModelAdmin):  # 文章类admin后台显示以及tinymce
    list_display = ('title', 'show', 'time')
    fields = ('title', 'show', 'content')

    class Media:
        def __init__(self):
            pass

        js = (
            '/static/js/tinymce/tinymce.min.js',
            '/static/js/tinymce/config.js',
        )


admin.site.register(Article, ArticleAdmin)
