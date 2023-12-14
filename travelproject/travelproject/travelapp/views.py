from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import people


# Create your views here.


def demo(request):
    # return HttpResponse("Hello World")
    #name = "India"
    obj=place.objects.all()
    obj1=people.objects.all()
    return render(request, "index.html", {'result': obj,'res': obj1})

"""
def about(request):
    return render(request, "about.html")


def addition(request):
    return render(request, "additionform.html")


def add(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    sum = x + y
    balance = x - y
    product = x * y
    res = x / y
    return render(request, "result.html", {'add': sum,'sub': balance,'mul': product,'div': res})
"""