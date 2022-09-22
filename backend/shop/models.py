from webptools import cwebp

from django.db import models


class ProductImage(models.Model):
    image_original = models.ImageField(upload_to='images/')
    image_webp = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        webp_image = self.image_original.path[:-4] + '.webp'
        cwebp(
            input_image=self.image_original.path,
            output_image=webp_image,
            option="-q 80", logging="-v"
        )
        self.image_webp = webp_image
        super(ProductImage, self).save()


class Product(models.Model):
    STATUS_CHOICE = (
        ('В наличии', 'В наличии'),
        ('Под заказ', 'Под заказ'),
        ('Ожидается поступление', 'Ожидается поступление'),
        ('Нет в наличии', 'Нет в наличии'),
        ('Не производится', 'Не производится'),
    )
    title = models.CharField(max_length=128)
    article = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICE, max_length=21)
    image = models.ForeignKey(
        ProductImage, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
