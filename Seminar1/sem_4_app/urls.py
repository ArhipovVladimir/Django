from django.urls import path
from . import views, views_4_sem

urlpatterns = [
    path('choice/', views.choice, name='choice'),
    path('author/', views.author_form, name='author'),
    path('create_post/', views.post_form, name='create_post'),
    path('add_comment/<int:article_id>/', views.comment_form, name='add_comment'),
    path('random_num/<int:count>/', views_4_sem.random_num, name='random_num'),
]