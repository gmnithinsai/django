from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',
    {
    'name':'Nithin',
    'age' : 21,
    'role' : 'Junior Software Engineer'})

def add(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    return render(request, 'result.html',{'result':n1+n2})