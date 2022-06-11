from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun(request):
    return HttpResponse('hello')

def fun1(request):
    return HttpResponse('hiii')

def us(request):
    return render(request, 'user/u.html')

def user(request):
    return render(request,'user/user.html')
