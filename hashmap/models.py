import os
from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=30,blank=False)
    number= models.BigIntegerField(unique=True,blank=False)
    imei = models.BigIntegerField(blank=True)
    email = models.EmailField(max_length=100,unique=True,blank=False)
    latitude = models.DecimalField(max_length=20,decimal_places=9,max_digits=29,blank=True)
    longitude = models.DecimalField(max_length=20,decimal_places=9,max_digits=29,blank=True)
    address = models.CharField(max_length=150,blank=True)
    tags = models.CharField(max_length=250,blank=True)

    class Meta:
        unique_together = [("number", "email")]

class Places(models.Model):

    user_field = models.ForeignKey(User,related_query_name="emailID ")
    latitude = models.DecimalField(max_length=20,decimal_places=9,max_digits=29,blank=False)
    longitude = models.DecimalField(max_length=20,decimal_places=9,max_digits=29,blank=False)
    address = models.CharField(max_length=150,blank=True)
    name = models.CharField(max_length=200,blank=False)
    number = models.IntegerField(blank=False)
    category = models.CharField(max_length=300,blank=True)
    description = models.CharField(max_length=500,blank=True)
    website= models.URLField(blank=True)
    tag = models.CharField(max_length=250,blank=True)
    place_id= models.IntegerField(blank=False)
    # image = models.ImageField(blank=True,upload_to=get_upload_path())



'''
def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.Place.user_id, filename)
      '''