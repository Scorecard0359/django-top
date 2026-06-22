from django.contrib import admin
from django.urls import path, include, re_path
from blog import views

blogpatterns = [
    path('', views.post_list),
    path('<int:id>', views.get_post),
    path('<int:id>/comments', views.get_post_comments),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('post/', include(blogpatterns)),
]
