from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('upload/', views.upload_product, name='upload_product'),
    path('products/', views.product_list, name='product_list'),
]
