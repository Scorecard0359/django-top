from django.shortcuts import render
from django.http import HttpResponse

newsposts = {
    1: "аномальная жара в Европе привела к обновлению в нескольких странах рекордов максимальной температуры воздуха за всю историю наблюдений и гибели более 1300 человек",
    2: "начались матчи основных сеток профессионального теннисного травяного турнира серии Большого шлема Уимблдонского турнира",
    3: "вспышка лихорадки Эбола (2026): Во Франции впервые установлен случай заражения Эболой у врача, который работал с гуманитарной миссией в Демократической республике Конго, охваченной эпидемией Эболы с середины мая. Министерство здравоохранения Франции подчеркнуло, что заболевший изолирован в специализированное учреждение и что в изоляцию его поместили ещё до того, как у него подтвердили вирус"
}

def index(request):
    return render(request, 'news/index.html', context={'news': newsposts})

def contact(request):
    return render(request, 'news/contact.html')

def post(request, id):
    if id in newsposts:
        content = newsposts[id]
    else:
        content = "empty"
    return render(request, 'news/post.html', context={'id': id, 'content': content})
