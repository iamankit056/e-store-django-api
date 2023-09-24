from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Cart, Product
from .serializers import (
    CartSerializer,
    UpdateCartSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

def GetProduct(productId):
    try:
        return Product.objects.get(id=productId)
    except:
        return None


def GetCartProduct(cartId):
    try:
        return Cart.objects.get(id=cartId)
    except:
        return None


# Create your views here.
class AddProductToCart(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, pId):
        data = {
            "user": request.user,
            "product": GetProduct(pId),
        }
        print(data)
        serializeCart = UpdateCartSerializer(data=data)
        if serializeCart.is_valid():
            serializeCart.save()
            return Response(status=status.HTTP_201_CREATED)
        message = 'Product does not add.'
        return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)


class RemoveProductToCart(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def delete(self, request, cartId):
        cartItem = GetCartProduct(cartId)
        if cartItem is not None:
            serializeCartItem = CartSerializer(cartItem)
            cartItem.delete()
            return Response(data=serializeCartItem.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class GetProductsIntoCart(APIView):
    def get(self, request):
        cartItems = Cart.objects.filter(user=request.user)
        serializeCart = CartSerializer(cartItems, many=True)
        return Response(serializeCart.data, status=status.HTTP_200_OK)

