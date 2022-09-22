from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('path', 'formats', )

    def get_path(self, obj):
        #obj.image_original.name
        return f'media/images/{obj.image_original.name.split(".")[0]}'

    def get_formats(self, obj):
        return [obj.image_original.name.split('.')[1],
                'webp']

class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer()

    class Meta:
        model = Product
        fields = '__all__'
