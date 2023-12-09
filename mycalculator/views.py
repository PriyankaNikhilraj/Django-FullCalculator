from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'calcu.html')


def calcu(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        myDict = {
            "q": q,
            "ans": ans,
            "error": False
        }
        return render(request, 'calcu.html', context=myDict)
    except:
        myDict = {
            "error": True,
        }
        return render(request, 'calcu.html', context=myDict)