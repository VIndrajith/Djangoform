from email.policy import default

from django.db import models

# Create your models here.



class Applicant(models.Model):
    first_name = models.CharField(max_length=15,default=None)
    last_name = models.CharField(max_length=15,default=None)
    roll = models.IntegerField(null=True,default=None)
    course = models.CharField(max_length=15,default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=12,default=None)
