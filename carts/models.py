from django.db import models
from products.models import Product
# Create your models here.

class Cart(models.Model):
    products=models.ManyToManyField(Product,blank=True)
    total=models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cart Id %s" %(self.id)
