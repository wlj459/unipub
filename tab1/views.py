#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from tab1.models import *


def business(requests):
    if requests.method == 'GET':
        return render_to_response('商务合作.html')
    else:
        Business.objects.create(
            user_name=requests.POST['user_name'],
            contact=requests.POST['contact'],
            company_name=requests.POST['company_name'],
            cooperation_way=requests.POST['cooperation_way'],
            others=(requests.POST['others'], ''),
        ).save()
        return render_to_response('success.html', "success")


def get_book(requests):
    if requests.method == 'GET':
        return render_to_response('留言板A.html')
    else:
        print requests.POST['phone_num']
        GetBook.objects.create(
            email=requests.POST['email'],
            phone_num=requests.POST['phone_num'],
        ).save()
        return render_to_response('success.html', "success")


def contact_us(requests):
    if requests.method == 'GET':
        return render_to_response('留言板B.html')
    else:
        ContactUs.objects.create(
            email=requests.POST['email'],
            phone_num=requests.POST['phone_num'],
            message=requests.POST['message'],
        ).save()
        return render_to_response('success.html', "success")
