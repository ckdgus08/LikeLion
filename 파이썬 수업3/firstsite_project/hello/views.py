from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request, 'home.html')
def count(request) :
    return render(request, 'count.html')
