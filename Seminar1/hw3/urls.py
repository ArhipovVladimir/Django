from django.urls import path
from .views import get_order, get_orders, get_order_gt
# from .views import year_post, MonthPost, post_detail
# from .views import my_view
# from .views import TemplIf
# from .views import view_for
# from .views import index, about
# from .views import author_posts, post_full

urlpatterns = [
     path('orders/', get_orders, name='orders'),
     path('order/<int:order_id>/', get_order, name='get_order'),
     path('delta/<int:delta>/', get_order_gt, name='get_order_gt'),
     # path('posts/<int:year>/', year_post, name='year_post'),
     # path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
     # path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
     # path('', my_view, name='index'),
     # path('if/', TemplIf.as_view(), name='templ_if'),
     # path('for/', view_for, name='templ_for'),
     # path('index/', index, name='index'),
     # path('about/', about, name='about'),
     # path('author/<int:author_id>/', author_posts, name='author_posts'),
     # path('post/<int:post_id>/', post_full, name='post_full')

]