from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

blogcomments = {
    "comments": ["эт конечно замечательно, но не мог бы также описать получение всех ачивок?", "memento mori", "Пусто здесь..."]
}

blogpatterns = [
    path('', TemplateView.as_view(template_name="blog/list.html")),
    path('<int:id>', TemplateView.as_view(template_name="blog/post.html")),
    path('<int:id>/comments', TemplateView.as_view(template_name="blog/comments.html", extra_context=blogcomments)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="blog/index.html")),
    path('post/', include(blogpatterns)),
]

# shop

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     path('about/', TemplateView.as_view(template_name="shop/about.html", extra_context={"header": "Подробная информация"})),
#     path('contact/', TemplateView.as_view(template_name="shop/contact.html")),
# ]
