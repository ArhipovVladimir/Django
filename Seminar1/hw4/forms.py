from django import forms
from hw3.models import Product


class ProductForm(forms.Form):
    # products = forms.ModelChoiceField(label='Продукты', queryset=Product.objects.all())
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите назв продукта'}))
    description = forms.CharField(max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите описание продукта'}))

    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField()


class ProductFormUpdate(ProductForm):
    products = forms.ModelChoiceField(label='Продукты', queryset=Product.objects.all())

