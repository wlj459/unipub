# -*- coding:utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response

from models import  Article, Category


def time_line(requests):
    if requests.method == 'GET':
        category_name = requests.GET['category']
        try:
           category = Category.objects.get(name = category_name)
        except ObjectDoesNotExist:
            return render_to_response("error.html")
        try:
            lists = Article.objects.filter(category = category).order_by('-published')
        except ObjectDoesNotExist:
            return render_to_response("error.html")
        lists = lists[0: min(5, len(lists))]
        return render_to_response("学习.html", {"lists": lists})

    else:
        return render_to_response("error.html")