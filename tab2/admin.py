# -*- coding:utf-8 -*-

from django.contrib import admin

from models import *


class ArticleAdmin(admin.ModelAdmin):  # 文章类admin后台显示以及tinymce
    list_display = ('title', 'author', 'is_send', 'category', 'published')
    search_fields = ('title', 'author__name')
    fields = ('title', 'author', 'ad_1', 'ad_2', 'category', 'summary', 'is_send', 'content')

    class Media:
        def __init__(self):
            pass

        js = (
            '/yunwen/js/tinymce/tinymce.min.js',
            '/yunwen/js/tinymce/config.js',
        )


class CommentAdmin(admin.ModelAdmin):  # 文章类admin后台显示以及tinymce
    search_fields = ('author__name', 'article__title')
    list_display = ('author', 'article', 'published', )
    fields = ('author', 'article', 'comment')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
