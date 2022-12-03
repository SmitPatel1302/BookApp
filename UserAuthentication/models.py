from django.db import models
from django.contrib.auth.models import AbstractUser

# Class to store the user's registration data
class CustomUserAuthentication(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    country_code = models.CharField(max_length=5, null=False)
    phone_number = models.CharField(max_length=25, null=False)
    panelty = models.IntegerField(default=0)
    profession = models.CharField(max_length=50)
    address_id = models.ForeignKey("UserAddress", on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'  # Set email as the unique login field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Field for which django ask when create superuser
    list_fields = ['first_name', 'last_name', 'email', 'country_code', 'phone_number', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']