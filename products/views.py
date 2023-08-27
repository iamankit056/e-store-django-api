from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from .serializers import (
    CategorySerializer,
    ProductSerializer
)
from .models import (
    Category,
    Product
)

# Create your views here.
class ProductList(APIView):
    authentication_classes = (JWTTokenUserAuthentication, )
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        products = Product.objects.all()
        serializeProducts = ProductSerializer(products, many=True)
        return Response(serializeProducts.data, status=status.HTTP_200_OK)


class ProductDetails(APIView):
    authentication_classes = (JWTTokenUserAuthentication, )
    permission_classes = (IsAuthenticated, )
    def GetProduct(self, productId):
        try:
            return Product.objects.get(id=productId)
        except:
            return None

    def get(self, request, p):
        product = self.GetProduct(productId=p)

        if product is None:
            response = {
                'error': 'Product not found'
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)

        serializeProduct = ProductSerializer(product)
        return Response(serializeProduct.data, status=status.HTTP_200_OK)

