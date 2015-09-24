"""unipub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tab1.views import *
from tab2.views import *
from customer.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^business$', business),
    url(r'^contact_us$', contact_us),
    url(r'^get_book$', get_book),
    url(r'^news/time_line$', time_line),
    url(r'^news/time_line/get$', get_time_line),
    url(r'news/get$', get),
    url(r'news/delete$', delete),
    url(r'news/create$', create),
    url(r'news/comment$', comment),
    url(r'news/comment/get$', get_comment),
    url(r'customer/get/intro$', get_customer_info),
    url(r'customer/get/articles$', get_customer_articles),
    url(r'customer/customer_bind$', bind),
    url(r'customer/company_bind$', company),
    url(r'customer/change/intro$', change_intro),
]