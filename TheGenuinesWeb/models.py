from django.db import models
from django.forms.fields import CharField



# Create your models here.
class MyOrderInfo(models.Model):
    Name = models.CharField(max_length = 300)
    Phone = models.IntegerField()
    Email = models.EmailField()
    AdditionalInfo = models.TextField()
    Product = models.CharField(max_length = 300)
    Amount = models.IntegerField()
    OrderDate = models.DateField(auto_now=False, auto_now_add=True)
    OrderTime = models.TimeField(auto_now=False, auto_now_add=True)
    
    
    def __str__(self):
        return self.Name



