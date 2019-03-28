from django.db import models

# Create your models here.
class Institution(models.Model):
    inst_name = models.CharField(max_length = 60)
    inst_pic = models.ImageField(upload_to = 'institutions/')

    def __str__(self):
        return self.inst_name



class Profile(models.Model):
    name  = models.CharField(max_length = 60)
    inst = models.ForeignKey(Institution)
    contact = models.IntegerField(default = 0)
    email = models.CharField(max_length = 60)
    dpic = models.ImageField(upload_to = 'profiles/')
    joined = models.CharField(max_length = 60)
    left =  models.CharField(max_length = 60)



    def __str__(self):
        return self.name
