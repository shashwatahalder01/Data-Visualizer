from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Product(models.Model):
    date = models.DateField(auto_now_add=False,auto_now=False)
    chal = models.FloatField()
    dal = models.FloatField()
    salt = models.FloatField()
    oil = models.FloatField()
    honey = models.FloatField()
    butter = models.FloatField()
    milk = models.FloatField()
    class Meta:
      db_table = 'product' 
        


    
        
        
   
            