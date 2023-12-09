from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)