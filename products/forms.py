from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = (
			'title',
			'price',
			'description',
			'email'
			)

# class ProductForm2(forms.Form):
# 	title 		= forms.CharField(max_length=120) #max_lenth=required
# 	description = forms.CharField()
	
			