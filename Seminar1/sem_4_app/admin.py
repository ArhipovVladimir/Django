from django.contrib import admin
# from .models import Category, Product
from sem_3_app.models import Article, Comment, Author

#
#
# @admin.action(description="Сбросить количество в ноль")
# def reset_quantity(modeladmin, request, queryset):
#     queryset.update(quantity=0)
#
#
class AuthorAdmin(admin.ModelAdmin):
    """Список авторов"""
    list_display = ['name', 'birthday']
    ordering = ['name', 'birthday']
    # list_filter = ['date_added', 'price']
#     search_fields = ['description']
#     search_help_text = 'Поиск по полю Описание продукта (description)'
#     actions = [reset_quantity]
#
    """Отдельный автор."""
    fields = ['name', 'surname', 'email', 'birthday']
    readonly_fields = ['email', 'birthday']
#     fieldsets = [
#         (
#             None,
#             {
#                 'classes': ['wide'],
#                 'fields': ['name'],
#             },
#         ),
#         (
#             'Подробности',
#             {
#                 'classes': ['collapse'],
#                 'description': 'Категория товара и его подробное   описание',
#                         'fields':['category', 'description'],
#         },
#         ),
#         (
#             'Бухгалтерия',
#             {
#                 'fields': ['price', 'quantity'],
#
#             }
#         ),
#         (
#             'Рейтинг и прочее',
#             {
#                 'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
#                                             'fields': ['rating', 'date_added'],
#             }
#         ),
#     ]
#


class CommentAdmin(admin.ModelAdmin):
    """Список комментариев"""
    list_display = ['author', 'modify_date']
    ordering = ['author', '-modify_date']
    # list_filter = ['date_added', 'price']


class ArticleAdmin(admin.ModelAdmin):
    """Список комментариев"""
    list_display = ['head', 'author', 'public', 'public_date']
    ordering = ['-author', 'head', 'public', '-public_date']


#
#
# admin.site.register(Category)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
