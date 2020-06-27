from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_create_view1(request):
	form = ProductForm() #request.POST or None
	error = []
	print(request.POST)
	if request.method == 'POST':
		title = request.POST.get('title')
		if not title:
			error.append("title reuqired")
		form = ProductForm(request.POST)
		if form.is_valid():
			obj = form.save()
			form = ProductForm()
		else:
			print("error")	
	context = {
	'form': form
	}
	# context = {
	# 	"title": obj.title,
	# 	"description" : obj.description
	# }
	return render(request,"products/product_create.html",context)




# def product_detail_view(request):
# 	obj=Product.objects.get(id=1)
# 	# context = {
# 	# 	"title": obj.title,
# 	# 	"description" : obj.description
# 	# }
# 	context = {
# 		'object' : obj
# 	}
# 	return render(request,"products/product_detail.html",context)