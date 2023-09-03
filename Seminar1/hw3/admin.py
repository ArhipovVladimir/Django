
from django.contrib import admin
from .models import Product, Order, Client


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count_products=0)


# class ProductAdmin(admin.ModelAdmin):
#     """Список продуктов"""
#     list_display = ['name', 'category', 'quantity']
#     ordering = ['category', '-quantity']
#     list_filter = ['date_added', 'price']
#     search_fields = ['description']
#     search_help_text = 'Поиск по полю Описание продукта (description)'
#     actions = [reset_quantity]


class OrderAdmin(admin.ModelAdmin):
    """Список Заказов"""
    list_display = ['date_order']
    ordering = ['date_order']
    list_filter = ['date_order']
    search_fields = ['date_order']
    search_help_text = 'Поиск по полю дата'
    actions = [reset_quantity]

    """отдельный ордер"""
    fields = ['client', 'date_order']
    readonly_fields = ['date_order']

# class Order(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     count_products = models.IntegerField()
#     date_order = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)


admin.site.register(Order, OrderAdmin)
# admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Product)
