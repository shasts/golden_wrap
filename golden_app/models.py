from django.db import models

# Create your models here.

class Addon(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def _unicode_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    base_price = models.DecimalField(max_digits = 7, decimal_places = 2)
    short_description = models.CharField(max_length = 100)
    long_description = models.CharField(max_length = 1000)
    thumbnail = models.ImageField(upload_to = 'thumbnails')
    product_image = models.ImageField(upload_to = 'images')
    addons = models.ManyToManyField(Addon)

    def _unicode_(self):
        return self.name

class User(models.Model):
    email_id = models.EmailField(max_length = 75)

    def _unicode_(self):
        return self.email_id


class Item(models.Model):
    delivery_address = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    user = models.OneToOneField(User)
    product = models.OneToOneField(Product)

    def _unicode_(self):
        return self.product.name

