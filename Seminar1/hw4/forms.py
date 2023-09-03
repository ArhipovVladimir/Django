from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите назв продукта'}))
    description = forms.CharField(max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите описание продукта'}))

    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField()
