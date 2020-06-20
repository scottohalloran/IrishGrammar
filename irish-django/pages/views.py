from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	#+from pages.namer import namer
	return render(request, "about.html", {})

