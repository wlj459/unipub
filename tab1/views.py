#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from tab1.form import *
from tab1.models import *


def business(requests):
    if requests.method == 'GET':
        return render_to_response('商务合作.html')
    else:
        form = BusinessForm(requests.POST)
        if form.is_valid:
            Business.objects.create(
                user_name=requests.POST['user_name'],
                contact=request.POST['contact'],
                company_name=request.POST['company_name'],
                cooperation_way=request.POST['cooperation_way'],
                others=request.POST['others'],
            ).save()
            return render_to_response('商务合作.html', "success")
        else:
            return render_to_response('商务合作.html')


def get_book(requests):
    if requests.method == 'GET':
        return render_to_response('留言板A.html')
    else:
        form = GetBook(requests.POST)
        if form.is_valid:
            Business.objects.create(
                email=request.POST['email'],
                phone_num=request.POST['phone_num'],
            ).save()
            return render_to_response('留言板A.html', "success")
        else:
            return render_to_response('留言板A.html')


def contact_us(requests):
    if requests.method == 'GET':
        return render_to_response('留言板B.html')
    else:
        form = ContactUs(requests.POST)
        if form.is_valid:
            Business.objects.create(
                email=request.POST['email'],
                phone_num=request.POST['phone_num'],
                message=request.POST['message'],
            ).save()
            return render_to_response('留言板B.html', "success")
        else:
            return render_to_response('留言板B.html')
