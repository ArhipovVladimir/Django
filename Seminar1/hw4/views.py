import form as form
from django.shortcuts import render
from .forms import ProductForm, ProductFormUpdate
from hw3.models import Product
import logging
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def add_product(request):
    name = 'Добавление продукта'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image.name)
            product.save()
            message = 'product сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'

    return render(request, 'hw4/product.html', {'form': form, 'message': message, 'name': name})


def update_product(request):
    name = 'Изменение продукта'
    if request.method == 'POST':
        form = ProductFormUpdate(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product = form.cleaned_data['products']
            old_product = Product.objects.filter(pk=product.pk).first()
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
            # old_product(name=name, description=description, price=price, quantity=quantity, image=image.name)
            old_product.name = name
            old_product.description = description
            old_product.price = price
            old_product.quantity = quantity
            old_product.image = image.name
            old_product.save()
            message = 'product сохранён'
    else:
        form = ProductFormUpdate()
        message = 'Заполните форму'

    return render(request, 'hw4/product.html', {'form': form, 'message': message, 'name': name})


def index(request):
    return render(request, 'hw4/index.html')


def about(request):
    return render(request, 'hw4/about.html')

#
#
# user = User.objects.filter(pk=pk).first()
#         user.name = name
#         user.save()



# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#     else:
#         form = ImageForm()
#     return render(request, 'less_4_form/product.html', {'form': form})
