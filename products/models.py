from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120) #max_lenth=required
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=20)
	summary		= models.TextField(blank=False, null=False)#default false for both
	feature		= models.BooleanField(default=False)
	email		= models.EmailField(default='noemail@noemail.noemail')