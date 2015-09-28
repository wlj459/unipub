# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect
from models import Customer, School
from django.core.exceptions import ObjectDoesNotExist
from tab2.models import Article


def bind(requests):
    schools = School.objects.all()
    if requests.method == 'GET':
        return render_to_response('个人用户_绑定.html',
                                  {'open_id': requests.GET['open_id'], 'category': requests.GET['category'],
                                   'schools': schools})
    else:
        name = requests.POST['name']
        email = requests.POST['email']
        open_id = requests.POST['open_id']
        school_id = requests.POST['school']
        #head_id = requests.POST['head']
        #if head_id is None:
        #     head_id = 1
        integral = 200
        if school_id is None or len(school_id) == 0:
            try:
                school = School.objects.get(id=school_id)
                integral = 250
            except ObjectDoesNotExist:
                school = None
        if name is not None and email is not None and open_id is not None:
            try:
                Customer.objects.get(open_id=open_id)
                return render_to_response('error.html', {'content': u'您已经绑定过了~'})
            except ObjectDoesNotExist:
                try:
                    Customer.objects.get(name=name)
                    return render_to_response('error.html', {'content': u'这个昵称有人用过了哦'})
                except ObjectDoesNotExist:
                    Customer.objects.create(
                        name=name,
                        email=email,
                        open_id=open_id,
                        permission=True,
                        integral=integral,
                    ).save()
                return HttpResponseRedirect(
                    '/news/time_line?open_id=' + str(open_id) + '&category=' + requests.POST['category'])
        else:
            return render_to_response('个人用户_绑定.html',
                                      {'open_id': open_id, 'category': requests.POST['category'],
                                       'schools': schools})


def company(requests):
    if requests.method == 'GET':
        return render_to_response('企业用户_绑定.html',
                                  {'open_id': requests.GET['open_id'], 'category': requests.GET['category']})
    else:
        name = requests.POST['name']
        email = requests.POST['email']
        num = requests.POST['num']
        open_id = requests.POST['open_id']
        introduction = requests.POST['introduction']
        if name is not None and email is not None and open_id is not None and num is not None:
            if introduction is not None:
                try:
                    Customer.objects.get(open_id=open_id)
                    return render_to_response('error.html', {'content': u'您已经注册过了~'})
                except ObjectDoesNotExist:
                    try:
                        Customer.objects.get(name=name)
                        return render_to_response('error.html', {'content': u'这个昵称有人用了哦'})
                    except ObjectDoesNotExist:
                        Customer.objects.create(
                            name=name,
                            email=email,
                            open_id=open_id,
                            num=num,
                            introduction=introduction,
                            type=True,
                            integral=200,
                        ).save()

                return HttpResponseRedirect(
                    '/news/time_line?open_id=' + str(open_id) + '&category=' + requests.POST['category'])
            else:
                return render_to_response('企业用户_绑定.html', {'open_id': open_id, 'category': requests.POST['category']})
        else:
            return render_to_response('企业用户_绑定.html', {'open_id': open_id, 'category': requests.POST['category']})


def get_customer_info(requests):
    if requests.method == 'GET':
        customer_id = requests.GET['id']
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('customer/customer_bind?open_id=' + str(open_id))
        if int(user.id) == int(customer_id):
            return render_to_response('我的资料.html', {'user': user})
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
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('customer/customer_bind?open_id=' + str(open_id))
        if int(user.id) == int(customer_id):
            try:
                articles = Article.objects.filter(author=user)
                return render_to_response('我发布的.html', {'articles': articles, 'user': user})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
        else:
            try:
                customer = Customer.objects.get(id=customer_id)
                articles = Article.objects.filter(author=customer)
                if len(articles) > 0:
                    return render_to_response('TA发布的.html', {'customer': customer, 'user': user, 'articles': articles})
                else:
                    return render_to_response('TA发布的_无.html',
                                              {'customer': customer, 'user': user, 'articles': articles})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
    else:
        return render_to_response('error.html')


def get_customer_articles_get(requests):
    if requests.method == 'GET':
        customer_id = requests.GET['id']
        open_id = requests.GET['open_id']
        page_num = int(requests.GET['page_num'])
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('customer/customer_bind?open_id=' + str(open_id))
        customer = Customer.objects.get(id=customer_id)
        articles = Article.objects.filter(author=customer)
        num = len(articles) / 5
        if len(articles) % 5 > 0:
            num += 1
        if page_num < num:
            article_list = articles[(page_num - 1) * 5: page_num * 5]
            lastPage = False
        else:
            article_list = articles[(page_num - 1) * 5:]
            lastPage = True
        if int(user.id) == int(customer_id):
            try:
                return render_to_response('page-我发布的.html', {'articles': article_list, 'user': user, 'lastPage': lastPage})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
        else:
            try:
                if len(articles) > 0:
                    return render_to_response('TA发布的.html', dict(customer=customer, user=user, articles=article_list,
                                                                 lastPage=lastPage))
                else:
                    return render_to_response('TA发布的_无.html',
                                              {'customer': customer, 'user': user, 'articles': articles})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
    else:
        return render_to_response('error.html')


def change_intro(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('customer/customer_bind?open_id=' + str(open_id))
        return render_to_response('我的资料_修改.html', {'open_id': open_id, 'user': user})
    else:
        open_id = requests.POST['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        name = requests.POST['name']
        email = requests.POST['email']
        qq = requests.POST['qq']
        introduction = requests.POST['introduction']
        try:
            customer = Customer.objects.get(name=name)
        except ObjectDoesNotExist:
            customer = None
        if customer is None or customer.open_id == open_id:
            user.email = email
            user.introduction = introduction
            user.name = name
            user.qq = qq
            user.save()
            return HttpResponseRedirect('customer/get/intro?id=' + str(user.id) + '&open_id=' + str(user.open_id))
        else:
            return render_to_response('error.html', {'content': u'有些信息格式不正确哦'})


def delete(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        delete_id = requests.GET['id']
        try:
            article = Article.objects.get(id=delete_id)
            article.delete()
            return HttpResponseRedirect('customer/get/articles?id=' + str(user.id) + '&open_id=' + str(user.open_id))
        except ObjectDoesNotExist:
            return render_to_response('error.html')
