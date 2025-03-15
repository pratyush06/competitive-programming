from django.db import models

# Create your models here.

class Product(models.Model):
    owner=models.ForeignKey('auth.User', related_name='user_products', on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=150)
    size=models.FloatField(default=0, blank=True)
    qunatity=models.IntegerField(default=0, null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=3, default=0)
    
    def __str__(self) -> str:
        return self.name
    
    