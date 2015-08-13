from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Customer, Company


def bind(requests):
    if requests.method == 'GET':
        return render_to_response('.html',)
    else:
        Customer.objects.create(
            name=requests.POST['name'],
            email=requests.POST['email'],
        )
        return render_to_response("success.html")


def company(requests):
    if requests.method == 'GET':
        return render_to_response(".html",)
    else:
        Company.objects.create(
            name=requests.POST['name'],
            email=requests.POST['email'],
            num=requests.POST['num'],
            introduction=requests.POST['introduction']
        )
        return render_to_response("success.html")
