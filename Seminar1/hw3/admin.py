
from django.contrib import admin
from .models import Product, Order, Client


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count_products=0)


class ProductAdmin(admin.ModelAdmin):
    """Список Заказов"""
    list_display = ['name', 'quantity']
    ordering = ['quantity']
    list_filter = ['date_add']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание'
    actions = [reset_quantity]

    """отдельный продукт"""
    fields = ['name', 'description', 'quantity', 'image']
    readonly_fields = ['name', 'quantity', 'quantity']

#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     date_add = models.DateField(auto_now=True)
#     quantity = models.IntegerField()
#     image = models.ImageField(upload_to='media/', default='media/')


class OrderAdmin(admin.ModelAdmin):
    """Список Заказов"""
    list_display = ['client', 'date_order']
    ordering = ['date_order']
    # list_filter = ['date_order']
    search_fields = ['date_order']
    search_help_text = 'Поиск по полю дата'


    """отдельный заказ"""
    fields = ['client', 'products', 'date_order']
    readonly_fields = ['client', 'date_order']


# class Order(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     count_products = models.IntegerField()
#     date_order = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)

class ClientAdmin(admin.ModelAdmin):
    """Список слиентов"""
    list_display = ['name', 'date_create']
    ordering = ['date_create']
    search_fields = ['date_order']
    search_help_text = 'Поиск по полю дата'

    """отдельный клиент"""
    fields = ['name', 'email', 'phone', 'adress']
    readonly_fields = ['email', 'phone', 'adress']


# class Client(models.Model):
#     name = models.CharField(max_length=15)
#     email = models.EmailField()
#     phone = models.CharField(max_length=12)
#     adress = models.CharField(max_length=100)
#     date_create = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return f'Name: {self.name}'


admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)

