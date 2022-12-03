from django.db import models

# Create your models here.
class Bank(models.Model):
    acc_holder_name = models.CharField(max_length=100)
    acc_no = models.FloatField()
    acc_type = models.CharField(max_length=100)
    
