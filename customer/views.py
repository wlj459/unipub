# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from models import Customer, School, Head, Province
from django.core.exceptions import ObjectDoesNotExist
from tab2.models import Article
from json import dumps


def bind(requests):
    schools = School.objects.all()
    lists = Head.objects.all()
    if requests.method == 'GET':
        return render_to_response('个人用户_绑定.html',
                                  {'open_id': requests.GET['open_id'], 'category': requests.GET['category'],
                                   'schools': schools, 'list': lists})
    else:
        name = requests.POST['name']
        email = requests.POST['email']
        open_id = requests.POST['open_id']
        school_id = requests.POST['school']
        head_id = requests.POST['userphoto']
        integral = 200
        print school_id
        print len(school_id)
        if school_id is not None and len(school_id) != 0:
            try:
                school = School.objects.get(id=school_id)
                integral = 250
            except ObjectDoesNotExist:
                school = None
        else:
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
                    try:
                        head = Head.objects.get(id=head_id)
                    except ObjectDoesNotExist:
                        return render_to_response('error.html', {'content': u'还没有选择头像哦'})
                    Customer.objects.create(
                        name=name,
                        email=email,
                        open_id=open_id,
                        permission=True,
                        integral=integral,
                        head=head,
                        school=school,
                    ).save()
                return HttpResponseRedirect(
                    '/news/time_line?open_id=' + str(open_id) + '&category=' + requests.POST['category'])
        else:
            return render_to_response('个人用户_绑定.html',
                                      {'open_id': open_id, 'category': requests.POST['category'],
                                       'schools': schools, 'list': lists})


def company(requests):
    lists = Head.objects.all()
    if requests.method == 'GET':
        return render_to_response('企业用户_绑定.html',
                                  {'open_id': requests.GET['open_id'], 'category': requests.GET['category'],
                                   'list': lists})
    else:
        name = requests.POST['name']
        email = requests.POST['email']
        num = requests.POST['num']
        open_id = requests.POST['open_id']
        introduction = requests.POST['introduction']
        head_id = requests.POST['userphoto']
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
                        try:
                            head = Head.objects.get(id=head_id)
                        except ObjectDoesNotExist:
                            return render_to_response('error.html', {'content': u'你还没有选择头像哦'})
                        Customer.objects.create(
                            name=name,
                            email=email,
                            open_id=open_id,
                            num=num,
                            introduction=introduction,
                            type=True,
                            integral=200,
                            head=head,
                        ).save()

                return HttpResponseRedirect(
                    '/news/time_line?open_id=' + str(open_id) + '&category=' + requests.POST['category'])
            else:
                return render_to_response('企业用户_绑定.html',
                                          {'open_id': open_id, 'category': requests.POST['category'], 'list': lists})
        else:
            return render_to_response('企业用户_绑定.html',
                                      {'open_id': open_id, 'category': requests.POST['category'], 'list': lists})


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
                return render_to_response('page-我发布的.html',
                                          {'articles': article_list, 'user': user, 'lastPage': lastPage})
            except ObjectDoesNotExist:
                return render_to_response('error.html')
        else:
            try:
                if len(articles) > 0:
                    return render_to_response('page-TA发布的.html',
                                              dict(customer=customer, user=user, articles=article_list,
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


def change_head(requests):
    lists = Head.objects.all()
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        print open_id
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('customer/customer_bind?open_id=' + str(open_id))
        return render_to_response('修改头像.html', {'open_id': open_id, 'user': user, 'list': lists})
    else:
        open_id = requests.POST['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('customer/customer_bind?open_id=' + str(open_id))
        head_id = requests.POST['userphoto']
        try:
            head = Head.objects.get(id=head_id)
        except ObjectDoesNotExist:
            return render_to_response('error.html', {'content': u'还没有选择头像哦'})
        user.head = head
        user.save()
        return HttpResponseRedirect('/customer/get/intro?id=' + str(user.id) + '&open_id=' + str(user.open_id))


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
            return HttpResponseRedirect('/customer/get/articles?id=' + str(user.id) + '&open_id=' + str(user.open_id))
        except ObjectDoesNotExist:
            return render_to_response('error.html')


def get_province(requests):
    if requests.method == 'POST':
        status = '1'
        lists = []
    else:
        lists = Province.objects.all()
        provinces = []
        for i in lists:
            provinces.append({'id': i.id, 'province': i.name})
        status = '0'
    return HttpResponse(dumps({'list': provinces, 'status': status}, ensure_ascii=False),
                        content_type='application/json')


def get_school(requests):
    if requests.method == 'POST':
        status = '1'
        lists = []
    else:
        province_id = requests.GET['province']
        if province_id is not None and len(province_id) > 0:
            try:
                province = Province.objects.get(id=province_id)
            except ObjectDoesNotExist:
                status = '1'
                lists = []
                return dumps({'list': lists, 'status': status})
            lists = School.objects.filter(province=province).order_by('-id')
            schools = []
            for i in lists:
                schools.append({'id': i.id, 'school': i.name})
            status = '0'
        else:
            status = '1'
            lists = []
    return HttpResponse(dumps({'list': schools, 'status': status}, ensure_ascii=False), content_type='application/json')
