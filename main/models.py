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

class Reviews(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    review = models.CharField(max_length=500)
    rating = models.CharField(max_length=10)
    time = models.DateTimeField()

