# -*- coding:utf-8 -*-
from django import forms


class BusinessForm(forms.Form):
    user_name = forms.CharField()
    contact = forms.CharField()
    company_name = forms.CharField()
    cooperation_way = forms.CharField()
    others = forms.CharField()


class GetBookForm(forms.Form):
    email = forms.CharField()
    phone_num = forms.CharField()


class ContactUsForm(forms.Form):
    email = forms.CharField()
    phone_num = forms.CharField()
    message = forms.CharField()