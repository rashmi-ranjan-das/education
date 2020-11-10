from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

class WebDev(models.Model):
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

class Arduino(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

class Reviews(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    review = models.CharField(max_length=500)
    rating = models.CharField(max_length=10)
    time = models.DateTimeField()

class Quotes(models.Model):
    name = models.CharField(max_length=40)
    quote = models.CharField(max_length=1000)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    number = models.IntegerField()
    education = models.CharField(max_length=100)
    feedback = models.CharField(max_length=1000)
