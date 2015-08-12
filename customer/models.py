# -*- coding:utf-8 -*-

from django.db import models


class Customer(models.Model):
    name = models.CharField('昵称', max_length=100)
    email = models.CharField('邮件', max_length=100)
    qq = models.CharField('联系方式', max_length=100, blank=True, null=True)
    introduction = models.TextField('个人介绍', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = u'个人用户'
        verbose_name_plural = u'个人用户'

    def __unicode__(self):
        return u'%s' % self.name
