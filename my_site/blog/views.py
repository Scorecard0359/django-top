from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Главная страница</h1>
        <p><a href='/post'>Список постов</a></p>
    """)

def post_list(request):
    return HttpResponse("""
        <h1>Список постов</h1>
        <p><a href='/post/1'>Первый пост</a></p>
    """)

def get_post(request, id):
    return HttpResponse(f"""
        <h1>Пост {id}</h1>
        <p>немножечно текст</p>
        <p><a href="/post/{id}/comments">Комментарии</a></p>
    """)

def get_post_comments(request, id):
    return HttpResponse(f"""
        <h2>Комментарии поста {id}:</h2>
        <ul>
            <li>эт конечно замечательно, но не мог бы также описать получение всех ачивок?</li>
            <li>memento mori</li>
            <li>Пусто здесь...</li>
        </ul>
    """)
