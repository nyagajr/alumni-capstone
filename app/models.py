from django.db import models

# Create your models here.
class Institution(models.Model):
    inst_name = models.CharField(max_length = 60)
    inst_pic = models.CharField(max_length = 60)



class Profile(models.Model):
    name  = models.CharField(max_length = 60)
    contact = models.IntegerField(default = 0)
    email = models.CharField(max_length = 60)
    dpic = models.CharField(max_length = 60)
    joined = models.CharField(max_length = 60)
