from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=50)
	password_re = models.CharField(max_length=50)