from rest_framework.serializers import ModelSerializer
from .models import Cart
from products.serializers import ProductSerializer

class CartSerializer(ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = '__all__'


class UpdateCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'