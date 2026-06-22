from django.contrib import admin
from django.urls import path, include, re_path
from blog import views

blogpatterns = [
    
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]
