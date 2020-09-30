from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

class Cplusplus(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

class Python(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

class MLAI(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

