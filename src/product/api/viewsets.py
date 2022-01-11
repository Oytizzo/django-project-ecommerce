from rest_framework import viewsets
from product.models import Product, ProductVariant

from .serializers import ProductSerializer, ProductVariantSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductVariantViewset(viewsets.ModelViewSet):
    queryset = ProductVariant
    serializer_class = ProductVariantSerializer
