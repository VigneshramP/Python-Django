from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sayHello(request):
	return HttpResponse("<===== WELCOME TO FIFTH GENERATION TECHNOLOGIES =====>")

def Addition(request):
	a = 10
	b = 5
	return HttpResponse(a + b)	

def Subraction(request):
	a = 10
	b = 5
	return HttpResponse(a - b)

def Multiply(request):
	a = 56
	b = 65
	return HttpResponse(a * b)

def Division(request):
	a = 56
	b = 2
	return HttpResponse(a / b)

def say_hello(request):
	return render(request,'hello.html')

def form(request):
	return render(request,'form.html')
