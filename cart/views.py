from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Cart, Product
from .serializers import (
    CartSerializer,
    UpdateCartSerializer
)


def GetProduct(productId):
    try:
        return Product.objects.get(id=productId)
    except:
        return None


# Create your views here.
class AddProductToCart(APIView):
    def get(self, request, pId):
        data = {
            "user": request.user,
            "product": GetProduct(pId),
        }
        print(data)
        serializeCart = UpdateCartSerializer(data=data)
        if serializeCart.is_valid():
            serializeCart.save()
            return Response(status=status.HTTP_201_CREATED)
        message = 'Product does not found.'
        return Response(message, status=status.HTTP_404_NOT_FOUND)


class RemoveProductToCart(APIView):
    def get(self, request, pId):
        pass


class GetProductsIntoCart(APIView):
    def get(self, request):
        cartItems = Cart.objects.filter(user=request.user)
        serializeCart = CartSerializer(cartItems, many=True)
        return Response(serializeCart.data, status=status.HTTP_200_OK)


class IncreaseQuentityOfProduct(APIView):
    def get(self, request, pId):
        pass


class DecreaseQuentityOfProduct(APIView):
    def get(self, request, pId):
        pass