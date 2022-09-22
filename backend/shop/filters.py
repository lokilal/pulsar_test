import django_filters as filters

from .models import Product


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )
    article = filters.CharFilter(
        field_name='article',
        lookup_expr='icontains',
    )
    status = filters.CharFilter(
        field_name='status',
        lookup_expr='icontains',
    )

    class Meta:
        model = Product
        fields = ('status', 'article', 'title', )
