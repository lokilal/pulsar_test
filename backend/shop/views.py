from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
