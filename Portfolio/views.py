from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contacts(request):
    return render(request, 'contacts.html')

def construction(request):
    return render(request, 'construction.html')