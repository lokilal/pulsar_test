from django.db import models


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
    image = models.ImageField()
