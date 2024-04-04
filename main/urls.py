from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('name/', views.name, name='author_name'),
    re_path('project/', views.project, name='project_info')
]
