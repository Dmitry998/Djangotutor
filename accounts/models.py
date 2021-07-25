from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'В дом'),
        ('Out door', 'Не в дом'),
    )
    name = models.CharField(max_length=150)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=150, choices=CATEGORY)
    description = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'В ожидании'),
        ('Out for delivery', 'Доставляется'),
        ('Delivered', 'Доставлено'),
    )
    # если при удалении ставим null, то надо явно прописать null=True
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, choices=STATUS)

    def __str__(self):
        return self.product.name
