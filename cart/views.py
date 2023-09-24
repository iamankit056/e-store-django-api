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
        product = GetProduct(pId)
        if product is None:
            message = 'Product does not Found.'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        createCartItem = Cart(user=request.user, product=product)
        print(createCartItem)
        createCartItem.save()
        return Response(status=status.HTTP_201_CREATED)


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
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        cartItems = Cart.objects.filter(user=request.user)
        serializeCart = CartSerializer(cartItems, many=True)
        return Response(serializeCart.data, status=status.HTTP_200_OK)

