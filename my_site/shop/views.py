from django.shortcuts import render
from django.http import HttpResponse

class Person:

    def __init__(self, name):
        self.name = name

def index(request):

    data = {
        'array': [4, 3, 86, 24, 46]
    }

    return render(request, "shop/index.html", context=data)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, "shop/contact.html")
