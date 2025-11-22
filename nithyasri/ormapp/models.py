from django.db import models
from django.contrib import admin
class Product(models.Model):
    sl_no=models.IntegerField
    category=models.CharField()
    price=models.FloatField()
    stockquantity=models.IntegerField()
    rating=models.FloatField()
    description=models.CharField()
    maximum_retail_price=models.IntegerField()

class ProductAdmin(admin.ModelAdmin):
    list_display=["sl_no","category","price","stockquantity","rating","description","maximum_retail_price"]




