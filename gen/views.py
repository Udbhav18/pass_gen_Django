from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.

def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,"about.html")

def password(request):
	length = int(request.GET.get('length',8))
	chars = list('qwertyuiopasdfghjklzxcvbnm')
	if request.GET.get('uppercase'):
		chars.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
	if request.GET.get('numbers'):	
		chars.extend('1234567890')
	if request.GET.get('spchar'):
		chars.extend('`~!@#$%^&*()-_+<>?/;"')

	npass = ''
	
	for x in range(length):
		npass+=random.choice(chars)
	return render(request,'password.html',{'password':npass})