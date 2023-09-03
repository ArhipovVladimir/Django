from django.shortcuts import render
from .forms import ProductForm
from hw3.models import Product
import logging
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def add_product(request):
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

    return render(request, 'hw4/product.html', {'form': form, 'message': message})

def update_product(request, product_id):
    old_product = Product.objects.filter(pk=product_id).first()
    # user.name = name
    # user.save()
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

    return render(request, 'hw4/product.html', {'form': form, 'message': message})

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
