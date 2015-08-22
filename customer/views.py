# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from models import Customer, Company
from django.core.exceptions import ObjectDoesNotExist
from tab2.models import Article


def bind(requests):
    if requests.method == 'GET':
        return render_to_response('个人用户_绑定.html', {'open_id': requests.GET['open_id']})
    else:
        name = requests.POST['name']
        email = requests.POST['email']
        open_id = requests.POST['open_id']
        if name is not None and email is not None and open_id is not None:
            try:
                Customer.objects.get(name=name)
                return render_to_response('error.html')
            except ObjectDoesNotExist:
                try:
                    Customer.objects.get(open_id=open_id)
                    return render_to_response('error.html')
                except ObjectDoesNotExist:
                    Customer.objects.create(
                        name=name,
                        email=email,
                        open_id=open_id
                    ).save()
                    return render_to_response('success.html', {'open_id': open_id})
        else:
            return render_to_response('个人用户_绑定.html', {'open_id': open_id})


def company(requests):
    if requests.method == 'GET':
        return render_to_response('企业用户_绑定.html', {'open_id': requests.GET['open_id']})
    else:
        name = requests.POST['name']
        email = requests.POST['email']
        num = requests.POST['num']
        open_id = requests.POST['open_id']
        introduction = requests.POST['introduction']
        if name is not None and email is not None and open_id is not None and num is not None:
            if introduction is not None:
                try:
                    Company.objects.get(name=name)
                    return render_to_response('error.html')
                except ObjectDoesNotExist:
                    try:
                        Company.objects.get(open_id=open_id)
                    except ObjectDoesNotExist:
                        Company.objects.create(
                            name=name,
                            email=email,
                            open_id=open_id,
                            num=num,
                            introduction=introduction,
                        ).save()
                        return render_to_response('success.html')
            else:
                return render_to_response('企业用户_绑定.html', {'open_id': open_id})
        else:
            return render_to_response('企业用户_绑定.html', {'open_id': open_id})


def get_customer_info(requests):
    if requests.method == 'GET':
        customer_id = requests.GET['id']
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('个人用户_绑定.html', {'open_id': open_id})
        if int(user.id) == int(customer_id):
            return render_to_response('我的资料.html', {'user':user})
        else:
            try:
                customer = Customer.objects.get(id=customer_id)
                return render_to_response('TA的资料.html', {'customer': customer, 'user': user})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
    else:
        return render_to_response('error.html')


def get_customer_articles(requests):
    if requests.method == 'GET':
        customer_id = requests.GET['id']
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('个人用户_绑定.html', {'open_id': open_id})
        if int(user.id) == int(customer_id):
            try:
                articles = Article.objects.filter(author=user)
                return render_to_response('我发布的.html', {'articles': articles, 'user': user})
            except ObjectDoesNotExist:
                return render_to_respinse('error.html')
        else:
            try:
                customer = Customer.objects.get(id=customer_id)
                articles = Article.objects.filter(author=customer)
                if len(articles) >0:
                    return render_to_response('TA发布的.html', {'customer': customer, 'user': user, 'articles':articles})
                else:
                    return render_to_response('TA发布的_无.html', {'customer': customer, 'user': user, 'articles':articles})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
    else:
        return render_to_response('error.html')


def change_intro(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('我的资料_修改.html', {'open_id': open_id})
        return render_to_response('我的资料_修改.html', {'user': user})
    else:
        open_id = requests.POST['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('我的资料_修改.html', {'open_id': open_id})
        name = (requests.POST['name'], user.name)
        email = (requests.POST['email'], user.email)
        qq = (requests.POST['qq'], user.qq)
        introduction = (requests.POST['introduction'], user.introduction)
        try:
            customer = Customer.objects.get(name=name)
        except ObjectDoesNotExist:
            customer = None
        if customer is None or customer.open_id == open_id:
            user.email = email
            user.introduction = introduction
            user.name = name
            user.qq =qq
            return render_to_response('我的资料.html', {'open_id': open_id})
        else:
            return render_to_response('error.html')
