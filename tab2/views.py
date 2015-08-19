# -*- coding:utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response

from models import Article, Category, Comment
from customer.models import Customer


def time_line(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('个人用户绑定.html')
        category_name = requests.GET['category']
        try:
            category = Category.objects.get(name=category_name)
        except ObjectDoesNotExist:
            return render_to_response("error.html")
        try:
            lists = Article.objects.filter(category=category, is_send=True).order_by('-published')
        except ObjectDoesNotExist:
            return render_to_response("error.html")
        lists = lists[0: min(5, len(lists))]
        return render_to_response("公共课.html", {"lists": lists, 'category': category_name})
    else:
        return render_to_response("error.html")


def get(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('个人用户绑定.html')
        article_id = requests.GET['id']
        try:
            article = Article.objects.get(id=article_id)
            comments = Comment.objects.filter(article=article)
            return render_to_response("公共课_详情.html",
                                      {'article': article, 'category': requests.GET['category'], 'comments': comments})
        except ObjectDoesNotExist:
            return render_to_response("error.html")
    else:
        return render_to_response("error.html")


def comment(requests):
    if requests.method ==
