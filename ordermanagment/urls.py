from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('all_orders/', views.all_orders, name='all_orders'),  # All orders page
]