"""
URL configuration for FWDjango project.

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
from less_3_tmpl.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('less_1_app.urls')),
    path('less2/', include('Less_2_model_app.urls')),
    path('less3/', include('less_3_tmpl.urls')),
    path('', index),
    path('less4/', include('less_4_form.urls')),
    path('less6/', include('less_6_server.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
]
