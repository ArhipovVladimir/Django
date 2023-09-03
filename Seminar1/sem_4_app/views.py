from django.shortcuts import render, redirect
from . import forms
from sem_4_app import views_4_sem as views
from sem_3_app import models


def choice(request):
    if request.method == 'POST':
        form = forms.ChoiceForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'd':
                return views.dice(request, count=count)
            elif game == 'r':
                return redirect('random_num', count=count)
            elif game == 'c':
                return views.heads_or_tails(request, count=count)
    else:
        form = forms.ChoiceForm()

    return render(request, 'sem_4_app/choice.html', {'form': form})


def author_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = models.Author(name=form.cleaned_data['name'],
                                   surname=form.cleaned_data['surname'],
                                   email=form.cleaned_data['email'],
                                   biography=form.cleaned_data['biography'],
                                   birthday=form.cleaned_data['birthdate'])
            author.save()
            message = 'Автор успешно сохранен'
    else:
        form = forms.AuthorForm()

    return render(request, 'sem_4_app/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение автора'})


def post_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            article = models.Article(head=form.cleaned_data['title'],
                               content=form.cleaned_data['content'],
                               author=form.cleaned_data['author'],
                               category=form.cleaned_data['category'],
                               public =form.cleaned_data['public'])
            article.save()
            message = 'Пост успешно сохранен'
    else:
        form = forms.ArticleForm()

    return render(request, 'sem_4_app/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение поста'})


def comment_form(request, article_id):
    message = ''
    article = models.Article.objects.filter(pk=article_id).first()
    comments = models.Comment.objects.filter(article=article)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(author=form.cleaned_data['author'],
                                     content=form.cleaned_data['comment'],
                                     article=article)
            comment.save()
            message = 'Комментарий добавлен'
            form = forms.CommentForm()
    else:
        form = forms.CommentForm()

    return render(request, 'sem_4_app/add_comment.html',
                  {'post': article, 'comments': comments, 'form': form, 'message': message,
                   'title': 'Добавление комментария'})