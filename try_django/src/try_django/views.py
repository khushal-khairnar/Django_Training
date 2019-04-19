from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	my_title="Hello There...."
	return render(request,"hello_world.html",{"title":my_title})	

def contact_page(request):
	
	return render(request,"hello_world.html",{"title":"Contact us"})	

def about_page(request):
	return render(request,"about.html",{"title":"About us"})	