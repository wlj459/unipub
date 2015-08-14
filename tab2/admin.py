# -*- coding:utf-8 -*-

from django.contrib import admin

from models import *


class ArticleAdmin(admin.ModelAdmin):  # 文章类admin后台显示以及tinymce
    list_display = ('title', 'author', 'is_send', 'category', 'published')
    fields = ('title', 'author', 'is_send', 'category', 'content')

    class Media:
        def __init__(self):
            pass

        js = (
            '/yunwen/js/tinymce/tinymce.min.js',
            '/yunwen/js/tinymce/config.js',
        )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
