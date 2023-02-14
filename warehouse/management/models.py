from django.db import models

# Create your models here.
#Planning warehouse db
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
#Gotta edit category as Field.choices https://docs.djangoproject.com/en/4.1/ref/models/fields/
    category = models.CharField(max_length=50)
#Items table
    #Item ID
    #Item name
    #Item size
    #Category
    #Item weight
class Warehouse:
    warehouse_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=70)
    filled = models.DecimalField()
#Warehouses table
    #Warehouse ID
    #Region
    #filled
class Stock:
    item_id = models.ForeignKey(Item)
    warehouse_id = models.ForeignKey(Warehouse)
    stock_state = models.IntegerField()
    target_state = models.IntegerField()
#Stock State table
    #Item ID
    #Warehouse ID
    #Stock State
    #Stock Target