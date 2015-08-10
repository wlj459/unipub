from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    qq = models.CharField(max_length=100, blank=True, null=True)
    introduction = models.TextField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = u'个人用户'
        verbose_name_plural = u'个人用户'

    def __unicode__(self):
        return u'%s' % self.name
