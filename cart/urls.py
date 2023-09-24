from django.urls import path
from .views import (
    AddProductToCart,
    RemoveProductToCart,
    GetProductsIntoCart
)


urlpatterns = [
    path('', GetProductsIntoCart.as_view(), name='cart_products_url'),
    path('<int:pId>/add', AddProductToCart.as_view(), name='cart_add_product_url'),
    path('<int:cartId>/remove', RemoveProductToCart.as_view(), name='cart_remove_product_url'),
]
