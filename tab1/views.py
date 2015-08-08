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
                user_name=form['user_name'],
                contact=form['contact'],
                company_name=form['company_name'],
                cooperation_way=form['cooperation_way'],
                others=form['others'],
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
                email=form.cleaned_data['email'],
                phone_num=form.cleaned_data['phone_num'],
            ).save()
            return render_to_response('留言板A.html', "success")
        else:
            return render_to_response('留言板A.html')


def contact_us(requests):
    if requests.method == 'GET':
        render_to_response('留言板B.html')
    else:
        form = ContactUs(requests.POST)
        if form.is_valid:
            Business.objects.create(
                email=form.cleaned_data['email'],
                phone_num=form.cleaned_data['phone_num'],
                message=form.cleaned_data['message'],
            ).save()
            render_to_response('留言板B.html', "success")
        else:
            render_to_response('留言板B.html')
