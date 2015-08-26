# -*- coding:utf-8 -*-

from django.db import models


class Customer(models.Model):
    name = models.CharField(u'名称', max_length=100)
    email = models.CharField(u"邮箱", max_length=100)
    num = models.CharField(u"工商号", max_length=100, default='')
    qq = models.CharField(u'联系方式', max_length=100, blank=True, null=True, default='')
    introduction = models.TextField(u"简介", max_length=500, blank=True, null=True, default='' )
    permission = models.BooleanField(u"是否审核", default=False)
    type = models.BooleanField(u"是否是企业用户", default=False)
    open_id = models.CharField(u'OpenID', max_length=100)
    integral = models.IntegerField(u'积分', default=50)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

    def __unicode__(self):
        return u'%s' % self.name
