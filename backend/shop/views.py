from rest_framework import viewsets, mixins

from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
