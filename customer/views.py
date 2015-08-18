from django.shortcuts import render_to_response
from models import Customer, Company
from django.core.exceptions import ObjectDoesNotExist


def bind(requests):
    if requests.method == 'POST':
        return render_to_response('.html', )
    else:
        name = requests.GET['name']
        email = requests.GET['email']
        open_id = requests.GET['open_id']
        if name is not None and email is not None and open_id is not None:
            try:
                Customer.objects.get(name=name)
                return render_to_response("error.html")
            except ObjectDoesNotExist:
                Customer.objects.create(
                    name=name,
                    email=email,
                    open_id=open_id
                ).save()
                return render_to_response("success.html")
        else:
            return render_to_response(".html")


def company(requests):
    if requests.method == 'POST':
        return render_to_response(".html", )
    else:
        name = requests.GET['name']
        email = requests.GET['email']
        num = requests.GET['num']
        open_id = requests.GET['open_id']
        introduction = requests.GET['introduction']
        if name is not None and email is not None and open_id is not None and num is not None:
            if introduction is not None:
                try:
                    Company.objects.get(name=name)
                    return render_to_response("error.html")
                except ObjectDoesNotExist:
                    Company.objects.create(
                        name=name,
                        email=email,
                        open_id=open_id,
                        num=num,
                        introduction=introduction,
                    ).save()
                    return render_to_response("success.html")
            else:
                return render_to_response('.html')
        else:
            return render_to_response('.html')


def get_customer(requests):
    if requests.method == 'GET':
        customer_id = requests.GET['id']
        try:
            customer = Customer.objects.get(id=customer_id)
            return render_to_response(".html", {'customer': customer})
        except ObjectDoesNotExist:
            return render_to_response("error.html")
    else:
        return render_to_response("error.html")
