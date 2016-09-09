from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class User(models.Model):
	userid = models.IntegerField(unique = True)
	age = models.IntegerField()
	sex = models.CharField(max_length=1)
	occupation = models.CharField(max_length=50)
	zipcode = models.IntegerField(max_length=20) 
	avg = models.FloatField()



