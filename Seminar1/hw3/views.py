from django.shortcuts import render
from .models import Order, Product, Client
from datetime import datetime


def get_orders(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "hw3/orders.html", context)


def get_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    products = Product.objects.filter(order=order)
    # products = Product.objects.select_related()
    context = {
        'order': order,
        'products': products,
    }
    return render(request, "hw3/order.html", context)


def get_order_gt(request, delta):
    order_list = []
    orders = Order.objects.all()
    for order in orders:
        print(order.date_order)
        res_delta = (datetime.now() - order.date_order).days
        if res_delta > delta:
            order_list.append(order)
    context = {
         'delta': delta,
         'orders': order_list,
     }
    return render(request, "hw3/delta.html", context)
