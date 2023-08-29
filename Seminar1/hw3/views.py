from django.shortcuts import render
from .models import Order, Product, Client


def get_orders(request):
    orders = Order.objects.all()
    print(orders)
    context = {"orders": orders}
    return render(request, "hw3/orders.html", context)


def get_order(request, order_id):
    order = Order.objects.filter(pk=order_id).all()
    # print(order)
    # products = Product.objects.filter(order__order=order_id).all()
    products = Product.objects.select_related(order_id)
    print(products)
    context = {
        'order': order,
        'products': products,
    }
    return render(request, "hw3/order.html", context)

