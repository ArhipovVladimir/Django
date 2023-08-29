from django.http import HttpResponse  # HttpResponse - класс, к-й возвращает http-ответ от сервера клиенту
import logging
from functools import wraps
from datetime import datetime
from random import randint
from django.views import View
# HttpResponse - это класс, экземпляры которого возвращают ответы
# JsonResponse - это класс, к-й позволяет возвращать ответ как json-объект
from django.http import HttpResponse, JsonResponse
# Чтобы передать данные в шаблон, мы можем использовать функцию render из модуля django.shortcuts:
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Author, Article, Comment
# get_object_or_404 позволяет обращаться к БД и получать объекты. Если нет, то django возвращает код 404
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)


def write_log(func):
    @wraps(func)
    def wrapper(request):
        view_name = func.__name__
        # print(view_name)
        client_ip = get_client_ip(request)
        # print(client_ip)
        logger.info(f'=== Page "{view_name}" was visited from ip = {client_ip}')
        return func(request)

    return wrapper


@write_log
def index(request):
    context = {'name': ' Arhipov Vladimir'}
    return render(request, 'sem_3_app/index.html', context)


@write_log
def about(request):
    context = {'datetime': datetime.now(), 'client_ip': get_client_ip(request)}
    return render(request, 'sem_3_app/about.html', context)



# возвращает ip, с которого пришёл request
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # если ip передан через proxy
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    # если открыто
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Задание 3

def coin(request):
    title = 'Бросок монеты'
    temp = randint(1, 2)
    if temp == 1:
        result = 'Решка'
    else:
        result = 'Орел'
    context = {'title': title, 'result': result}
    return render(request, 'sem_3_app/temp_1.html', context)


def cube(request):
    title = 'Бросок кубика'
    throw = randint(1, 6)
    context = {'title': title, 'result': throw}
    return render(request, 'sem_3_app/temp_1.html', context)


def rand100(request):
    title = 'Случайное число'
    random_number = randint(0, 100)
    context = {'title': title, 'result': random_number}
    return render(request, 'sem_3_app/temp_1.html', context)


def get_articles(request, author_id):
    # print(author_id)
    articles = Article.objects.filter(author__pk=author_id)
    # print(len(articles))
    context = {"articles": articles}
    return render(request, "sem_3_app/orders.html", context)


def get_article(request, article_id):
    article = Article.objects.filter(pk=article_id).first()
    article.count += 1
    article.save()
    # все комментарии статьи
    comments = Comment.objects.filter(article=article).order_by('modify_date')
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, "sem_3_app/article.html", context)