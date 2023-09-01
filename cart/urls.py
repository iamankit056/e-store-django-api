from django.urls import path
from .views import (
    AddProductToCart,
    RemoveProductToCart,
    GetProductsIntoCart,
    IncreaseQuentityOfProduct,
    DecreaseQuentityOfProduct
)


urlpatterns = [
    path('', GetProductsIntoCart.as_view(), name='cart_products_url'),
    path('<int:pId>/add', AddProductToCart.as_view(), name='cart_add_product_url'),
    path('<int:pId>/remove', RemoveProductToCart.as_view(), name='cart_remove_product_url'),
    path('<int:pId>/increase', IncreaseQuentityOfProduct.as_view(), name='cart_increase_product_url'),
    path('<int:pId>/decrease', DecreaseQuentityOfProduct.as_view(), name='cart_decrease_product_url'),
]
