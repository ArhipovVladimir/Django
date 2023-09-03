from django.shortcuts import render
from .models import Order, Product, Client
from datetime import datetime, date


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
    corrent_date = date.today()

    for order in orders:
        print(order.date_order)
        res_delta = (corrent_date - order.date_order).days
        if res_delta > delta:
            order_list.append(order)
    context = {
         'delta': delta,
         'orders': order_list,
     }
    return render(request, "hw3/delta.html", context)


def get_order_sort(request):
    order_list_sort = {}
    orders = Order.objects.all()
    corrent_date = date.today()

    for order in orders:
        res_delta = (corrent_date - order.date_order).days
        order_list_sort.setdefault(order, res_delta)
    print(order_list_sort)
    context = {
         'orders': order_list_sort,
     }
    return render(request, "hw3/delta_sort.html", context)
