from django.urls import path, include
from .import views


urlpatterns = [
    path('products/list', views.product_list, name='list'),
    path('products/add', views.register_product, name='create')
   
]
