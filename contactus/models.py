from django.db import models

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=100, null=False)
    message = models.CharField(max_length=500, null=False)

    class Meta:
        db_table = "contact us"