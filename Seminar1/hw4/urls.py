from django.urls import path
from hw4.views import add_product, update_product


urlpatterns = [
     path('add_product/', add_product, name='add_product'),
     path('update_product/<int:product_id>/', update_product, name='update_product'),
     # path('delta/<int:delta>/', get_order_gt, name='get_order_gt'),
     # path('sort/', get_order_sort, name='get_order_sort'),

]