from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home_view(request, *args, **kwargs):
	print(args, "test",kwargs)
	print(request.user)
	return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Contact Page</h1>")	
	my_context = {
	"my_text" : "this is your username",
	"my_number" : 123,
	"my_list" 	: [4323,12312, 53,"asc"]
	}
	return render(request,"contact.html",my_context)
	#return JsonResponse(my_context)

def social_view(request, *args, **kwargs):
	return render(request,"social.html",{})


def info_view(request, *args, **kwargs):
	return render(request,"info.html",{})