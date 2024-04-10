from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # cloth
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=255, default='black')
    size = models.CharField(max_length=255, default='medium')
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title