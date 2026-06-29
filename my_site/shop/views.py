from django.shortcuts import render
from django.http import HttpResponse

class Person:

    def __init__(self, name):
        self.name = name

def index(request):

    data = {
        'clients': {
            'client_one': "slava petrov",
            'client_two': "olga gerasimova",
            'client_three': "fedor borisov"
        },
        'users': ["bob", "petr", "alexandr"]
    }

    return render(request, "shop/index.html", context=data)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, "shop/contact.html")
