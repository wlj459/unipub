# -*- coding:utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, HttpResponseRedirect

from models import Article, Category, Comment
from customer.models import Customer

id_list = [6, 7, 8, 9, 10]


def time_line(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        category_id = requests.GET['category']
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect(
                'customer/customer_bind?open_id=' + str(open_id) + '&category=' + category_id)

        if int(category_id) in id_list:
            if user.integral < 200:
                return render_to_response('error.html', {'content': u'您的积分还不够哦，快给我们来信吧'})
        try:
            category = Category.objects.get(id=category_id)
        except ObjectDoesNotExist:
            return render_to_response('error.html', {'content': u'您访问的分类有错误哦~'})
        try:
            lists = Article.objects.filter(category=category, is_send=True).order_by('-published')
        except ObjectDoesNotExist:
            return render_to_response('error.html')

        # lists = lists[0: min(5, len(lists))]
        return render_to_response('公共课.html',
                                  {'lists': lists, 'category': category, 'user': user, 'lists_num': len(lists)})
    else:
        return render_to_response('error.html')


def get_time_line(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        category_id = requests.GET['category']
        page_num = int(requests.GET['page_num'])
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        try:
            category = Category.objects.get(id=category_id)
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        try:
            lists = Article.objects.filter(category=category, is_send=True).order_by('-published')
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        num = len(lists) / 5
        if len(lists) % 5 > 0:
            num += 1
        if page_num < num:
            lists = lists[(page_num - 1) * 5: page_num * 5]
            lastPage = False
        else:
            lists = lists[(page_num - 1) * 5:]
            lastPage = True
        return render_to_response('page-公共课列表.html',
                                  {'lists': lists, 'category': category, 'user': user, 'lists_num': len(lists),
                                   'lastPage': lastPage})
    else:
        return render_to_response('error.html')


def get(requests):
    if requests.method == 'GET':
        open_id = requests.GET['open_id']
        article_id = requests.GET['id']
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        try:
            article = Article.objects.get(id=article_id)
            article.clicks += 1
            article.save()
            comments = Comment.objects.filter(article=article)
            if article.category.id in id_list:
                if user.integral < 200:
                    return render_to_response('error.html', {'content': u'您的积分还不够哦，快给我们来信吧'})
            return render_to_response('公共课_详情.html',
                                      dict(article=article, category=article.category, comments=comments,
                                           user=user, comments_num=len(comments)))
        except ObjectDoesNotExist:
            return render_to_response('error.html')
    else:
        return render_to_response('error.html')


def comment(requests):
    if requests.method == 'GET':
        return HttpResponseRedirect('error.html')
    else:
        open_id = requests.POST['open_id']
        article_id = requests.POST['article_id']
        comment_text = requests.POST['comment']

        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        if open_id is not None and article_id is not None and comment_text is not None:
            try:
                article = Article.objects.get(id=article_id)
            except ObjectDoesNotExist:
                return render_to_response('error.html')
            if article.category.id in id_list:
                if user.integral < 200:
                    return render_to_response('error.html', {'content': u'您的积分还不够哦，快给我们来信吧'})
            Comment.objects.create(
                author=user,
                article=article,
                comment=comment_text,
            ).save()
            return HttpResponseRedirect(
                'news/get?id=' + str(article_id) + '&open_id=' + str(open_id) + '&category=' + str(article.category.id))
        else:
            return render_to_response('error.html')


def create(requests):
    if requests.method == 'GET':
        category = Category.objects.get(id=requests.GET['category'])
        return render_to_response('新建主题.html',
                                  {'open_id': requests.GET['open_id'], 'category':category })
    else:
        open_id = requests.POST['open_id']
        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return render_to_response('error.html')

        if int(requests.POST['category']) in id_list:
            if user.integral < 200:
                return render_to_response('error.html', {'content': u'您的积分还不够哦，快给我们来信吧'})
        title = requests.POST['title']
        category_id = requests.POST['category']
        content = requests.POST['content']
        summary = requests.POST['summary']
        category = Category.objects.get(id=category_id)
        article = Article.objects.create(
            title=title,
            category=category,
            author=user,
            content=content,
            summary=summary,
            is_send=True,
        )
        article.save()
        user.integral += 5
        user.save()
        return HttpResponseRedirect(
            'news/get?id=' + str(article.id) + '&open_id=' + str(open_id) + '&category=' + str(article.category.id))


def get_comment(requests):
    if requests.method == 'POST':
        return render_to_response('error.html')
    else:
        open_id = requests.GET['open_id']
        article_id = requests.GET['article_id']
        page_num = int(requests.GET['page_num'])

        try:
            user = Customer.objects.get(open_id=open_id)
            if not user.permission:
                return render_to_response('error.html', {'content': u'您还没有权限，请等待管理员审批'})
        except ObjectDoesNotExist:
            return render_to_response('error.html')
        article = Article.objects.get(id=article_id)
        comments = Comment.objects.filter(article=article)
        num = len(comments) / 5
        if len(comments) % 5 > 0:
            num += 1
        if page_num < num:
            comments_list = comments[(page_num - 1) * 5: page_num * 5]
            lastPage = False
        else:
            comments_list = comments[(page_num - 1) * 5:]
            lastPage = True

        return render_to_response('page-公共课评论.html',
                                  dict(comments=comments_list, page_num=min(page_num + 1, num), lastPage=lastPage,
                                       user=user))
