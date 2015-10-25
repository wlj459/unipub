# -*- coding:utf-8 -*-
from django.contrib import admin

from models import *


class SearchAdmin(admin.ModelAdmin):
    search_fields = ('customer__name', )
    list_display = ('phone_num', 'email',  'customer')


class EmailAdmin(admin.ModelAdmin):
    search_fields = ('email', )
admin.site.register(Business)
admin.site.register(ContactUs, SearchAdmin)
admin.site.register(GetBook, EmailAdmin)
