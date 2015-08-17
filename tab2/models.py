# -*- coding:utf-8 -*-

from django.db import models
from customer.models import Customer


class Category(models.Model):
    name = models.CharField(u'类型', max_length=100)

    class Meta:
        verbose_name = u'类型'
        verbose_name_plural = u'类型类'

    def __unicode__(self):
        return u'%s' % self.name


class Article(models.Model):
    title = models.CharField(u'标题名', max_length=300)
    author = models.ForeignKey(Customer, verbose_name=u'作者')
    category = models.ForeignKey(Category, verbose_name=u'类型')
    is_send = models.BooleanField(u'是否显示', default=False)
    published = models.DateTimeField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    clicks = models.IntegerField(u'点击次数', default=0)
    summary = models.CharField(u'文章简介', max_length=300)

    class Meta:
        ordering = ['-published']
        verbose_name = u'文章'
        verbose_name_plural = u'文章类'

    def __unicode__(self):
        return u'%s' % self.title

