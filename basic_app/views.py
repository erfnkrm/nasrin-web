from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def education(request):
    return render(request,'basic_app/education.html')


def experience(request):
    return render(request,'basic_app/experience.html')

def media(request):
    return render(request,'basic_app/media.html')


