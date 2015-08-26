#-*- coding:utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import render_to_response
from tab1.models import *
from customer.models import Customer


def business(requests):
    if requests.method == 'GET':
        return render_to_response('商务合作.html')
    else:
        Business.objects.create(
            user_name=requests.POST['user_name'],
            contact=requests.POST['contact'],
            company_name=requests.POST['company_name'],
            cooperation_way=requests.POST['cooperation_way'],
            others=requests.POST['others'],
        ).save()
        return render_to_response('success.html', "success")


def get_book(requests):
    if requests.method == 'GET':
        return render_to_response('留言板A.html')
    else:
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
        open_id = ''
        try:
            open_id = requests.POST['open_id']
        except:
            pass
        try:
            user = Customer.objects.get(open_id=open_id)
            if user.permission:
                user.integral += 5
                user.save()
        except ObjectDoesNotExist:
             pass
        return render_to_response('success.html', "success")
