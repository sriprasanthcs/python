from django.db import models

# Create your models here.
class crudapp(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    semail = models.CharField(max_length=20)