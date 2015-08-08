#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class Business (models.Model):
    user_name = models.CharField(u'用户', max_length=100)
    contact = models.CharField(u'联系方式', max_length=100)
    company_name = models.CharField(u'公司名称', max_length=100)
    cooperation_way = models.CharField(u'合作方式', max_length=300)
    others = models.CharField(u'备注', max_length=300)

    class Meta:
        verbose_name = u'合作'
        verbose_name_plural = u'合作'

    def __unicode__(self):
        return u'%s' % self.user_name


class GetBook(models.Model):
    email = models.CharField(u'邮箱', max_length=100)
    phone_num = models.CharField(u'电话', max_length=100)

    class Meta:
        verbose_name = u'订阅'
        verbose_name_plural = u'订阅'

    def __unicode__(self):
        return u'%s' % self.email


class ContactUs(models.Model):
    phone_num = models.CharField(u'电话', max_length=100)
    email = models.CharField(u'邮箱', max_length=100)
    message = models.CharField(u'留言', max_length=300)

    class Meta:
        verbose_name = u'来信'
        verbose_name_plural = u'来信'

    def __unicode__(self):
        return u'%s' % self.email