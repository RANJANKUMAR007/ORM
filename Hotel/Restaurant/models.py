from django.db import models
from django.contrib import admin
class HotelsD(models.Model):
    customerid= models.IntegerField(primary_key=True)
    orderid= models.IntegerField()
    age = models.IntegerField()
    cust_no = models.IntegerField()
    rate = models.IntegerField()
class HotelsDAdmin(admin.ModelAdmin):
    list_display=('customerid','orderid','age','cust_no','rate')