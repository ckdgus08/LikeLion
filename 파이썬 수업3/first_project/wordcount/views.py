from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request, 'home.html')
def about(request) :
    return render(request, 'about.html')
def count(request) :
    text = request.GET['textarea']
    list = text.split()
    dic = {}

    for i in list :
        if i in dic :
            dic[i] = dic[i]+1
        else :
            dic[i] = 1

    return render(request, 'count.html', {'full' : text, 'total' : len(list), 'dict' : dic.items()})
