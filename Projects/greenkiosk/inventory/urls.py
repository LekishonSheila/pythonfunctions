from django.urls import path 
from .views import product_upload_view
from .views import products_list
from .views import productdetailview
from .views import add_to_cart
from .views import edit_product_view
from .views import cart_list


urlpatterns = [
    path("products/upload/", product_upload_view, name="product_uploadview"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>/",productdetailview,name="productsdetail"),
    path("products/add_to_cart", add_to_cart, name="add_to_cart_view"),
    path("products/edit/<int:id>/", edit_product_view, name= "product_edit_view"), 
    path("cart/cartlist",cart_list, name="cart_list_view"),

   
]