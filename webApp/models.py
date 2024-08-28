from email.policy import default

from django.db import models

# Create your models here.



class Applicant(models.Model):
    first_name = models.CharField(max_length=15,default=None)
    last_name = models.CharField(max_length=15,default=None)
    age = models.IntegerField(default=None)
