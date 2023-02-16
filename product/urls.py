from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('home/', home, name='home'),
    path('adminlogin/', adminlogin, name='adminlogin'),
    path('admin-add-product/', admin_add_product, name='admin-add-product'),
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin-delete-product/<int:pk>', admin_delete_product, name='admin-delete-product'),
    path('admin-update-product/<int:pk>', admin_update_product, name='admin-update-product'),
    path('adminlogout/', admin_logout, name='adminlogout'),
    path('product-catalogue/', product_catalogue, name='product-catalogue'),
]
