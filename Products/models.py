from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )

    status = models.CharField(max_length=10,choices=STATUS_CHOICE , default='Active')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
 
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_image = models.ImageField(upload_to='media/productimages/', null=True, blank=True)
    
    # Ye ForeignKey aapke dropdowns banayengi
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name

