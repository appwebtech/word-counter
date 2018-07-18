from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def josembi(request):
	return HttpResponse('Django sucks cos it has very few dependencies!')