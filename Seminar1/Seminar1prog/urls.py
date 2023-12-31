"""
URL configuration for Seminar1prog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hw4.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    # path('', include('app1.urls')),
    # path('app2/', include('app_2_1.urls')),
    path('hw1/', include('hw1.urls')),
    path('hw3/', include('hw3.urls')),
    # path('sem2/', include('sem_2_1_app.urls')),
    path('sem3/', include('sem_3_app.urls')),
    path('sem4/', include('sem_4_app.urls')),
    path('hw4/', include('hw4.urls')),

]
