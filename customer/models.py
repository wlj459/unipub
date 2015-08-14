# -*- coding:utf-8 -*-

from django.db import models


class Customer(models.Model):
    name = models.CharField(u'昵称', max_length=100)
    email = models.CharField(u'邮件', max_length=100)
    qq = models.CharField(u'联系方式', max_length=100, blank=True, null=True)
    open_id = models.CharField(u'OpenID', max_length=100)
    introduction = models.TextField(u'个人介绍', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = u'个人用户'
        verbose_name_plural = u'个人用户'

    def __unicode__(self):
        return u'%s' % self.name


class Company(models.Model):
    name = models.CharField(u'公司名称', max_length=100)
    email = models.CharField(u"邮箱", max_length=100)
    num = models.CharField(u"工商号", max_length=100)
    introduction = models.TextField(u"公司简介", max_length=500)
    permission = models.BooleanField(u"是否审核", default=False)
    open_id = models.CharField(u'OpenID', max_length=100)

