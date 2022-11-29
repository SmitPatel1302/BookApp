from django.db import models

# Class to store the user's address
class UserAddress(models.Model):
    id = models.AutoField(primary_key=True)
    house = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)