from django.db import models

# Create your models here.
class empuser(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=250)

class empdata(models.Model):
    name=models.CharField(max_length=25)
    regno=models.IntegerField()
    age=models.IntegerField()
    yearofjoin=models.IntegerField()
    mobile=models.CharField(max_length=15)
    address=models.CharField(max_length=25)
    

