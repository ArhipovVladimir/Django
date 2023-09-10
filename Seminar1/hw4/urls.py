from django.urls import path
from hw4.views import add_product, update_product, about


urlpatterns = [
     path('add_product/', add_product, name='add_product'),
     path('update_product/', update_product, name='update_product'),
     path('about/', about, name='about'),
     # path('sort/', get_order_sort, name='get_order_sort'),

]