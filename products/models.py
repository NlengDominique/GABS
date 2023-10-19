from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(upload_to='products/images', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

