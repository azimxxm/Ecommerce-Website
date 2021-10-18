from django.db import models

class Product_size(models.Model):
    product_size = models.CharField(max_length=10)

    def __str__(self):
        return self.product_size
    
    class Meta:
        verbose_name = "Product_size"
        verbose_name_plural = "Product_size"


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_size_id = models.ManyToManyField(Product_size, related_name="product")
    product_info = models.TextField(max_length=300)
    product_photo_1 = models.ImageField(upload_to="Product/%Y/%M/")
    product_photo_2 = models.ImageField(upload_to="Product/%Y/%M/", blank=True)
    product_photo_3 = models.ImageField(upload_to="Product/%Y/%M/", blank=True)
    product_photo_4 = models.ImageField(upload_to="Product/%Y/%M/", blank=True)
    product_photo_5 = models.ImageField(upload_to="Product/%Y/%M/", blank=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"