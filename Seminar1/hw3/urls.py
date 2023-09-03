from django.urls import path
from .views import get_order, get_orders, get_order_gt, get_order_sort


urlpatterns = [
     path('orders/', get_orders, name='orders'),
     path('order/<int:order_id>/', get_order, name='get_order'),
     path('delta/<int:delta>/', get_order_gt, name='get_order_gt'),
     path('sort/', get_order_sort, name='get_order_sort'),

]