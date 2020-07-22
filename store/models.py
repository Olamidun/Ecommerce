from django.db import models
from PIL import Image
from cloudinary.models import CloudinaryField

# Create your models here.


class Product(models.Model):
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=200)
    images = CloudinaryField('product_pics', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

