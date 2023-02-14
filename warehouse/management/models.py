from django.db import models

# Create your models here.
#Planning warehouse db
class Item(models.Model):
    category_choices = [
        ('FOO', 'Food'),
        ('BEA', 'Beauty'),
        ('CLO', 'Clothes'),
        ('HEA', 'Health'),
        ('ACC', 'Accessories'),
        ]
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
#Gotta edit category as Field.choices https://docs.djangoproject.com/en/4.1/ref/models/fields/
    category = models.CharField(max_length=3,choices=category_choices)
#Items table 
    #Item ID
    #Item name
    #Item size
    #Category
    #Item weight
class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=70)
    filled = models.IntegerField()
    max_capacity = models.IntegerField()
#Warehouses table
    #Warehouse ID
    #Region
    #filled
class Stock(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    stock_state = models.IntegerField()
    target_state = models.IntegerField()
#Stock State table
    #Item ID
    #Warehouse ID
    #Stock State
    #Stock Target