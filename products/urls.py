from django.urls import path
from .views import (
    ProductList,
    ProductDetails
)

urlpatterns = [
    path('', ProductList.as_view(), name='productList_url'),
    path('<int:p>', ProductDetails.as_view(), name='productDetails_url'),
]
