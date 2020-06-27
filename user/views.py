from django.shortcuts import render
from .form import userForm
from .models import Student
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
	errors = []
	form = userForm()
	if request.method == 'POST':
		form = userForm(request.POST)
		if form.is_valid():
			user1 = request.POST.get('name')
			password = request.POST.get('password')
			passwordre = request.POST.get('password_re')
			if passwordre == password:
				Student.objects.create(name=user1,password=password)
				print('user created')
			else:
				errors.append('password does not match')

	context= {
		'form' : form,
		'errors' : errors
	}
	return render(request,"signup.html",context)
				

