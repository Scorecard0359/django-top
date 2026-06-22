from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная страница</h1>")

def about(request):
    return HttpResponse("О нас")

def contact(request, name: str, age: int, email: str):
    return HttpResponse(f"""
        <h2>Name: {name}</h2>
        <h2>Age: {age}</h2>
        <h2>E-mail: {email}</h2>
    """)

def browser_info(request):
    return HttpResponse(f"""
        <p>Схема запроса: {request.scheme}</p>
        <p>Вес тела (байт): {request.body}</p>
        <p>IP-адрес клиента: {request.META['REMOTE_ADDR']}</p>
    """)

def user(request, name="undefined", age=0):
    return HttpResponse(f"Username: {name} Age: {age}")

def product(request, id):
    return HttpResponse(f"Список товаров {id}")

def new_products(requests, id):
    return HttpResponse(f"Новые товары {id}")

def top_products(requests, id):
    return HttpResponse(f"Популярные продукты {id}")
