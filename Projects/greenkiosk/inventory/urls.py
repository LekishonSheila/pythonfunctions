from django.urls import path 
from .views import product_upload_view
from .views import products_list
from .views import product_detail_view


urlpatterns = [
    path("products/upload/", product_upload_view, name="product_uploadview"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>/",product_detail_view,name="products_detail"),
   
]