from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def w(request):
    return HttpResponse('work started')

def wrk(request):
    return render(request,'w.html')