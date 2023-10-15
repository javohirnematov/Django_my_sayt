from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('magazine', views.magazine),
    path('contacts', views.contacts),
    path('team', views.team),
    path('category/<int:pk>', views.get_exact_category),
    path('product/<int:pk>', views.get_exact_product, name='news-detail'),
    path('search', views.search_product),
    path('cart', views.user_cart),
    path('del-item/<int:pk>', views.del_from_cart),
    path('add-to-cart/<int:pk>', views.add_to_cart),
]
